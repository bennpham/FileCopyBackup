'''
Created on Dec 20, 2014

@author: Ben
'''
import tkinter

class Help():
    ''' Displays how to use '''
    def __init__(self, menuobj: dict):
        self.MenuObj = menuobj
        
        self.MenuObj['help'] = tkinter.Toplevel()
        Yscrollbar = tkinter.Scrollbar(self.MenuObj['help'])
        Yscrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        Help = tkinter.Text(self.MenuObj['help'], background = "#f4f4f4",
                            width = round(self.MenuObj['help'].winfo_screenwidth()/16),
                            height = round(self.MenuObj['help'].winfo_screenheight()/32),
                            wrap = tkinter.WORD, yscrollcommand=Yscrollbar.set)
        Help.insert('1.0', '''Program will start and create "default.txt" in the directory that this 
program is in. "Default.txt" contains parameters that will automatically 
load into this program. You can modify these parameters in the destination 
boxes or options menu and hit "Save to Default" to modify your default 
settings. If "default.txt" already exists, program will automatically 
load from the presets that "default.txt" resides in.
        
Target destination:
    - Input destination to file or name of file in parent folder.
        * You will get invalid file pop up if file cannot be found
    - Click the folder button and browse for file to backup
        
Save Destination:
    - Input destination or name of folder to create in parent
    directory to save file.
    - Click the folder button and browse for file to backup
    
Save Destination 2:
    - Same as Save Destination
    
OPTION:
    + Save Dest 1 on start:
        - Backup file to save dest 1 location when program starts
    
    + Save Dest 2 on start:
        - Backup file to save dest 2 location when program starts
        
    + BOX TO SELECT SAVE TYPE:
        * Overwrite:
            - overwrite file in save destination folder
        * Daily:
            - creates a new folder with today's date
            - overwrite file in today's date backup folder
            - creates a new folder on different date
        * Exact:
            - creates a new folder with today's date
            - creates new folder with exact time
            - backup file into folder with exact time
            
Save to Default:
    - Save target destination, save destination 1 & 2, and 
    all settings in your option folder to "default.txt"
    
Load Set:
    - Load target destination, save destination 1 & 2, and
    all settings in your option folder based on selected
    text file presets. Nothing will change if text file doesn't 
    contain any valid parameters
    
Save Set:
    - Save target destination, save destination 1 & 2, and 
    all settings in your option folder to text file of your
    choice.
''') 
        Help.config(state=tkinter.DISABLED)
        Help.pack(fill=tkinter.BOTH, expand=1) 
        Yscrollbar.config(command=Help.yview)
        self.MenuObj['help'].protocol("WM_DELETE_WINDOW", self._cancel_help)
        self.MenuObj['help'].grab_set()
        self.MenuObj['help'].mainloop()
        
    def _cancel_help(self) -> None:
        ''' Turns the help root back to None so it can be called on again '''
        self.MenuObj['help'].destroy()
        self.MenuObj['help'] = None
    
    
    
class About():
    ''' Displays About '''
    def __init__(self, menuobj: dict):
        self.MenuObj = menuobj
        
        self.MenuObj['about'] = tkinter.Toplevel()
        About = tkinter.Text(self.MenuObj['about'], background = '#f4f4f4',
                             width = round(self.MenuObj['about'].winfo_screenwidth()/32),
                            height = round(self.MenuObj['about'].winfo_screenheight()/64),
                            wrap = tkinter.WORD)
        About.insert('1.0', "Version 1.0\n\n\
File Copy Backup developed using Python 3.4.1 \n\
by Ben Pham.")
        About.config(state=tkinter.DISABLED)
        About.pack(fill=tkinter.BOTH, expand=1) 
        self.MenuObj['about'].protocol("WM_DELETE_WINDOW", self._cancel_about)
        self.MenuObj['about'].grab_set()
        self.MenuObj['about'].mainloop()
        
    def _cancel_about(self) -> None:
        ''' Turns the about root back to None so it can be called on again '''
        self.MenuObj['about'].destroy()
        self.MenuObj['about'] = None
