# ---------PIX.HUNTER-------2021
#
#
#
import ctypes
import tkinter as tk
from tkinter import *
from tkinter import font

from pynput import mouse

#Need it to size pixel
import os
import sys
from PyQt5.QtWidgets import QApplication

def schet_run( ):
    global scale_way
    global scale_scroll_way
    global M_s_run
    global x0
    global y0
    global k,ks
    global count_click
    global il 
    
    
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)
    
    scale_way=0
    obnul_=1
    pk=0
    M_s_run=0
    count_click=0
    count_click_l=0
    count_click_r=0
    k=0
    ks=0
    time_not_work= 0
    time_not_workm=0
    scroll_roll=0
    
    
    app = QApplication(sys.argv)
    screen = app.screens()[0]
    dpi = screen.physicalDotsPerInch()
    
    koeff=dpi/screensize[0] *  0.393701   #size of pixel

    if not doTick:
        return
        
    while (doTick):
        with mouse.Events() as events:

            event = events.get(1.0)
            if event is None:
            # lets count time procrastination
                time_not_work=time_not_work+1
                window.update()
                if (time_not_work<60):
                    lbl_value_t['text'] = str(time_not_work) + ' sec'
                elif (time_not_work<3600):
                    lbl_value_t['text'] = str(int(time_not_work/60)) + ' min ' + str(time_not_work - (int(time_not_work/60))*60) + ' sec'
                elif (time_not_work<86400):
                    lbl_value_t['text'] = str(int(time_not_work/3600)) + ' hours ' + str((int(time_not_work/60))-(int(time_not_work/3600))*60) + ' min ' + str(time_not_work - (int(time_not_work/60))*60) + ' sec'
                else:
                    lbl_value_t['text'] = str(int(time_not_work/86400)) + ' days ' +str(-(int(time_not_work/86400)*24) + int(time_not_work/3600)) + ' hours ' + str((int(time_not_work/60))-(int(time_not_work/3600))*60) + ' min ' + str(time_not_work - (int(time_not_work/60))*60) + ' sec'

                
                if (time_not_workm <= time_not_work): #time p record
                    time_not_workm=time_not_work
                    if (time_not_workm<60):
                        lbl_value_tm['text'] = str(time_not_workm) + ' sec'
                    elif (time_not_workm<3600):
                        lbl_value_tm['text'] = str(int(time_not_workm/60)) + ' min ' + str(time_not_workm - (int(time_not_workm/60))*60) + ' sec'
                    elif (time_not_workm<86400):
                        lbl_value_tm['text'] = str(int(time_not_workm/3600)) + ' hours ' + str((int(time_not_workm/60))-(int(time_not_workm/3600))*60) + ' min ' + str(time_not_workm - (int(time_not_workm/60))*60) + ' sec'
                    else:
                        lbl_value_tm['text'] = str(int(time_not_work/86400)) + ' days ' +str(-(int(time_not_work/86400)*24) + int(time_not_work/3600)) + ' hours ' + str((int(time_not_work/60))-(int(time_not_work/3600))*60) + ' min ' + str(time_not_work - (int(time_not_work/60))*60) + ' sec'
                window.update()
            else:
                time_not_work=0
                window.update()
                lbl_value_t['text'] = ' 0'
                window.update()
                 
                if (il==5):
                    
                    scale_way=0
                    obnul_=1
                    pk=0
                    M_s_run=0
                    count_click=0
                    count_click_l=0
                    count_click_r=0
                    k=0
                    time_not_work= 0
                    time_not_workm=0
                    scroll_roll=0
                    M_x=0
                    M_y=0
                    x0=0
                    y0=0
                    mem=0

                    #start values
                    lbl_value['text'] = '0 cm'
                    lbl_value_s['text'] = '0 cm'
                    lbl_value_c['text'] = '0'
                    lbl_value_cl['text'] = '0'
                    lbl_value_cr['text'] = '0'
                    window.update()
                    k=0
                     
                    il=6
                   
                s= format(event)
                if 'Move' in s:
                #count moving distance
                    s1=s.find(',')
                    
                    M_x=int(s[7:s1:])
                    M_y=int(s[s1+4:(len(s)-1):])
                    if (x0==0):
                        mem=0
                    else:
                        mem=round(pow((pow((M_x-x0),2) + pow((M_y-y0),2)).real,0.5),4)
                     
                    if (M_s_run==0):
                        M_s_run=(mem)*koeff
                    else:
                        if (k==0):
                            M_s_run=M_s_run + (mem)*koeff
                        elif (k==1):
                            M_s_run=M_s_run + (mem)*koeff/100
                        elif (k==2):
                            M_s_run=M_s_run + (mem)*koeff/100000
                            
                            
                    if ((M_s_run < 100) & (k==0)):
                        window.update()
                        lbl_value['text'] = str(round(M_s_run,2)) + ' cm'
                        window.update()
                        

                    elif (((M_s_run >= 100) & (M_s_run < 1000)) & (k==0)):     
                        window.update()
                        M_s_run=M_s_run/100
                        lbl_value['text'] = str(round(M_s_run,2)) + ' m'
                        window.update()
                        k=1
                        
                    elif ((M_s_run < 1000) & (k==1)):
                        window.update()
                        lbl_value['text'] = str(round(M_s_run,2)) + ' m'
                        window.update()

                    elif (((M_s_run >= 1000)) & (k==1)):     
                        window.update()
                        M_s_run=M_s_run/1000
                        lbl_value['text'] = str(round(M_s_run,2)) + ' km'
                        window.update()
                        k=2
                        
                    elif ( (k==2)):
                        window.update()
                        lbl_value['text'] = str(round(M_s_run,2)) + ' km'
                        window.update()

                        
                    x0=M_x
                    y0=M_y
                    
                if 'Click' in s:
                #count clicks
                    
                    s1=s.find('.')
                    C_click=s[s1+1:(len(s)-16):]
 
                    count_click=count_click+1
 
                    if 'ri' in C_click:
                        count_click_r +=1
                    elif 'le' in C_click:
                        count_click_l +=1
                        
                    lbl_value_c['text'] = str(int(count_click/2))  
                    lbl_value_cl['text'] = str(int(count_click_l/2)) 
                    lbl_value_cr['text'] = str(int(count_click_r/2)) 
                    window.update()

                    
                if 'Scroll' in s:
                #count scrolling distance
                    scroll_roll=(scroll_roll+1)

                    if ((scroll_roll*0.5 < 100) & (ks==0)):
                        window.update()
                        lbl_value_s['text'] = str(round(scroll_roll*0.5,2)) + ' cm'
                        window.update()
                        

                    elif (((scroll_roll*0.5 >= 100) & (M_s_run < 1000)) & (ks==0)):     
                        window.update()
                        scroll_roll=scroll_roll/100
                        lbl_value_s['text'] = str(round((scroll_roll)*0.5,2)) + ' m'
                        window.update()
                        ks=1
                        
                    elif ((scroll_roll*0.5 < 1000) & (ks==1)):
                        window.update()
                        lbl_value_s['text'] = str(round(scroll_roll*0.005,2)) + ' m'
                        window.update()

                    elif (((scroll_roll*0.5 >= 1000)) & (ks==1)):     
                        window.update()
                        scroll_roll=scroll_roll/1000
                        lbl_value_s['text'] = str(round(scroll_roll,2)) + ' km'
                        window.update()
                        ks=2
                        
                    elif ( (ks==2)):
                        window.update()
                        lbl_value_s['text'] = str(round(scroll_roll*0.5,2)) + ' km'
                        window.update()
                        
                    window.update()

   
