from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from googletrans import Translator
from PIL import ImageTk,Image

root = Tk()
root.geometry('500x620')


background_image = ImageTk.PhotoImage(Image.open("D:\\bglang.jpeg"))
background_label = Label(root, image = background_image)
background_label.place(relwidth = 1, relheight =1)


root.title(" ONESTOP-TOOLKIT")
Label(root, text = "LANGUAGE TRANSLATOR", font = ('Lora',23,BOLD), bg='#55b8ed', foreground='#fff15e').place(x=48,y=30)
Input_text = Text(root,font = 'arial 10', height = 5, wrap = WORD, padx=5, pady=5, width = 50,bg="#accbe3")
Input_text.place(x=65,y = 160)
Output_text = Text(root,font = 'arial 10', height = 5, wrap = WORD, padx=5, pady= 5, width =50, bg="#accbe3")
Output_text.place(x = 65 ,y = 440)


LANGUAGES_LIST ={"Arabic","Bangla","Chinese","English","French","Gujarati", "Hindi","Italian","Japanese","Kannada","Korean","Malayalam","Marathi","Odia","Punjabi","Russian","Spanish","Telugu","Urdu"}
language = list(LANGUAGES_LIST)
src_lang = ttk.Combobox(root, values= language, width =22)
src_lang.place(x=170,y=120)
src_lang.set('choose input language')
dest_lang = ttk.Combobox(root, values= language, width =22)
dest_lang.place(x=170,y=400)
dest_lang.set('choose output language')


def Translate():
    translator = Translator()
    translated=translator.translate(text= Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)

trans_btn = Button(root, text = 'Translate',font = 'arial 12 bold',pady = 5,command = Translate , bg = '#c72c41',foreground="white", activebackground = 'sky blue')
trans_btn.place(x = 200, y= 310 )
root.mainloop()