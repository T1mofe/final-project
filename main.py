from tkinter import *
import time
from random import randint

#создаем класс для удобства
class Reaction:
    def __init__(self) -> None:
        self.start_program()

#создаем функцию для старта
    def start_game(self):
        self.frame.config(bg='green')
        self.start_time = time.time()
        self.frame.bind('<Button-1>', self.click)
    
#по нажатию левой кнопки мыши у нас начинается отсчет до начала ,если мы нажмем слишком рано  , то функия прервется  
    def btn_click(self):
        self.frame.config(bg='red')
        self.label.config(text='Приготовьтесь...')
        self.cancel = self.speed.after(randint(1000, 5000), self.start_game)
        self.frame.bind('<Button-1>', self.error_click)

#просто функия тестом, если нажали слишком рано 
    def error_click(self, event):
        self.label.config(text=f'Вы кликнули слишком рано! Попробуйте снова.')

#функция для того чтобы программа отменялась ,если нажали слишком рано
        if self.cancel is not None:
            self.speed.after_cancel(self.cancel)
            self.cancel = None

#функция дял рссчета секунд после нажатия на зеленый фон
    def click(self, event):
        self.end_time= time.time()
        self.frame.unbind('<Button-1>')
        self.frame.config(bg='red')
        self.label.config(text=f'Секунды: {round(self.end_time - self.start_time, 3)}')

#сама конструкция тк интера которая запускает окно определяет: его размер, задний фон, кнопки, framы
    def start_program(self):
        self.speed = Tk()

        self.speed['bg'] = '#fafafa'
        self.speed.title('Тест на реакцию')
        self.speed.wm_attributes('-alpha', 0.7)
        self.speed.geometry('500x420')

        self.speed.resizable(width=False, height=False)

        self.label = Label(self.speed, text=' ')

        self.frame = Frame(self.speed, bg = 'white', height=420)

        self.btn = Button(self.speed, text='Начать', bg ='grey', command=self.btn_click)
        self.btn.pack()
        
        self.label.pack()

        self.frame.pack(side='top', fill='both')

        self.speed.mainloop()

#запускающая окно
program = Reaction()