def stop():
    global doTick
    doTick = False

def start():
    global doTick
    doTick = True
    schet_run()
    
def obnulenie():
    global doTick
    global obnul_
    global M_s_run
    global x0
    global y0
    global k,ks
    global count_click
    global il
    
    lbl_value['text'] = '0 cm'
    lbl_value_s['text'] = '0 cm'
    lbl_value_c['text'] = '0'
    lbl_value_cl['text'] = '0'
    lbl_value_cr['text'] = '0'
    window.update()
    obnul_=0
    x0=0
    y0=0
    M_s_run=0
    count_click=0
    doTick = True
    il=5
    k=0
    ks=0
    
    
def user_name_re():
    window.update()
    lbl_0['text']='\nYour mouse statistics, \n' + str(os.environ.get( "USERNAME" )) + '\n'
  
#-------------------------------------------------------------------------------------------------------
#          ENTER
#-------------------------------------------------------------------------------------------------------
# ---------PIX.HUNTER-------2021

window = Tk()
#window.eval('tk::PlaceWindow . center')
x00 = (window.winfo_screenwidth() - 2*window.winfo_reqwidth()) / 3
y00 = (window.winfo_screenheight() - 2*window.winfo_reqheight()) / 3

window.wm_geometry("+%d+%d" % (x00, y00))

courier_18 = font.Font(family="Arial", size=18, weight=font.BOLD, slant="italic")
courier_16 = font.Font(family="Helvetica", size=12, slant="italic")
courier_10 = font.Font(family="Helvetica", size=14, weight=font.BOLD)
courier_1 = font.Font(family="Helvetica", size=11, weight=font.BOLD)
x0=0
y0=0
M_s_run=0
il=5

window.title("Мышовая статистика")  
window.geometry('420x560')
window.configure(background="black")
window.resizable(False, False)

os.environ.get( "USERNAME" ) #i need your name ^___^

lbl_0 = tk.Label(master=window, text="\n0",background="black", fg='#ff086b', font=courier_18)
lbl_0.grid(row=0, column=1, columnspan=6)
user_name_re()

