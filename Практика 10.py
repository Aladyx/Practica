from tkinter import *
from tkinter import ttk 
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import filedialog




#Функции для чекбокса
def clicked1():
    messagebox.showinfo('Внимание', 'Вы выбрали первый вариант')
def clicked2():
    messagebox.showinfo('Внимание', 'Вы выбрали второй вариант')
def clicked3():
    messagebox.showinfo('Внимание', 'Вы выбрали третий вариант')
    
    


#Для калькулятора
def calkyl():
    a = txt.get()
    b = txt2.get()
    res = 0
    c = combo.get()
    if c == '+':
        res = float(a) + float(b)
    if c == '-':
        res = float(a) - float(b)
    if c == '*':
        res = float(a) * float(b)
    if c == '/':
        res = float(a) // float(b)
    lbl['text'] = res
    
    

#Для работы с текстом      
def select_file():
    file = filedialog.askopenfile(filetypes= (('text files', '*.txt'),('All files', '*.*')))
    textfile.insert('1.0', file.readlines())    



  
window = Tk()
window.geometry('800x600')
window.title('Буриков Никита Михайлович')




#Вкладка Калькулятора
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text = 'Калькулятор')
tab_control.pack(expand=1, fill = 'both')

txt = Entry(tab1, width=10)
txt.grid(column=0, row=0)

combo = Combobox(tab1)
combo.grid(column = 2, row = 0)
combo['values'] = ('+' , '-', '*', '/' )

txt2 = Entry(tab1, width=10)
txt2.grid(column=5, row=0)

btncal = Button(tab1, text='=', command=calkyl)
btncal.grid(column=6, row = 0)
lbl= Label(tab1, text='')
lbl.grid(column=7, row=0)



#Вкладка чекбокса
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text = 'Чекбоксы')
tab_control.pack(expand=1, fill = 'both')

btn = Button(tab2, text='Первый', command=clicked1)
btn.grid(column=0, row=0) 
btn2 = Button(tab2, text='Второй', command=clicked2)
btn2.grid(column=0, row=1) 
btn3 = Button(tab2, text='Третий', command=clicked3)
btn3.grid(column=0, row=2) 




#Вкладка работы с текстом
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text = 'Работа с текстом')
tab_control.pack(expand=1, fill = 'both')

textfile = Text(tab3, height = 15)
textfile.grid(column=0, row=0, sticky='nsew')


openfile = ttk.Button(tab3, text='Открыть файл', command= select_file)
openfile.grid(column=0, row=1)




window.mainloop()