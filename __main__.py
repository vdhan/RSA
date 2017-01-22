"""
RSA
Copyright (C) Hoàng Ân

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import math
import os
import random
import subprocess
from tkinter import *
from tkinter.ttk import *

from An import trim


class Core(Tk):
    def get_w(self):
        return self._w


class Application(Notebook):
    def __init__(self, master=NONE, **kw):
        super().__init__(master, **kw)

        self.path = os.path.dirname(__file__)
        self.master.title("An's RSA cryptography v3.0")
        self.master.resizable(False, False)

        try:
            img = PhotoImage(file=os.path.join(self.path, 'icon.png'))
            self.master.tk.call('wm', 'iconphoto', self.master.get_w(), img)
        except TclError:
            img = PhotoImage(file=os.path.join(self.path, 'icon.gif'))
            self.master.tk.call('wm', 'iconphoto', self.master.get_w(), img)

        self.style = Style()
        self.style.configure('GetE.TEntry', borderwidth=0)

        self.frame1 = Frame(self, padding=10)
        self.frame2 = Frame(self, padding=10)
        self.frame3 = Frame(self, padding=10)
        self.frame4 = Frame(self, padding=10)

        self.it = Text(self.frame1, width=62, height=5)
        self.n_str = StringVar()
        self.k_str = StringVar()
        self.ot = Text(self.frame1, width=62, height=5)

        self.p_str = StringVar()
        self.q_str = StringVar()
        self.e_str = StringVar()
        self.d_str = StringVar()
        self.phi_str = StringVar()
        self.str_l = StringVar()

        self.widgets()
        self.bind_class('Text', '<Control-a>', self.text_selectall)
        self.bind_class('Text', '<Control-v>', self.text_paste)
        self.bind_class('TEntry', '<Control-a>', self.entry_selectall)

    def widgets(self):
        self.add(self.frame1, text='Mã hóa và Giải mã')
        self.add(self.frame2, text='Tìm khóa d')
        self.add(self.frame3, text='Tìm khóa e')
        self.add(self.frame4, text='Tìm p, q')

        Label(self.frame1, text='Nhập: ').grid(row=0, column=0, sticky='e')
        self.it.grid(row=0, column=1, columnspan=3, pady=10, sticky='e')

        Label(self.frame1, text='n: ').grid(row=1, column=0, sticky='e')
        Entry(self.frame1, textvariable=self.n_str).grid(row=1, column=1, sticky='e')

        Label(self.frame1, text='k: ').grid(row=1, column=2, sticky='e')
        Entry(self.frame1, textvariable=self.k_str).grid(row=1, column=3, sticky='e')

        Label(self.frame1, text='Xuất: ').grid(row=2, column=0, sticky='e')
        self.ot.grid(row=2, column=1, columnspan=3, pady=10, sticky='e')

        Button(self.frame1, text='Mã hóa', command=self.encrypt).grid(row=3, column=0, columnspan=2)
        Button(self.frame1, text='Giải mã', command=self.decrypt).grid(row=3, column=2, columnspan=2)

        Label(self.frame2, text='p: ').grid(row=0, column=0)
        Entry(self.frame2, textvariable=self.p_str).grid(row=0, column=1)

        Label(self.frame2, text='q: ').grid(row=0, column=3)
        Entry(self.frame2, textvariable=self.q_str).grid(row=0, column=4)

        Label(self.frame2, text='e: ').grid(row=1, column=0)
        Entry(self.frame2, textvariable=self.e_str).grid(row=1, column=1)

        Label(self.frame2, text='d: ').grid(row=1, column=3)
        Entry(self.frame2, textvariable=self.d_str, state='readonly').grid(row=1, column=4)

        Button(self.frame2, text='Tìm khóa', command=self.find_d).grid(row=2, column=2)

        Label(self.frame3, text='p: ').grid(row=0, column=0)
        Entry(self.frame3, textvariable=self.p_str).grid(row=0, column=1)

        Label(self.frame3, text='q: ').grid(row=0, column=3)
        Entry(self.frame3, textvariable=self.q_str).grid(row=0, column=4)

        Label(self.frame3, text='n: ').grid(row=1, column=0)
        Entry(self.frame3, textvariable=self.n_str, state='readonly').grid(row=1, column=1)

        Label(self.frame3, text='\u03C6: ').grid(row=1, column=3)
        Entry(self.frame3, textvariable=self.phi_str, state='readonly').grid(row=1, column=4)

        Label(self.frame3, text='e: ').grid(row=2, column=0)
        Entry(self.frame3, textvariable=self.e_str, state='readonly', width=60, style='GetE.TEntry').grid(
            row=2, column=1, columnspan=4, sticky='w')

        Button(self.frame3, text='Tìm khóa', command=self.find_e).grid(row=3, column=2)

        self.str_l.set(2048)
        Label(self.frame4, text='Độ dài khóa: ').grid(row=0, column=0)
        Entry(self.frame4, textvariable=self.str_l).grid(row=0, column=1)

        Label(self.frame4, text='p: ').grid(row=1, column=0)
        Entry(self.frame4, textvariable=self.p_str, state='readonly').grid(row=1, column=1)

        Label(self.frame4, text='q: ').grid(row=1, column=3)
        Entry(self.frame4, textvariable=self.q_str, state='readonly').grid(row=1, column=4)

        Button(self.frame4, text='Tìm p, q', command=self.find_pq).grid(row=2, column=2)

        for child in self.frame2.winfo_children():
            child.grid_configure(pady=10)

        for child in self.frame3.winfo_children():
            child.grid_configure(pady=10)

        for child in self.frame4.winfo_children():
            child.grid_configure(pady=10)

        self.it.focus()

    def encrypt(self):
        self.ot.delete(1.0, 'end')

        try:
            n = int(self.n_str.get())
            e = int(self.k_str.get())
            m = trim(self.it.get(1.0, 'end'))
            c = []
            for x in m:
                y = pow(ord(x), e, n)
                c.append(str(y))

            self.ot.insert('end', ' '.join(c))
        except ValueError:
            self.ot.insert('end', 'Input Error!')

    def decrypt(self):
        self.ot.delete(1.0, 'end')
        try:
            n = int(self.n_str.get())
            d = int(self.k_str.get())
            c = self.it.get(1.0, 'end').split()
            m = ''
            for y in c:
                x = pow(int(y), d, n)
                m += chr(x)

            self.ot.insert('end', m)
        except ValueError:
            self.ot.insert('end', 'Input Error!')

    @staticmethod
    def inverse(a, z):
        if a < 0:
            a %= z

        if math.gcd(a, z) == 1:
            n, y, y2 = z, 1, 0
            while a != 0:
                q = z // a
                z, a = a, z % a
                y, y2 = y2 - q * y, y
            return y2 % n

        return 0

    def find_d(self):
        try:
            p = int(self.p_str.get())
            q = int(self.q_str.get())
            e = int(self.e_str.get())
            o = (p - 1) * (q - 1)
            d = self.inverse(e, o)
            self.d_str.set(d)
        except ValueError:
            self.d_str.set('Input Error!')

    def find_e(self):
        try:
            p = int(self.p_str.get())
            q = int(self.q_str.get())
            o = (p - 1) * (q - 1)
            if o < 3:
                raise ValueError

            self.n_str.set(p * q)
            self.phi_str.set(o)

            while True:
                e = random.randint(2, o)
                if math.gcd(e, o) == 1:
                    self.e_str.set(e)
                    break

        except ValueError:
            self.e_str.set('Input Error!')

    @staticmethod
    def text_selectall(event):
        event.widget.tag_add('sel', '1.0', 'end-1c')  # select string only

    @staticmethod
    def text_paste(event):
        widget = event.widget
        try:
            start = widget.index('sel.first')
            end = widget.index('sel.last')
            widget.delete(start, end)
        except TclError:  # not select text
            pass

        widget.event_generate('<<Paste>>')

    @staticmethod
    def entry_selectall(event):
        event.widget.select_range(0, 'end')

    def find_pq(self):
        try:
            l = int(self.str_l.get())
            length = l // 2

            process = subprocess.run(['openssl', 'prime', '-generate', '-bits', str(length)], stdout=subprocess.PIPE)
            p = int(process.stdout)
            self.p_str.set(p)

            process = subprocess.run(['openssl', 'prime', '-generate', '-bits', str(length)], stdout=subprocess.PIPE)
            q = int(process.stdout)
            self.q_str.set(q)
        except ValueError:
            self.p_str.set('Input Error!')

if __name__ == '__main__':
    root = Core()
    app = Application(root, padding=10)
    app.grid(column=0, row=0, sticky='wnes')
    app.mainloop()
