from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import os
import binascii
window = Tk()

window.title("Fix Better Hi3 Launcher")
lbl = Label(window, text="Server:")
lbl.grid(column=0,row=0)
combo = Combobox(window)

combo['values']= ('SEA','Global') #select server
combo.current(1) #set the selected item

combo.grid(column=1, row=0)
lbl2 = Label(window, text="Games folder")
lbl2.grid(column=0,row=1)
def browseFiles():
    global currentdir
    if os.path.isdir('C:\Program Files\Honkai Impact 3rd'):
        filename = filedialog.askdirectory(initialdir = "C:\Program Files\Honkai Impact 3rd\Games",
                                          title = "Select a File")
        
        currentdir = filename
        rint(currentdir)
    else:
        if os.path.isdir('C:\Program Files\Honkai Impact 3'):
            filename = filedialog.askdirectory(initialdir = "C:\Program Files\Honkai Impact 3\Games",
                                          title = "Select a File")
            
            currentdir = filename
            print(currentdir)
        else:
           filename = filedialog.askdirectory(initialdir = "/", title = "Select a File")
           
           currentdir = filename
           print(currentdir)

def makeFile():
    #print('test')
    print(currentdir)
    if combo.get() == 'SEA':
        f=open("betterhi3fix.reg","w")
        f.write('Windows Registry Editor Version 5.00\n\n[HKEY_CURRENT_USER\SOFTWARE\Bp\Better HI3 Launcher]\n"VersionInfoSEA"=hex:7b,22,67,61,6d,65,5f,69,6e,66,6f,22,3a,7b,22,76,65,72,73,\\\n69,6f,6e,22,3a,22,34,2e,36,2e,30,5f,35,65,34,32,33,36,35,61,30,64,62,22,2c,\\\n22,69,6e,73,74,61,6c,6c,5f,70,61,74,68,22,3a,22,' + binascii.hexlify(str.encode(currentdir.replace('/','\\\\')), ',').decode('utf-8')+',22,7d,7d')
        f.close()
    if combo.get() == 'Global':
        f=open("betterhi3fix.reg","w")
        f.write('Windows Registry Editor Version 5.00\n\n[HKEY_CURRENT_USER\SOFTWARE\Bp\Better HI3 Launcher]\n"VersionInfoGlobal"=hex:7b,22,67,61,6d,65,5f,69,6e,66,6f,22,3a,7b,22,76,65,72,73,\\\n69,6f,6e,22,3a,22,34,2e,36,2e,30,5f,35,65,34,32,33,36,35,61,30,64,62,22,2c,\\\n22,69,6e,73,74,61,6c,6c,5f,70,61,74,68,22,3a,22,' + binascii.hexlify(str.encode(currentdir.replace('/','\\\\')), ',').decode('utf-8')+',22,7d,7d')
        f.close()
    
button_explore = Button(window, 
                        text = "Browse Files",
                        command = browseFiles)
button_explore.grid(column = 1, row = 1)
btn_reg = Button(window, text="Make .reg file", command = makeFile)
btn_reg.grid(column=2,row=2)
window.mainloop()
