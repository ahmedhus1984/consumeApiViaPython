'''
1.
self.__unit = tk.IntVar(value=1)  # Set default to 1 (No Boost)
'''

import tkinter as tk
from tkinter import ttk
import requests

url = "http://66.96.207.213:3000/api/calc"

class MyFirstGUI:
    def __init__(self):
        self.__win = tk.Tk()
        self.__top=tk.Frame(self.__win)
        self.__bot=tk.Frame(self.__win)

        self.__num1_lbl=tk.Label(self.__top, text='Number 1: ')
        self.__num2_lbl=tk.Label(self.__top, text='Number 2: ')
        self.__result_lbl=tk.Label(self.__top, text='Result: ')
        self.__num1_ety=tk.Entry(self.__top)
        self.__num2_ety=tk.Entry(self.__top)
        self.__output_lbl=tk.Label(self.__top)

        self.__add_btn=tk.Button(self.__bot, text='+')
        self.__sub_btn=tk.Button(self.__bot, text='-')
        self.__mul_btn=tk.Button(self.__bot, text='*')
        self.__div_btn=tk.Button(self.__bot, text='/')

        self.topGrid()
        self.botGrid()
        self.mainGrid()

        self.__add_btn.bind('<Button-1>', self.add)
        self.__sub_btn.bind('<Button-1>', self.sub)
        self.__mul_btn.bind('<Button-1>', self.mul)
        self.__div_btn.bind('<Button-1>', self.div)

        self.__win.title('Basic Calculator')
        self.__win.geometry('500x200')
        self.__win.resizable(True,True)
        self.__win.mainloop()

    def topGrid(self):
        self.__num1_lbl.grid(row=0, column=0, sticky='w')
        self.__num2_lbl.grid(row=2, column=0, sticky='w')
        self.__result_lbl.grid(row=3, column=0, sticky='w')
        
        self.__num1_ety.grid(row=0, column=1, sticky='nsew')
        self.__num2_ety.grid(row=2, column=1, sticky='nsew')
        self.__output_lbl.grid(row=3, column=1, sticky='nsew')

        self.__top.columnconfigure(index=1, weight=1)

        self.__output_lbl.configure(background='azure')

    def botGrid(self):
        self.__add_btn.grid(row=0, column=0, sticky='nsew')
        self.__sub_btn.grid(row=0, column=1, sticky='nsew')
        self.__mul_btn.grid(row=0, column=2, sticky='nsew')
        self.__div_btn.grid(row=0, column=3, sticky='nsew')
 
        self.__bot.columnconfigure(index=0, weight=1)
        self.__bot.columnconfigure(index=1, weight=1)
        self.__bot.columnconfigure(index=2, weight=1)
        self.__bot.columnconfigure(index=3, weight=1)

        self.__bot.rowconfigure(index=0, weight=1)  # ADD THIS

    def mainGrid(self):
        self.__top.grid(row=0, column=0, sticky='nsew')
        self.__bot.grid(row=1, column=0, sticky='nsew')

        self.__win.columnconfigure(index=0, weight=1)
        self.__win.rowconfigure(index=1, weight=1)
      
    def add(self, evt):
        self.calculate('+')

    def sub(self, evt):
        self.calculate('-')

    def mul(self, evt):
        self.calculate('*')

    def div(self, evt):
        self.calculate('/')

    def calculate(self, operator):
        try:
            params = {
                'a': float(self.__num1_ety.get()),
                'o': operator,  # operator passed from the button
                'b': float(self.__num2_ety.get())
            }
            response = requests.get(url, params=params, timeout=5)  # Timeout added here
            response.raise_for_status()  # Will raise an HTTPError if the status is 4xx/5xx
            data = response.json()
            result = data.get('result')
            if result is None:
                self.__output_lbl.configure(text="Error: No result from server")
            else:
                self.__output_lbl.configure(text=str(result))
        except requests.exceptions.Timeout:
            self.__output_lbl.configure(text="Error: Timeout")
        except requests.exceptions.RequestException as e:
            self.__output_lbl.configure(text=f"Request Error: {e}")
        except Exception as e:
            self.__output_lbl.configure(text=f"Error: {e}")

g = MyFirstGUI()