import service
from tkinter import *
import time

class Reaction:
    def __init__(self) -> None:
        self.start_program()

    
    def btn_click(self):   
        service.start_timer()
        self.frame.config(bg='green')
        
        self.start_time = time.time()
        self.frame.bind('<Button-1>', self.click)

    def click(self, event):
        self.end_time= time.time()
        self.frame.unbind('<Button-1>')
        self.frame.config(bg='red')
        self.label.config(text=f'Секунды: {round(self.end_time - self.start_time, 3)}')

    def start_program(self):
        self.speed = Tk()

        self.speed['bg'] = '#fafafa'
        self.speed.title('Тест на реакцию')
        self.speed.wm_attributes('-alpha', 0.7)
        self.speed.geometry('500x420')

        self.speed.resizable(width=False, height=False)

        self.frame = Frame(self.speed, bg = 'red', height=420)

        self.btn = Button(self.speed, text='Начать', bg ='grey', command=self.btn_click)
        self.btn.pack()

        self.label = Label(self.speed, text='')
        self.label.pack()

        self.frame.pack(side='top', fill='both')


        self.speed.mainloop()

program = Reaction()