lbl_1_0 = tk.Label(master=window, background="black",text="       ").grid(row=0, column=0, sticky="W", padx=0, rowspan=25)

lbl_1_0 = tk.Label(master=window,  background="black",text="Distances:", fg='lime', font=courier_10).grid(row=1, column=1, sticky="W", padx=0, columnspan=3)
lbl_2_0 = tk.Label(master=window, background="black",text="    - cursor movement:", fg='white', font=courier_16).grid(row=2, column=1, sticky="W", padx=0, columnspan=3)
lbl_3_0 = tk.Label(master=window, background="black",text="    - scroll wheel:\n", fg='white', font=courier_16).grid(row=3, column=1, sticky="W", padx=0, columnspan=3)
lbl_4_0 = tk.Label(master=window, background="black",text="Mouse clicks:", fg='#ffb121', font=courier_10).grid(row=4, column=1, sticky="W", padx=0, columnspan=3)
lbl_4_0 = tk.Label(master=window, background="black",text="    - left:", fg='white', font=courier_16).grid(row=5, column=1, sticky="W", padx=0, columnspan=3)
lbl_4_0 = tk.Label(master=window, background="black",text="    - right:", fg='white', font=courier_16).grid(row=6, column=1, sticky="W", padx=0, columnspan=3)
lbl_4_0 = tk.Label(master=window, background="black",text="    - all:\n", fg='#f74040', font=courier_16).grid(row=7, column=1, sticky="W", padx=0, columnspan=3)
lbl_4_0 = tk.Label(master=window, background="black",text="Idle time:", fg='deepskyblue', font=courier_10).grid(row=9, column=1, sticky="W", padx=0, columnspan=3)
lbl_4_0 = tk.Label(master=window, background="black",text="Best idle time:", fg='magenta', font=courier_10).grid(row=10, column=1, sticky="W", pady=0, columnspan=3)

lbl_4_0 = tk.Label(master=window, background="black", fg='white', font=courier_16,text="\n\n------------------------PIX.HUNTER-------------------------\n\n").grid(row=21, column=1, padx=0, sticky="W", columnspan=5)



lbl_value = tk.Label(master=window, text="0" , background="black", fg='white', font=courier_16)
lbl_value.grid(row=2, column=3, columnspan=3, sticky="E")
lbl_value_s= tk.Label(master=window, text="0" , background="black", fg='white', font=courier_16)
lbl_value_s.grid(row=3, column=3, columnspan=3, sticky="E")

lbl_value_cl= tk.Label(master=window, text="0" , background="black", fg='white', font=courier_16)
lbl_value_cl.grid(row=5, column=3, columnspan=3, sticky="E")
lbl_value_cr= tk.Label(master=window, text="0" , background="black", fg='white', font=courier_16)
lbl_value_cr.grid(row=6, column=3, columnspan=3, sticky="E")
lbl_value_c= tk.Label(master=window, text="0" , background="black", fg='#f74040', font=courier_16)
lbl_value_c.grid(row=7, column=3, columnspan=3, sticky="E")
lbl_value_t= tk.Label(master=window, text="0" , background="black", fg='deepskyblue', font=courier_16)
lbl_value_t.grid(row=9, column=3, columnspan=3, sticky="E")
lbl_value_tm= tk.Label(master=window, text="0" , background="black", fg='magenta', font=courier_16)
lbl_value_tm.grid(row=10, column=3, columnspan=3, sticky="E")


btn2 = Button(text="Start", command=start, bg='#00ff00', fg='black', activebackground="magenta", font=courier_1, width=5).grid(row=25, column=2, sticky="nsew", padx=5, pady=5)
btn3 = Button(text="Revoke", command=obnulenie,  bg='#ff6200', fg='yellow', activebackground="yellow", font=courier_1, width=13).grid(row=25, column=3, sticky="nsew", padx=5, pady=5, columnspan=2)

btn4 = Button(text="Stop", command=stop, width=5, height=1,bg='#cc0000', fg='white', activebackground="cyan", font=courier_1).grid(row=25, column=5, sticky="nsew", padx=5, pady=5)


window.mainloop()


#░░░░░░░▐▀▄──────▄▀▌───▄▄▄▄▄▄▄
#░░░░░░░▌▒▒▀▄▄▄▄▀▒▒▐▄▀▀▒██▒██▒▀▀▄
#░░░░░░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄
#░░░░░░▌▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄
#░░░░░▀█▒▒█▌▒▒█▒▒▐█▒▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌
#░░░░░▀▌▒▒▒▒▒▀▒▀▒▒▒▒▒▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐ ▄▄
#░░░░░░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄█▒█
#░░░░░░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▀
#░░░░░░▐▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▌
#░░░░░░░▀▄▄▀▀▀▀▄▄▀▀▀▀▀▀▄▄▀▀▀▀▀▀▄▄
# ---------PIX.HUNTER-------2021
