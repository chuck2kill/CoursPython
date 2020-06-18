from tkinter import *

fen1 = Tk()

# création des widgets 'Label' et 'Entry'
Label(fen1, text='Premier champ :').grid(row=1, sticky=E)
Label(fen1, text='Second :').grid(row=2, sticky=E)
Label(fen1, text='Troisième :').grid(row=3, sticky=E)
entr1 = Entry(fen1)
entr2 = Entry(fen1)
entr3 = Entry(fen1)
chek1 = Checkbutton(fen1, text='Case à cocher, pour voir')

# création d'un widget canvas contenant une image bitmap:
can1 = Canvas(fen1, width=200, height=200, bg='white')
photo = PhotoImage(file='image-asset.png')
item = can1.create_image(100, 100, image=photo)

# mise en page à l'aide de la méthode 'grid'
entr1.grid(row=1, column=2)
entr2.grid(row=2, column=2)
entr3.grid(row=3, column=2)
can1.grid(row=1, column=3, rowspan=3, padx=10, pady=5)
chek1.grid(columnspan=2)

# démarrage
fen1.mainloop()
