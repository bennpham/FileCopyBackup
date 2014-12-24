FileCopyBackup
==============

Introduction
-------------
I was getting sick of certain files such as saved games that are constantly updated either getting lost or corrupted in the past. You can manually go to the folder of the save game and copy and paste it to another location each time, but I find it would be more convenient to have a program to do this entire task in a few clicks of a button. 

I decided to create this program with a few goals:
  •	A really simple interface
  •	2 backup folder destination options
    o	1 to back up the save file to another destination on my computer
    o	2 to back up the save file to a cloud service such as DropBox if I so desire
  •	The ability to save presets of what file you want to save and where to save them
  •	The ability to automatically back up files the moment the program start if the options is ticked

Tool: Main Window
-------------------
A window should pop up that looks like the one above. If you do not have a file called default.txt inside your FileCopyBackup folder, it will automatically be created for you. If you have this file inside your FileCopyBackup folder already, the program will read this document and will make its values (if it contains valid values) as its default launch parameters. 

Tool: Target Destination
-------------------------
The target destination box is where you type in the location of the directory with the filename of the item you want to backup. You can get the name/location in 2 ways.
  -	Type in the directory of the file with the name of the file at the end
  -	Click the folder button and browse for the file to save
Note:	You can just type in the name of the file if it is in the same folder as FileCopyBackup.exe 

Tool: Save Destination
----------------------- 
The save destination is where you type in the location of the directory that you want the file in your target destination to be copied to. You can get the directory in 2 ways.
  -	Type in the directory of the file with the name of the file at the end
  -	Click the folder button and browse for the file to save
When you click the BACKUP button, the action will be initialized and your targeted file will be copied. The 1st backup button will copy to the 1st Save Destination and the 2nd button will copy to the 2nd Save Destination. You can also use the backup button found in the Action dropdown menu by File and Help.

Notes:  
-	 If you do not specify a path and input a name of a folder you want to name your backup folder instead, the folder will be created in the folder that contains your FileCopyBackup.exe instead.
-	If you get the File cannot be found error, when you backup, your backup folders will be created anyways, but it will be empty.
-	If a directory doesn’t exist, it will be created
-	The backups will be made based on the settings you have set in your options (they will be cover in the OPTIONS section)
  o	Backup #1 Default = Exact
  o	Backup #2 Default = Overwrite
-	There are rare cases that an unknown error will occur. One of them is entering a name for a directory using invalid symbols

Tool: Option
--------------
You can select option by either clicking the big OPTION button or go to File  Option. You should have the little box that looks like the one above appear. 

Save Destination on Start
--------------------------- 
-	If the boxes are checked, either Backup #1 or Backup #2 will attempt to backup your targeted file if it can. There will be no popup to indicate, but if there are any failures during the backup process, nothing happens or a new folder will be created but it is empty.
-	You must click SAVE TO DEFAULT if you want this option to occur. 

Save Destination Selection Box
------------------------------- 
-	Select the save option for either Save Destination 1 or 2
  o	Overwrite
    	Copy file to save destination. Overwrite file if it already exists.
  o	Daily
    	Creates a new folder with today’s date in save destination
    	Copy file to new folder (overwrite file if the day is still today)
  o	Exact
    	Creates a new folder with today’s date in save destination
    	Create a new folder with exact time
    	Copy file to folder with exact time

Tool: Save to Default
---------------------- 
This button saves your current settings including any settings you set in OPTION and anything you inputted in TARGET DESTINATION, SAVE DESTINATION, and SAVE DESTINATION 2 to your default.txt file.
Because the program reads from default.txt before it starts, the program will start with the same settings you previously had since the last time you click SAVE TO DEFAULT.
Note: You can change your default.txt file manually to change startup parameters. I would only recommend this to advance users only. If you put invalid parameters, the program will start up with any valid parameters it can find, but it will give you a warning message (see below).

Tool: Load Set & Save Set
-------------------------- 
Besides SAVE TO DEFAULT, you can also use SAVE SET to save your current settings to a separate text file in the same format as default.txt file.
LOAD SET allows you to load parameters from another text file into the program and it will change each setting for each valid parameters.
Note: 
-	You can load a text file with random texts but it will still load as long as there is a valid parameter inside.
-	If a parameter contains invalid values, a warning will appear (see below) and none of your settings will be changed

Editing Default.txt & Making Your Own Sets Manually
------------------------------------------------------ 
This is the standard layout of the default.txt file. You can manually edit it if you want. You can add in any spam text (slowing the program down) as long as it still contains the following parameters, it will load. The parameters can appear in any order. It is best that you don’t add thousands of lines of spam texts or else you will slow the program down as it tries to read all of the lines although this haven’t been tested nor would it be too significant. 
You can also create your own text files to load via LOAD SET based on these parameters. LOAD SET and starting the program for default.txt will take any values for the following:
-	TARGET DESTINATION
-	SAVE DESTINATION
-	SAVE DESTINATION2
-	SAVE TYPE DEST1
-	SAVE TYPE DEST2
If SAVE STARTUP DESTs are not integers, you will get the invalid parameter warnings as you have seen above in the SAVE TO DEFAULT and LOAD & SAVE SET sections.

Unknown Errors
-------------- 
One known way to cause this error is to type in invalid characters such as “*” in the SAVE DESTINATION boxes then hitting back up since directories are not allowed to have invalid characters.
If for any reason you receive this error from a task other than typing in invalid characters for SAVE DESTINATION directories, please report them to me.
