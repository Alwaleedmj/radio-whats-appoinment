# -*- coding: utf-8 -*-sw
# modules for the bots
import csv
import pywhatkit 
import time
import pyautogui
import keyboard as k

# for GUI
import tkinter as tk 
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile




### The app
root = tk.Tk() # intializing the programer

canvas = tk.Canvas(root, width=600, height=300) # feature of app window, you add color and other features
canvas.grid(columnspan=3, rowspan=5) # the division

#logo

#instructions

instructions = tk.Label(root, text='رسائل واتساب  حجز المواعيد قسم الاشعة التشخيصية'
                            , font='Raleway') # Adding label and change it
instructions.grid(columnspan=3, column=1, row=1) # place of text (columnspan= width of the text)

# Whatsapp app
def Whatsapp(N, M):
    pywhatkit.sendwhatmsg_instantly(N, M, 4)
    time.sleep(10)
    pyautogui.click(875, 819)
    time.sleep(2)
    k.press_and_release('enter')  
    
    # sending the text message
    time.sleep(2)
    #----- From here start closing the tab for whatsapp
    #pyautogui.click(471, 29)
    #time.sleep(1)
    #pyautogui.click(1011, 395)
    #time.sleep(1)
    #---- End of closing tabd
    k.press_and_release('Ctrl+w')
# terminate function
def close_app():
    root.quit()

# function
def open_file():
    browse_text.set('يتم التحميل ...!')
    file = askopenfile(parent=root, mode='r', title='Choose a file', filetypes=[("CSV File", "*.csv")])
    if file:     
            patient= csv.reader(file)
            next(patient)
            
            sended = []
            count = 0

            text_box = tk.Text(root, height=50, width=100, padx=15, pady=15)
            text_box.grid(column=1,row=5)
            for line in patient:
                line[6] = '+966'+line[6][1:]
                count +=1  

                MRN = line[3][:-4]  
                
                if line[6] in sended:
                    print(f' Was sent {line[6]}  {line[1]}')
                    pass
                else:
                    if line[1] == 'CT':
                        MSG_CT = f"تم حجز موعدكم في قسم الاشعة بوحدة الاشعة المقطعية بمستشفى الملك فهد التخصصي ببريدة بتاريخ {line[9]} بتوقيت {line[10]}"+"\n\n"+f'رقم ملف: {MRN}'+"\n\n"+'🔄 لتأجيل الموعد إرسال ( تأجيل ).'+"\n\n"+'❌ لإلغاء الموعد إرسال ( إلغاء ).'+'\n\n'+'✉️- نأمل منكم الاطلاع على تحضيرات الفحص المرفقة لكم في رابط بالرسالة النصية.'+'\n\n'+'💉- للمراجعين فوق 50 سنه واصحاب الامراض المزمنة والخاضعين للعلاج الكيميائي يجب عمل تحليل وظائف الكلى خلال 10 ايام التي تسبق الموعد ومن دون التحليل لن يتم عمل الفحص.'+'\n\n'+'💉- يجب عمل تحليل حمل للمتزوجة اقل من 50 سنه خلال 10 ايام التي تسبق الموعد ومن دون التحليل لن يتم عمل الفحص.'+"\n\n"+'🔴-في حال تم تاجيل الموعد من قِبلكم نامل منكم تجاهل هذه الرسالة.'
                        content = str(count) + f' - تم الارسال الى {line[6],}  {line[1]}'
                        text_box.insert(1.0, content)
                        text_box.insert(1.0, '\n')
                        text_box.tag_configure('center', justify='center')
                        text_box.tag_add("center",1.0, "end")
                        Whatsapp(line[6], MSG_CT)
                        sended.append(line[6])
                    if line[1] == 'US':
                        MSG_US = f"تم حجز موعدكم في قسم الاشعة بوحدة الموجات فوق الصوتية بمستشفى الملك فهد التخصصي ببريدة بتاريخ {line[9]} بتوقيت {line[10]}"+"\n\n"+f'رقم ملف: {MRN}'+"\n\n"+ "🔄 لتأجيل الموعد إرسال ( تأجيل ). " + "\n\n" + '❌ لإلغاء الموعد إرسال ( إلغاء ) .' + '\n\n' + '☢️ التعليمات ☢️' + '\n' + '✉️- نأمل منكم الاطلاع على تحضيرات الفحص المرفقة لكم في رابط بالرسالة النصية.'+"\n\n"+'🔴-في حال تم تاجيل الموعد من قِبلكم نامل منكم تجاهل هذه الرسالة.'
                        content = str(count) + f' - تم الارسال الى {line[6],}  {line[1]}'
                        text_box.insert(1.0, content)
                        text_box.insert(1.0, '\n')
                        text_box.tag_configure('center', justify='center')
                        text_box.tag_add("center",1.0, "end")
                        Whatsapp(line[6], MSG_US)
                        sended.append(line[6])
                    if line[1] == "MR":
                        MSG_MR = f"تم حجز موعدكم في قسم الاشعة بوحدة الرنين المغناطيسي في العيادات الخارجية بمستشفى الملك فهد التخصصي ببريدة بتاريخ {line[9]} بتوقيت {line[10]}""\n\n"+f'رقم ملف: {MRN}'+"\n\n"+'❌ لإلغاء الموعد إرسال ( إلغاء )'+'\n\n'+'🕒-  الحضور قبل الموعد بـ 15 دقيقه'+'\n\n'+'☢️ التعليمات ☢️'+'\n'+'✉️- نأمل منكم الاطلاع على تحضيرات الفحص المرفقة لكم في رابط بالرسالة النصية.'+'\n'+'💉- يجب عمل تحليل وظائف الكلى خلال 10 ايام التي تسبق الفحص لفحوصات الرنين المغناطيسي مع الصبغه ومن دون التحليل لن يتم عمل الفحص.'+"\n\n"+'🔴-في حال تم تاجيل الموعد من قِبلكم نامل منكم تجاهل هذه الرسالة.'
                        content = str(count) + f' - تم الارسال الى {line[6],}  {line[1]}'
                        text_box.insert(1.0, content)
                        text_box.insert(1.0, '\n')
                        text_box.tag_configure('center', justify='center')
                        text_box.tag_add("center",1.0, "end")
                        Whatsapp(line[6], MSG_MR)
                        sended.append(line[6])
                        
                browse_text.set("يتم الارسال .. !")
#browse button
browse_text = tk.StringVar() #verified the txt
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(),# this adding the function
                        font='Raleway', bg='#20bebe', fg='black', 
                        height=2, width=15) # specification of text
browse_text.set('حمل ملف بصيغة CSV') # text of butting
browse_btn.grid(column=1, row=3) # the grid

# Quit button
quit_text = tk.StringVar() #verified the txt
quit_btn = tk.Button(root, textvariable=quit_text, command=lambda:close_app(),# this adding the function
                        font='Raleway', fg='black', 
                        height=2, width=15) # specification of text
quit_text.set('ايقاف البرنامج') # text of butting
quit_btn.grid(column=1, row=4) # the grid

# Exnted the app window
canvas = tk.Canvas(root, width=600, height=250) #  extend of the app window
canvas.grid(columnspan=5)


made = tk.Label(root, text='This app developed by Dr.Alwaleed Almajlad'
                            , font='Raleway', fg='red') # Adding label and change it
made.grid(columnspan=3, column=1, row=2)


root.mainloop()
