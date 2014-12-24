'''
Created on Dec 20, 2014

@author: Ben
'''
import file_copy_backup_gui, file_copy_backup



if __name__ == '__main__':
    MAINPROGRAM = file_copy_backup.FileCopyBackup()
    GUI = file_copy_backup_gui.FileCopyBackupGUI(MAINPROGRAM)
