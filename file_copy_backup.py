'''
Created on Dec 21, 2014

@author: Ben
'''
import inspect, os, glob, shutil, time
import create_new_default

class FileCopyBackup(object):
    '''
    Handles copying and backing up files
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.destination = {"target": "", "save": "", "save2": ""}
        
        self.Parameters = {"dest1_save_on_start": 0, 
                            "dest2_save_on_start": 0, 
                            "save_dest1": "exact", "save_dest2": "overwrite"}
        
        self.error = 0
        
        self._load_default()
        
    def save_destination(self, which_destination: int)->None:
        '''
        - Pick which destination to save as parameter. 
        - Back a backup of the file in target destination to folder
        in save or save2 depending on parameters.
        - Will make overwrite backup or new folders to store backup
        depending on save_dest or save_dest2 in parameters 
        - If folder doesn't exist, folder will be created
        '''
        save_destination = ""
        save_parameter = ""
        
        if which_destination == 1:
            save_destination = self.destination['save']
            save_parameter = self.Parameters['save_dest1'] 
        elif which_destination == 2:
            save_destination = self.destination['save2']
            save_parameter = self.Parameters['save_dest2']  
            
        if save_parameter == "overwrite":
            if not os.path.exists(save_destination):
                os.makedirs(save_destination)
            shutil.copy2(self.destination['target'], save_destination)
            
        if save_parameter == "daily":
            time_now = time.gmtime(time.time())
            new_folder = save_destination + "\\" + str(time_now.tm_year) + "-" \
                        + str(time_now.tm_mon) + "-" + str(time_now.tm_mday)
            if not os.path.exists(new_folder):
                os.makedirs(new_folder)
            shutil.copy2(self.destination['target'], new_folder)
            
        if save_parameter == "exact":
            time_now = time.gmtime(time.time())
            new_folder = save_destination + "\\" + str(time_now.tm_year) + "-" \
                        + str(time_now.tm_mon) + "-" + str(time_now.tm_mday) \
                        + "\\" + str(time_now.tm_hour) + "h " + str(time_now.tm_min) \
                        + "m " + str(time_now.tm_sec) + "s"
            if not os.path.exists(new_folder):
                os.makedirs(new_folder)
            shutil.copy2(self.destination['target'], new_folder)
        
    def make_default(self)->None:
        ''' Overwrites the old default.txt with new values '''
        create_new_default.create_new_default(self.current_directory + "\\default.txt",
                                              self.destination, self.Parameters)
    
    def load_set(self, select_file:str)->None:
        '''
        Load parameters with text file into class with new values if text
        contains valid parameters somewhere inside
        '''
        with open(select_file, 'r') as file:
            for line in file:
                if line[0:20] == 'TARGET DESTINATION =':
                    self.destination['target'] = line[20:].rstrip().lstrip()
                elif line[0:18] == 'SAVE DESTINATION =': 
                    self.destination["save"] = line[18:].rstrip().lstrip()
                elif line[0:19] == 'SAVE DESTINATION2 =': 
                    self.destination["save2"] = line[19:].rstrip().lstrip()
                elif line[0:20] == 'SAVE STARTUP DEST1 =':
                    self.Parameters['dest1_save_on_start'] = int(line[20:])
                elif line[0:20] == 'SAVE STARTUP DEST2 =':
                    self.Parameters['dest2_save_on_start'] = int(line[20:])
                elif line[0:17] == 'SAVE TYPE DEST1 =':
                    self.Parameters['save_dest1'] = line[17:].rstrip().lstrip()
                elif line[0:17] == 'SAVE TYPE DEST2 =':
                    self.Parameters['save_dest2'] = line[17:].rstrip().lstrip()
    
    def save_set(self, file:str)->None:
        '''
        Save current parameters to a text file of your choice
        '''
        create_new_default.create_new_default(file, self.destination, self.Parameters)
    
    #===========================================================================
    # PRIVATE
    #===========================================================================
    def _load_default(self)->None:
        '''
        - Check if default.txt exists
        - If default.txt doesn't exist, creates one and loads in default empty
        parameters
        - If default.txt exist, gets default settings and load it in init
        '''
        _self_file = inspect.getfile(inspect.currentframe())
        self.current_directory = os.path.dirname(os.path.abspath(_self_file))
        
        if (len(glob.glob(self.current_directory + "\\default.txt")) == 0):
            create_new_default.create_new_default("default.txt", self.destination, self.Parameters)
        else:
            try:
                self.load_set("default.txt")
            except ValueError:
                self.error = 1
            
