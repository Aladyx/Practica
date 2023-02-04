from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.ttk import Combobox
from tkinter import scrolledtext
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import os



window = Tk()
window.title("Буриков Никита Михайлович УБ-23")
window.geometry('1000x500')



def clicked():
    search = name_github.get()
    search2 = int(Shet.get())
    search3 = combo.get()
    s = requests.Session()
    user = UserAgent().random
    header = {
        'user-agent': user
    }
    if search3 == 'Best match':
        url = f"https://github.com/search?o=desc&q={search}&s=&type=Repositories"
    elif search3 == 'Most stars':
        url = f"https://github.com/search?o=desc&q={search}&s=stars&type=Repositories"
    elif search3 == 'Fewest stars':
        url = f"https://github.com/search?o=asc&q={search}&s=stars&type=Repositories"       
    elif search3 == 'Most forks':
        url = f"https://github.com/search?o=desc&q={search}&s=forks&type=Repositories"
    elif search3 == 'Fewest forks':
        url = f"https://github.com/search?o=asc&q={search}&s=forks&type=Repositories"
    elif search3 == 'Recently updated':
        url = f"https://github.com/search?o=desc&q={search}&s=updated&type=Repositories"
    elif search3 == 'Least recently updated':
        url = f"https://github.com/search?o=asc&q={search}&s=updated&type=Repositories"
    r = s.get(url, headers=header)

    soup = BeautifulSoup(r.text, "html.parser")
    languages = soup.find_all("a", class_="v-align-middle")
    lst = [i.text for i in languages]
    href = []
    try:
        for i in range(search2):
            url_rep = f'https://github.com/{lst[i]}'
            r2 = s.get(url_rep, headers=header)
            print(r2.status_code)
            href.append('Название проекта: ' + lst[i] +  ';' +' Языки:')
            soup1 = BeautifulSoup(r2.text, "html.parser")
            for g in soup1.find_all("span", class_="color-fg-default text-bold mr-1"):
                href.append(g.text + ',')
            for k in soup1.find_all("a", title="README.md"):
                otv = 'https://github.com'
                href.append('Ссылка на readme файл: ' + otv + k.get('href'))
    except IndexError:
        text.insert("На странице меньше результатов чем вы запросили")
    try:
        for i in range(len(href)):
            with open("pass_url.txt", "a+") as file:
                for g in range(len(lst)):
                    if href[i] == lst[g]:
                        if str(href[i+1]).endswith("README.md") == True:
                            del href[i]
                            del href[i]
                            text.insert("\nК сожалению не все результаты попали под фильтр интересующих репозиториев\n")
                if str(href[i]).endswith('README.md'):
                    file.write(str(href[i])+'\n'+'\n')
                else:
                    file.write(f'{str(href[i])} ')
    except IndexError:
        pass

    with open('pass_url.txt', 'r+') as f:
        line = f.readlines()
    for i in range(len(line)):
        print(line[i])
        text.insert('1.0' , line[i] )
    os.remove("pass_url.txt")
def delete():
    text.delete(1.0, END)


lbl1= Label(window, text='Введите ключевые слова для поиска:',)
lbl1.grid(column = 0, row = 1, sticky= W)

name_github = Entry(window, width = 20)
name_github.grid(column = 0, row = 1, sticky= W, padx=220)



Shet = Entry(window, width = 5)
Shet.grid(column= 0, row = 2, sticky= W, padx=110 )
Shetlbl = Label(window, text='Кол-во проектов:') 
Shetlbl.grid(column= 0, row = 2, sticky= W)





lblcombo = Label(window, text='Фильтр:')
lblcombo.grid(column= 0, row= 3, sticky= W)
combo = Combobox(window)
combo.grid(column = 0, row = 3, sticky= W, padx=55)
combo['values'] = ('Best match' , 'Most stars', 'Fewest stars', 'Most forks', 'Fowest forks', 'Resently updated', 'Least resently updated' )
combo.current(0)


text = scrolledtext.ScrolledText(window, width=120, height= 20, wrap=WORD)
text.grid(column=0, row = 5 , sticky= W)





butt1= Button(window, width=10, text='Найти', command = clicked )
butt1.grid(column=0, row = 4, sticky= W)
butt2 = Button(window, width=10, text='Очистить', command = delete)
butt2.grid(column=0, row = 4, sticky= W, padx=80)



window.mainloop()


