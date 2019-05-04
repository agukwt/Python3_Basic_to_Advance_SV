#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.geometry()                  # ボタン位置の制御用
        self.master.title('Calculation')        # GUIタイトルの設定

        self.entry = tk.Entry(self.master)      # 入力フォーム宣言
        self.menu_bar = tk.Menu(self.master)    # メニューバー宣言
        self.master.config(menu=self.menu_bar)  # メニューバー作成

        self.create_widgets()                   # GUIの立ち上げ

    def input(self, action):
        self.entry.insert(tk.END, action)

    def clear_all(self):
        self.entry.delete(0, tk.END)

    def clear_one(self):
        txt = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, txt[:-1])

    def equals(self):
        self.value = eval(self.entry.get().replace('÷', '/').replace('×', '*'))
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.value)

    # def test(self):
    #     print('()なし')

    def create_widgets(self):
        # メニューバーの「File」タブに「Exit」を作成
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label='Exit', command=self.master.quit)
        self.menu_bar.add_cascade(label='File', menu=file_menu)

        # 入力フォームを作成
        self.entry.grid(row=0, column=0, columnspan=6, pady=3)
        self.entry.focus_set()

        # ボタンの作成
        # |7| |8| |9|
        tk.Button(self.master, text='7', width=3,
                  command=lambda: self.input(7)).grid(row=1, column=0)
        tk.Button(self.master, text='8', width=3,
                  command=lambda: self.input(8)).grid(row=1, column=1)
        tk.Button(self.master, text='9', width=3,
                  command=lambda: self.input(9)).grid(row=1, column=2)

        # |4| |5| |6|
        tk.Button(self.master, text='4', width=3,
                  command=lambda: self.input(4)).grid(row=2, column=0)
        tk.Button(self.master, text='5', width=3,
                  command=lambda: self.input(5)).grid(row=2, column=1)
        tk.Button(self.master, text='6', width=3,
                  command=lambda: self.input(6)).grid(row=2, column=2)

        # |1| |2| |3|
        tk.Button(self.master, text='1', width=3,
                  command=lambda: self.input(1)).grid(row=3, column=0)
        tk.Button(self.master, text='2', width=3,
                  command=lambda: self.input(2)).grid(row=3, column=1)
        tk.Button(self.master, text='3', width=3,
                  command=lambda: self.input(3)).grid(row=3, column=2)

        # |0| |.| |÷|
        tk.Button(self.master, text='0', width=3,
                  command=lambda: self.input(0)).grid(row=4, column=0)
        tk.Button(self.master, text='.', width=3,
                  command=lambda: self.input('.')).grid(row=4, column=1)
        tk.Button(self.master, text='÷', width=3,
                  command=lambda: self.input('÷')).grid(row=4, column=2)

        # t(|×| |-| |+| |+|)
        tk.Button(self.master, text='×', width=3,
                  command=lambda: self.input('×')).grid(row=1, column=3)
        tk.Button(self.master, text='-', width=3,
                  command=lambda: self.input('-')).grid(row=2, column=3)
        tk.Button(self.master, text='+', width=3,
                  command=lambda: self.input('+')).grid(row=3, column=3)
        tk.Button(self.master, text='%', width=3,
                  command=lambda: self.input('%')).grid(row=4, column=3)

        # t(|AC| |C|)
        tk.Button(self.master, text='AC', width=3,
                  command=lambda: self.clear_all()).grid(row=1, column=4)
        tk.Button(self.master, text='C', width=3,
                  command=lambda: self.clear_one()).grid(row=1, column=5)

        # |=|
        tk.Button(self.master, text='=', width=6,
                  command=lambda: self.equals()).grid(row=4, column=4, columnspan=2)

        # |test|
        # tk.Button(self.master, text='test', width=6,
        #           command=lambda: self.test()).grid(row=3, column=4, columnspan=2)
        tk.Button(self.master, text='test', width=6,
                  command=self.test()).grid(row=3, column=4, columnspan=2)


root = tk.Tk()
app = Application(master=root)
app.mainloop()

