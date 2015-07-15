import os
path = os.path.dirname(__file__) + '/'

from tkinter import *
from tkinter.ttk import *
from An import *

def encrypt():
	ot.delete(1.0, 'end')
	try:
		n = int(nStr.get())
		e = int(kStr.get())
		m = trim(it.get(1.0, 'end'))
		c = []
		for x in m:
			y = pow(ord(x), e, n)
			c.append(str(y))
	
		ot.insert('end', ' '.join(c))

	except:
		ot.insert('end', 'Input Error!')

def decrypt():
	ot.delete(1.0, 'end')
	try:
		n = int(nStr.get())
		d = int(kStr.get())
		c = it.get(1.0, 'end').split()
		m = ''
		for y in c:
			x = pow(int(y), d, n)
			m += chr(x)
		
		ot.insert('end', m)
	except:
		ot.insert('end', 'Input Error!')

def encrypt2():
	ot.delete(1.0, 'end')
	try:
		n = int(nStr.get())
		e = int(kStr.get())
		m = it.get(1.0, 'end').split()
		c = []
		for x in m:
			y = pow(int(x), e, n)
			c.append(str(y))
			
		ot.insert('end', ' '.join(c))
	except:
		ot.insert('end', 'Input Error!')

def decrypt2():
	ot.delete(1.0, 'end')
	try:
		n = int(nStr.get())
		d = int(kStr.get())
		c = it.get(1.0, 'end').split()
		m = []
		for y in c:
			x = pow(int(y), d, n)
			m.append(str(x))
		
		ot.insert('end', ' '.join(m))
	except:
		ot.insert('end', 'Input Error!')

def findD():
	try:
		p = int(pStr.get())
		q = int(qStr.get())
		e = int(eStr.get())
		o = (p - 1) * (q - 1)
		d = inverse(e, o)
		dStr.set(d)
	except:
		dStr.set('Input Error!')
		
def findE():
	try:
		p = int(pStr.get())
		q = int(qStr.get())
		o = (p - 1) * (q - 1)

		nStr.set(p * q)
		phiStr.set(o)
		l = []
		for i in range(2, o):
			if gcd(i, o) == 1:
				l.append(str(i))

		eLst.set(', '.join(l))
	except:
		eLst.set('Input Error!')

if __name__ == '__main__':
	root = Tk()
	root.title("An's RSA cryptography v2.0")
	img = PhotoImage(file = path + 'icon.gif')
	root.tk.call('wm', 'iconphoto', root._w, img)
	root.resizable(False, False)

	style = Style()
	themes = style.theme_names()
	if 'xpnative' in themes:
		style.theme_use('xpnative')
	elif 'aqua' in themes:
		style.theme_use('aqua')
	if 'clam' in themes:
		style.theme_use('clam')
	else:
		style.theme_use('default')

	nb = Notebook(root, padding = 10)
	nb.grid(column = 0, row = 0, sticky = 'wnes')
	
	fm1 = Frame(nb, padding = 10)
	fm2 = Frame(nb, padding = 10)
	fm3 = Frame(nb, padding = 10)
	
	nb.add(fm1, text = 'Mã hóa và Giải mã')
	nb.add(fm2, text = 'Tìm khóa d')
	nb.add(fm3, text = 'Tìm khóa e')
	
	Label(fm1, text = 'Nhập: ').grid(row = 0, column = 0, sticky = 'e')
	it = Text(fm1, width = 62, height = 5)
	it.grid(row = 0, column = 1, columnspan = 3, pady = 10, sticky = 'e')
	
	Label(fm1, text = 'n: ').grid(row = 1, column = 0, sticky = 'e')
	nStr = StringVar()
	Entry(fm1, textvariable = nStr).grid(row = 1, column = 1, sticky = 'e')
	
	Label(fm1, text = 'k: ').grid(row = 1, column = 2, sticky = 'e')
	kStr = StringVar()
	Entry(fm1, textvariable = kStr).grid(row = 1, column = 3, sticky = 'e')
	
	Label(fm1, text = 'Xuất: ').grid(row = 2, column = 0, sticky = 'e')
	ot = Text(fm1, width = 62, height = 5)
	ot.grid(row = 2, column = 1, columnspan = 3, pady = 10, sticky = 'e')
	
	Button(fm1, text = 'Mã hóa', command = encrypt).grid(row = 3, column = 0)
	Button(fm1, text = 'Giải mã', command = decrypt).grid(row = 3, column = 1)
	Button(fm1, text = 'Mã hóa (số)', command = encrypt2).grid(row = 3, column = 2)
	Button(fm1, text = 'Giải mã (số)', command = decrypt2).grid(row = 3, column = 3)
	
	Label(fm2, text = 'p: ').grid(row = 0, column = 0)
	pStr = StringVar()
	Entry(fm2, textvariable = pStr).grid(row = 0, column = 1)
	
	Label(fm2, text = 'q: ').grid(row = 0, column = 3)
	qStr = StringVar()
	Entry(fm2, textvariable = qStr).grid(row = 0, column = 4)
	
	Label(fm2, text = 'e: ').grid(row = 1, column = 0)
	eStr = StringVar()
	Entry(fm2, textvariable = eStr).grid(row = 1, column = 1)
	
	Label(fm2, text = 'd: ').grid(row = 1, column = 3)
	dStr = StringVar()
	Entry(fm2, textvariable = dStr, state = 'readonly').grid(row = 1, column = 4)
	
	Button(fm2, text = 'Tìm khóa', command = findD).grid(row = 2, column = 2)
	
	Label(fm3, text = 'p: ').grid(row = 0, column = 0)
	Entry(fm3, textvariable = pStr).grid(row = 0, column = 1)
	
	Label(fm3, text = 'q: ').grid(row = 0, column = 3)
	Entry(fm3, textvariable = qStr).grid(row = 0, column = 4)
	
	Label(fm3, text = 'n: ').grid(row = 1, column = 0)
	Entry(fm3, textvariable = nStr, state = 'readonly').grid(row = 1, column = 1)

	Label(fm3, text = '\u03C6: ').grid(row = 1, column = 3)
	phiStr = StringVar()
	Entry(fm3, textvariable = phiStr, state = 'readonly').grid(row = 1, column = 4)

	Label(fm3, text = 'e: ').grid(row = 2, column = 0)
	eLst = StringVar()
	Label(fm3, textvariable = eLst, wraplength = 500).grid(row = 2, column = 1, columnspan = 4)

	Button(fm3, text = 'Tìm khóa', command = findE).grid(row = 3, column = 2)

	for child in fm2.winfo_children():
		child.grid_configure(pady = 10)

	for child in fm3.winfo_children():
		child.grid_configure(pady = 10)

	it.focus()
	root.mainloop()