from tkinter import *

ablak = Tk()
ablak.Title('Próba')
ablak.minsize(200, 100)

szoveg = Label(ablak, text='Szia!')
gomb = Button(ablak, text='Ok', command=ablak.destroy)

szoveg.pack()
gomb.pack()

mainloop()