'''
Created on Dec 21, 2014

@author: Ben
'''
import tkinter
import file_copy_backup

class Option(object):
    '''
    Option Menu for File Copy Backup
    '''
    BACKGROUND = '#f4f4f4'


    def __init__(self, param: file_copy_backup.FileCopyBackup):
        '''
        Constructor
        '''
        self.FileCopyBackup = param
        
        self._ROOT = tkinter.Toplevel(bg=Option.BACKGROUND)
        self._ROOT.rowconfigure(0, weight = 1)
        self._ROOT.rowconfigure(1, weight = 1)
        self._ROOT.rowconfigure(2, weight = 1)
        self._ROOT.rowconfigure(3, weight = 1)
        self._ROOT.rowconfigure(4, weight = 1)
        self._ROOT.columnconfigure(0, weight = 1)
        self._ROOT.resizable(0,0)
        self._ROOT.grab_set()

        self.frame1_resolution = {'width': 320, 'height': 320 * 3/20}
        self.frame1 = None
        
        self.frame_empty_resolution = {'width': 320, 'height': 320 * 1/20}
        self.frame_empty = None

        self.frame2_resolution = {'width': 320, 'height': 320 * 14/20}
        self.frame2 = None
        
        self.frame_empty_resolution2 = {'width': 320, 'height': 320 * 1/20}
        self.frame_empty2 = None

        self.frame3_resolution = {'width': 320, 'height': 320 * 1/20}
        self.frame3 = None

        self._frame1_exec()
        self._frame_empty_exec()
        self._frame2_exec()
        self._frame_empty2_exec()
        self._frame3_exec()
        
        self._frame_objects1()
        self._frame_objects2()
        self._frame_objects3()

    #===========================================================================
    # DISPLAY
    #===========================================================================
    def _frame1_exec(self)->None:
        self.frame1 = tkinter.Frame(self._ROOT, 
                    width = self.frame1_resolution['width'], height = self.frame1_resolution['height'],
                    background = Option.BACKGROUND)
        self.frame1.grid(row=0, column=0, padx=0, pady=0)

        self.frame1.columnconfigure(0, weight = 1)
        self.frame1.rowconfigure(0, weight = 1)
        self.frame1.rowconfigure(1, weight = 1)
        
    def _frame_empty_exec(self)->None:
        self.frame_empty = tkinter.Frame(self._ROOT, 
                    width = self.frame_empty_resolution['width'], 
                    height = self.frame_empty_resolution['height'],
                    background = Option.BACKGROUND)
        self.frame_empty.grid(row=1, column=0, padx=0, pady=0)
        
        self.frame_empty.columnconfigure(0, weight = 1)
        self.frame_empty.rowconfigure(0, weight = 1)
        
    def _frame2_exec(self)->None:
        self.frame2 = tkinter.Frame(self._ROOT, 
                    width = self.frame2_resolution['width'], height = self.frame2_resolution['height'],
                    background = Option.BACKGROUND)
        self.frame2.grid(row=2, column=0, padx=0, pady=0)

        self.frame2.columnconfigure(0, weight = 1)
        self.frame2.columnconfigure(1, weight = 1)
        self.frame2.rowconfigure(0, weight = 1)
        self.frame2.rowconfigure(1, weight = 1)
        self.frame2.rowconfigure(2, weight = 1)
        
    def _frame_empty2_exec(self)->None:
        self.frame_empty = tkinter.Frame(self._ROOT, 
                    width = self.frame_empty_resolution['width'], 
                    height = self.frame_empty_resolution['height'],
                    background = Option.BACKGROUND)
        self.frame_empty.grid(row=3, column=0, padx=0, pady=0)
        
        self.frame_empty.columnconfigure(0, weight = 1)
        self.frame_empty.rowconfigure(0, weight = 1)

    def _frame3_exec(self)->None:
        self.frame3 = tkinter.Frame(self._ROOT, 
                    width = self.frame3_resolution['width'], height = self.frame3_resolution['height'],
                    background = Option.BACKGROUND)
        self.frame3.grid(row=4, column=0, padx=0, pady=0)

        self.frame3.columnconfigure(0, weight = 1)
        self.frame3.rowconfigure(0, weight = 1)
        
    def _frame_objects1(self) -> None:
        def set_dest1_startup():
            if self.FileCopyBackup.Parameters['dest1_save_on_start'] == 0:
                self.FileCopyBackup.Parameters['dest1_save_on_start'] = 1
                savedest1_button.select()
            elif self.FileCopyBackup.Parameters['dest1_save_on_start'] == 1:
                self.FileCopyBackup.Parameters['dest1_save_on_start'] = 0
                savedest1_button.deselect()
        
        def set_dest2_startup():
            if self.FileCopyBackup.Parameters['dest2_save_on_start'] == 0:
                self.FileCopyBackup.Parameters['dest2_save_on_start'] = 1
                savedest2_button.select()
            elif self.FileCopyBackup.Parameters['dest2_save_on_start'] == 1:
                self.FileCopyBackup.Parameters['dest2_save_on_start'] = 0
                savedest2_button.deselect()
        
        savedest1_button = tkinter.Checkbutton(self.frame1, text="Save Dest 1 on start", 
                         bg=Option.BACKGROUND, command=set_dest1_startup)
        savedest1_button.grid(row=0, column=0, padx=5, pady=2)
        if self.FileCopyBackup.Parameters["dest1_save_on_start"] == 1:
            savedest1_button.select() 
        else:
            savedest1_button.deselect()
        
        savedest2_button = tkinter.Checkbutton(self.frame1, text="Save Dest 2 on start", 
                         bg=Option.BACKGROUND, command=set_dest2_startup)
        savedest2_button.grid(row=1, column=0, padx=5, pady=2)
        if self.FileCopyBackup.Parameters["dest2_save_on_start"] == 1:
            savedest2_button.select() 
        else:
            savedest2_button.deselect()
        
    def _frame_objects2(self)->None:
        default_font = 'Lucida', 12
        label1_text = "Save Dest 1"
        label2_text = "Save Dest 2"
        
        dest1_label = tkinter.Label(self.frame2, text=label1_text, font=default_font, 
                        width=len(label1_text), height=1, bg=Option.BACKGROUND)
        dest1_label.grid(row=0, column=0, padx=5, pady=1)
        
        def dest1_options(event):
            if dest1_listbox.get(dest1_listbox.curselection()[0]) == "overwrite":
                dest1_cur_label.configure(text = "overwrite", width = len("overwrite"))
                self.FileCopyBackup.Parameters['save_dest1'] = 'overwrite'
            elif dest1_listbox.get(dest1_listbox.curselection()[0]) == "daily":
                dest1_cur_label.configure(text = "daily", width = len("daily"))
                self.FileCopyBackup.Parameters['save_dest1'] = 'daily'
            elif dest1_listbox.get(dest1_listbox.curselection()[0]) == "exact":
                dest1_cur_label.configure(text = "exact", width = len("exact"))
                self.FileCopyBackup.Parameters['save_dest1'] = 'exact'
        
        dest1_listbox = tkinter.Listbox(self.frame2, bd=1, height=4, selectmode=tkinter.SINGLE)
        dest1_listbox.grid(row=1, column=0, padx=5, pady=5)
        dest1_listbox.insert(1, "overwrite")
        dest1_listbox.insert(2, "daily")
        dest1_listbox.insert(3, "exact")
        dest1_listbox.bind("<<ListboxSelect>>", dest1_options)
        
        dest1_cur_label = tkinter.Label(self.frame2, text=self.FileCopyBackup.Parameters['save_dest1'],
                                        width=len(self.FileCopyBackup.Parameters['save_dest1']), 
                                        height=1, bg=Option.BACKGROUND)
        dest1_cur_label.grid(row=2, column=0, padx=5, pady=1)
        
        dest2_label = tkinter.Label(self.frame2, text=label2_text, font=default_font, 
                        width=len(label2_text), height=1, bg=Option.BACKGROUND)
        dest2_label.grid(row=0, column=1, padx=5, pady=1)
        
        def dest2_options(event):
            if dest2_listbox.get(dest2_listbox.curselection()[0]) == "overwrite":
                dest2_cur_label.configure(text = "overwrite", width = len("overwrite"))
                self.FileCopyBackup.Parameters['save_dest2'] = 'overwrite'
            elif dest2_listbox.get(dest2_listbox.curselection()[0]) == "daily":
                dest2_cur_label.configure(text = "daily", width = len("daily"))
                self.FileCopyBackup.Parameters['save_dest2'] = 'daily'
            elif dest2_listbox.get(dest2_listbox.curselection()[0]) == "exact":
                dest2_cur_label.configure(text = "exact", width = len("exact"))
                self.FileCopyBackup.Parameters['save_dest2'] = 'exact'
        
        dest2_listbox = tkinter.Listbox(self.frame2, bd=1, height=4, selectmode=tkinter.SINGLE)
        dest2_listbox.grid(row=1, column=1, padx=5, pady=5)
        dest2_listbox.insert(1, "overwrite")
        dest2_listbox.insert(2, "daily")
        dest2_listbox.insert(3, "exact")
        dest2_listbox.bind("<<ListboxSelect>>", dest2_options)
        
        dest2_cur_label = tkinter.Label(self.frame2, text=self.FileCopyBackup.Parameters['save_dest2'],
                                        width=len(self.FileCopyBackup.Parameters['save_dest2']),
                                        height=1, bg=Option.BACKGROUND)
        dest2_cur_label.grid(row=2, column=1, padx=5, pady=1)
        
    def _frame_objects3(self) -> None:
        button_ok = tkinter.Button(self.frame3, text="OK", command=self.quit,
                                   width = 8, height = 2)
        button_ok.grid(row=0, column=0, padx=5, pady=5)
        
    #===========================================================================
    # HELPER
    #===========================================================================        
    def quit(self):
        ''' Close option menu '''
        self._ROOT.destroy()
