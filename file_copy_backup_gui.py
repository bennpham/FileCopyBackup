'''
Created on Dec 20, 2014

@author: Ben
'''
import tkinter, PIL.ImageTk
from tkinter import messagebox
from tkinter import filedialog
import helpmenu, option, file_copy_backup

class FileCopyBackupGUI(object):
    '''
    Handles GUI of FileCopyBackup
    '''
    BACKGROUND = '#f4f4f4'


    def __init__(self, param: file_copy_backup.FileCopyBackup()):
        ''' Constructor '''
        self.FileCopyBackup = param
        self._exec_default()
        self._root_exec()
        
        self.frame1_resolution = {'width': 512, 'height': 512 * 13/20}
        self.frame = None
        
        self.frame_blank_resolution = {'width': 512, 'height': 512 * 1/20}
        self.frame_blank = None
        
        self.frame2_resolution = {'width': 512, 'height': 512 * 3/20}
        self.frame2 = None
        
        self.frame3_resolution = {'width': 512, 'height': 512 * 3/20}
        self.frame3 = None
        
        self.MenuObj = {'about': None, 'help': None, 'option': None}
        
        self.menu_bar()
        self.newset()
        self._ROOT.protocol("WM_DELETE_WINDOW", self.quit)
        
        if self.FileCopyBackup.error == 1:
            tkinter.messagebox.showwarning("Invalid Parameter", '"default.txt" contains one or more invalid parameters.\n\n\
Program will load all valid settings.\n\n\
Please click SAVE TO DEFAULT to save current settings to "default.txt" with valid parameters.')
        
        self._ROOT.mainloop()
        
    #===========================================================================
    # MENU
    #===========================================================================
    def menu_bar(self)->None:
        ''' Displays menu '''
        menubar = tkinter.Menu(self._ROOT)
        self._filemenu(menubar)
        self._actionmenu(menubar)
        self._helpmenu(menubar)
        self._ROOT.config(menu=menubar)
        
    #===========================================================================
    # DISPLAY
    #===========================================================================
    def newset(self)->None:
        ''' main screen '''
        self._frame_exec()
        self._frame_blank_exec()
        self._frame_exec2()
        self._frame_exec3()
        
        self._frame_objects1()
        self._frame_objects2()
        self._frame_objects3()
        
    #===========================================================================
    # OPTION
    #===========================================================================
    def loadset(self)->None:
        ''' Load text file with specified parameters ''' 
        ftypes = [('Text files', '*.txt')]
        dialog = tkinter.filedialog.askopenfilename(filetypes=ftypes, defaultextension="*.txt")
        if dialog != '':
            try:
                self.FileCopyBackup.load_set(dialog)
                self.entry_tar_dest.delete(0, tkinter.END)
                self.entry_tar_dest.insert(0, dialog)
                self.entry_save_dest.delete(0, tkinter.END)
                self.entry_save_dest.insert(0, dialog)
                self.entry_save_dest2.delete(0, tkinter.END)
                self.entry_save_dest2.insert(0, dialog)
            except ValueError:
                tkinter.messagebox.showwarning("Invalid Parameter", "One or more parameters inside this text file contains invalid settings.")
        
    def saveset(self)->None:
        ''' Save text file with specified parameters '''
        ftypes = [('Text files', '*.txt')]
        dialog = tkinter.filedialog.asksaveasfilename(filetypes=ftypes, defaultextension="*.txt")
        if dialog != '':
            self.FileCopyBackup.save_set(dialog)
        
    def makedefault(self)->None:
        ''' Save text file with specified parameters to default.txt '''  
        self.FileCopyBackup.make_default()
        
    def option(self)->None:
        ''' Allows user to modify settings '''
        option.Option(self.FileCopyBackup)
        
    def quit(self)->None:
        ''' Shutdowns all active windows and closes the application '''
        self._ROOT.destroy()
        
    #===========================================================================
    # ACTION
    #===========================================================================
    def backup(self)->None:
        ''' Creates backup #1 '''
        try:
            self.FileCopyBackup.save_destination(1)
        except FileNotFoundError:
            tkinter.messagebox.showerror("File Not Found Error", "File cannot be found.\n\nPress OK to continue.")
        except:
            tkinter.messagebox.showerror("Unknown Error", "An unknown error has occurred.\n\nPress OK to continue.")
        else:
            tkinter.messagebox.showinfo("SUCCESS", "Backup #1 successful.\n\nPress OK to continue.")
        
    def backup2(self)->None:
        ''' Creates backup #2 '''
        try:
            self.FileCopyBackup.save_destination(2)
        except FileNotFoundError:
            tkinter.messagebox.showerror("File Not Found Error", "File cannot be found.\n\nPress OK to continue.")
        except:
            tkinter.messagebox.showerror("Unknown Error", "An unknown error has occurred.\n\nPress OK to continue.")
        else:
            tkinter.messagebox.showinfo("SUCCESS", "Backup #2 successful.\n\nPress OK to continue.")
    
    #===========================================================================
    # INSTRUCTION
    #===========================================================================
    def about(self)->None:
        ''' Displays information about program '''
        helpmenu.About(self.MenuObj) 
    
    def help(self)->None:
        ''' Displays information on how to use '''
        helpmenu.Help(self.MenuObj) # EDIT WORDS
        
    #===========================================================================
    # PRIVATE
    #===========================================================================
        #=======================================================================
        # Menu
        #=======================================================================
    def _filemenu(self, menubar: 'menubar') -> None:
        ''' Displays the cascade labeled File '''
        filemenu = tkinter.Menu(menubar, tearoff = 0)
        filemenu.add_command(label='Load Set', command=self.loadset) 
        filemenu.add_command(label='Save Set', command=self.saveset)
        filemenu.add_command(label='Make Default', command=self.makedefault)
        filemenu.add_command(label='Option', command=self.option)
        filemenu.add_separator()
        filemenu.add_command(label='Quit', command=self.quit)
        menubar.add_cascade(label='File', menu = filemenu)
        
    def _actionmenu(self, menubar: 'menubar') -> None:
        ''' Displays the casade labeled Action '''
        actionmenu = tkinter.Menu(menubar, tearoff = 0)
        actionmenu.add_command(label='Backup', command=self.backup)
        actionmenu.add_separator()
        actionmenu.add_command(label='Secondary Backup', command=self.backup2)
        menubar.add_cascade(label='Action', menu = actionmenu)
        
    def _helpmenu(self, menubar: 'menubar') -> None:
        ''' Displays the cascade labeled Help '''
        helpmenu = tkinter.Menu(menubar, tearoff = 0)
        helpmenu.add_command(label='Help', command = self.help)
        helpmenu.add_separator()
        helpmenu.add_command(label='About', command=self.about)
        menubar.add_cascade(label='Help', menu=helpmenu)
        
        #=======================================================================
        # Display
        #=======================================================================
    
    def _change_resolution(self, event) -> None:
        self.resolution['width'] = self._ROOT.winfo_width()
        self.resolution['height'] = self._ROOT.winfo_height()
        
    def _frame1_change_resolution(self, event) -> None:
        self.frame1_resolution['width'] = self.frame.winfo_width()
        self.frame1_resolution['height'] = self.frame.winfo_height()
        
    def _frame_blank_change_resolution(self, event) -> None:
        self.frame_blank_resolution['width'] = self.frame_blank.winfo_width()
        self.frame_blank_resolution['height'] = self.frame_blank.winfo_height()
        
    def _frame2_change_resolution(self, event)->None:
        self.frame2_resolution['width'] = self.frame2.winfo_height()
        self.frame2_resolution['height'] = self.frame2.winfo_width()
        
    def _frame3_change_resolution(self, event)->None:
        self.frame3_resolution['width'] = self.frame3.winfo_height()
        self.frame3_resolution['height'] = self.frame3.winfo_width()
        
    def _root_exec(self)->None:
        self.resolution = {'width': 512, 'height': 512}
        self._ROOT = tkinter.Tk()
        self._ROOT.configure(background='white', 
                width=self.resolution['width'], height=self.resolution['height'])
        self._ROOT.bind('<Configure>', self._change_resolution)
        self._ROOT.rowconfigure(0, weight = 1)
        self._ROOT.rowconfigure(1, weight = 1)
        self._ROOT.rowconfigure(2, weight = 1)
        self._ROOT.rowconfigure(3, weight = 1)
        self._ROOT.columnconfigure(0, weight = 1)
        
    def _frame_exec(self)->None:
        self.frame = tkinter.Frame(self._ROOT, 
                    width = self.frame1_resolution['width'], height = self.frame1_resolution['height'],
                    background = FileCopyBackupGUI.BACKGROUND)
        self.frame.grid(row=0, column=0, padx=0, pady=0, sticky=tkinter.NSEW)
        self.frame.bind('<Configure>', self._frame1_change_resolution)
        
        self.frame.rowconfigure(0, weight = 1)
        self.frame.rowconfigure(1, weight = 3)
        self.frame.rowconfigure(2, weight = 1)
        self.frame.rowconfigure(3, weight = 3)
        self.frame.rowconfigure(4, weight = 1)
        self.frame.rowconfigure(5, weight = 3)
        self.frame.columnconfigure(0, weight = 25)
        self.frame.columnconfigure(1, weight = 5)
        self.frame.columnconfigure(2, weight = 10)
        
    def _frame_blank_exec(self)->None:
        self.frame_blank = tkinter.Frame(self._ROOT, 
                    width = self.frame_blank_resolution['width'], height = self.frame_blank_resolution['height'],
                    background = FileCopyBackupGUI.BACKGROUND)
        self.frame_blank.grid(row=1, column=0, padx=0, pady=0, sticky=tkinter.NSEW)
        self.frame_blank.bind('<Configure>', self._frame_blank_change_resolution)
        
    def _frame_exec2(self) -> None:
        self.frame2 = tkinter.Frame(self._ROOT, 
                    width = self.frame2_resolution['width'], height = self.frame2_resolution['height'],
                    background = FileCopyBackupGUI.BACKGROUND)
        self.frame2.grid(row=2, column=0, padx=0, pady=0, sticky=tkinter.NSEW)
        self.frame2.bind('<Configure>', self._frame2_change_resolution)
        
        self.frame2.rowconfigure(0, weight = 1)
        self.frame2.columnconfigure(0, weight = 1)
        self.frame2.columnconfigure(1, weight = 1)
        self.frame2.columnconfigure(2, weight = 1)
        self.frame2.columnconfigure(3, weight = 1)
        
    def _frame_exec3(self) -> None:
        self.frame3 = tkinter.Frame(self._ROOT, 
                    width = self.frame3_resolution['width'], height = self.frame3_resolution['height'],
                    background = FileCopyBackupGUI.BACKGROUND)
        self.frame3.grid(row=3, column=0, padx=0, pady=0, sticky=tkinter.NSEW)
        self.frame3.bind('<Configure>', self._frame3_change_resolution)
        
        self.frame3.rowconfigure(0, weight = 1)
        self.frame3.columnconfigure(0, weight = 1)
        
    def _frame_objects1(self)->None:
        default_font = 'Lucida', 14
        str_tar_dest = "Target Destination"
        str_save_dest = "Save Destination"
        str_save_dest2 = "Save Destination 2"
        folder_image = PIL.ImageTk.PhotoImage(file="folder.gif")
        
        def modifybyentry_target(strvar):
            self.FileCopyBackup.destination['target'] = strvar.get()
            
        def modifybyentry_save(strvar):
            self.FileCopyBackup.destination['save'] = strvar.get()
        
        def modifybyentry_save2(strvar):
            self.FileCopyBackup.destination['save2'] = strvar.get()
        
        label_tar_dest = tkinter.Label(self.frame, text=str_tar_dest, 
                        font = default_font, justify = tkinter.LEFT,
                        width = len(str_tar_dest), height = 1, bg=FileCopyBackupGUI.BACKGROUND)
        label_tar_dest.grid(row=0, column=0, padx=0, pady=0, sticky=tkinter.NSEW)
        
        str_tar_dest = tkinter.StringVar()
        str_tar_dest.trace("w", lambda name, index, mode, str_tar_dest=str_tar_dest: modifybyentry_target(str_tar_dest))
        self.entry_tar_dest = tkinter.Entry(self.frame, width = 50, textvariable = str_tar_dest)
        self.entry_tar_dest.grid(row=1, column=0, padx=10, pady=5, sticky=tkinter.E + tkinter.W + tkinter.N)
        self.entry_tar_dest.insert(0, self.FileCopyBackup.destination['target'])
        
        button_tar_dest = tkinter.Button(self.frame, image=folder_image, justify=tkinter.LEFT, command=self._command_tar_destination) 
        button_tar_dest.image = folder_image
        button_tar_dest.grid(row=1, column=1, padx=1, pady=0, sticky=tkinter.E  + tkinter.N)
        
        label_save_dest = tkinter.Label(self.frame, text=str_save_dest, 
                        font = default_font, justify = tkinter.LEFT,
                        width = len(str_save_dest), height = 1, bg=FileCopyBackupGUI.BACKGROUND)
        label_save_dest.grid(row=2, column=0, padx=0, pady=0, sticky=tkinter.NSEW)
        
        str_save_dest = tkinter.StringVar()
        str_save_dest.trace("w", lambda name, index, mode, str_save_dest=str_save_dest: modifybyentry_save(str_save_dest))
        self.entry_save_dest = tkinter.Entry(self.frame, width = 50, textvariable = str_save_dest)
        self.entry_save_dest.grid(row=3, column=0, padx=10, pady=5, sticky=tkinter.E + tkinter.W + tkinter.N)
        self.entry_save_dest.insert(0, self.FileCopyBackup.destination['save'])
        
        button_save_dest = tkinter.Button(self.frame, image=folder_image, justify=tkinter.LEFT, command=self._command_save_destination)
        button_save_dest.image = folder_image
        button_save_dest.grid(row=3, column=1, padx=1, pady=0, sticky=tkinter.E + tkinter.N)
        
        button_save_backup = tkinter.Button(self.frame, text="BACKUP", justify=tkinter.LEFT, command=self.backup) 
        button_save_backup.grid(row=3, column=2, padx=10, pady=0, sticky=tkinter.E + tkinter.N)
        
        label_save_dest2 = tkinter.Label(self.frame, text=str_save_dest2, 
                        font = default_font, justify = tkinter.LEFT,
                        width = len(str_save_dest2), height = 1, bg=FileCopyBackupGUI.BACKGROUND)
        label_save_dest2.grid(row=4, column=0, padx=0, pady=0, sticky=tkinter.NSEW)
        
        str_save_dest2 = tkinter.StringVar()
        str_save_dest2.trace("w", lambda name, index, mode, str_save_dest2=str_save_dest2: modifybyentry_save2(str_save_dest2))
        self.entry_save_dest2 = tkinter.Entry(self.frame, width = 50, textvariable = str_save_dest2)
        self.entry_save_dest2.grid(row=5, column=0, padx=10, pady=5, sticky=tkinter.E + tkinter.W + tkinter.N)
        self.entry_save_dest2.insert(0, self.FileCopyBackup.destination['save2'])
        
        button_save_dest2 = tkinter.Button(self.frame, image=folder_image, justify=tkinter.LEFT, command=self._command_save_destination2)
        button_save_dest2.image = folder_image
        button_save_dest2.grid(row=5, column=1, padx=1, pady=0, sticky=tkinter.E  + tkinter.N)
        
        button_save_backup2 = tkinter.Button(self.frame, text="BACKUP", justify=tkinter.LEFT, command=self.backup2)
        button_save_backup2.grid(row=5, column=2, padx=10, pady=0, sticky=tkinter.E + tkinter.N)
        
    def _frame_objects2(self)->None:
        str_option = "OPTION"
        str_makedefault = "SAVE TO\nDEFAULT"
        str_loadset = "LOAD\nSET"
        str_saveset = "SAVE\nSET"
        
        button_option = tkinter.Button(self.frame2, text=str_option, command=self.option,
                                       width = 4, height = 4)
        button_option.grid(row=0, column=0, padx=5, pady=5, sticky=tkinter.S + tkinter.W + tkinter.E)
        
        button_makedefault = tkinter.Button(self.frame2, text=str_makedefault, command=self.makedefault,
                                       width = 4, height = 4)
        button_makedefault.grid(row=0, column=1, padx=5, pady=5, sticky=tkinter.S + tkinter.W + tkinter.E)
        
        button_loadset = tkinter.Button(self.frame2, text=str_loadset, command=self.loadset,
                                       width = 4, height = 4)
        button_loadset.grid(row=0, column=2, padx=5, pady=5, sticky=tkinter.S + tkinter.W + tkinter.E)
        
        button_saveset = tkinter.Button(self.frame2, text=str_saveset, command=self.saveset,
                                       width = 4, height = 4)
        button_saveset.grid(row=0, column=3, padx=5, pady=5, sticky=tkinter.S + tkinter.W + tkinter.E)
        
    def _frame_objects3(self)->None:
        str_quit = "QUIT"
        
        button_quit = tkinter.Button(self.frame3, text=str_quit, command=self.quit,
                                       width = 20, height = 4)
        button_quit.grid(row=0, column=0, padx=5, pady=5, sticky=tkinter.S)
        
        #=======================================================================
        # COMMANDS
        #=======================================================================
    def _command_tar_destination(self):
        ''' Command to browse for path of filename to copy '''
        dialog = tkinter.filedialog.askopenfilename()
        if dialog != '':
            self.entry_tar_dest.delete(0, tkinter.END)
            self.entry_tar_dest.insert(0, dialog)
            self.FileCopyBackup.destination['target'] = dialog
    
    def _command_save_destination(self):
        ''' Command to browse for path of filename to save '''
        dialog = tkinter.filedialog.askdirectory()
        if dialog != '':
            self.entry_save_dest.delete(0, tkinter.END)
            self.entry_save_dest.insert(0, dialog)
            self.FileCopyBackup.destination['save'] = dialog
    
    def _command_save_destination2(self):
        ''' Command to browse for path of filename to save '''
        dialog = tkinter.filedialog.askdirectory()
        if dialog != '':
            self.entry_save_dest2.delete(0, tkinter.END)
            self.entry_save_dest2.insert(0, dialog)
            self.FileCopyBackup.destination['save2'] = dialog
            
        #=======================================================================
        # SAVE INITIALIZATION
        #=======================================================================
    def _exec_default(self) -> None:
        '''
        - Check whether whether parameters dest1_save_on_start and dest2_save_on_start are
        0 or 1.
        - If values are 1, then save destination will be called.
        - If values are 0, then nothing happens.
        - If save destination is called and fails, errors are ignored.
        '''
        if self.FileCopyBackup.Parameters["dest1_save_on_start"] == 1:
            try:
                self.FileCopyBackup.save_destination(1)
            except:
                print("Destination 1 save on start have failed.") #debug
                
        if self.FileCopyBackup.Parameters["dest2_save_on_start"] == 1:
            try:
                self.FileCopyBackup.save_destination(2)
            except:
                print("Destination 2 save on start have failed.") #debug
