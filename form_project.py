import tkinter as tk
import os


window = tk.Tk()
window.title('Formularz składania zamówienia')
window.geometry('700x600')
window.resizable(False, False)


def show_info():
    print('Imię: ', entry4.get() )
    print('Nazwisko: ', entry5.get() )
    print('E-mail: ', entry6.get() )
    print('Wiek: ', spin.get() )
    print('Płeć: ', radioValue.get())
    print('Liczba dni: ', scale.get())





scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)
samochod = tk.PhotoImage(file='samochod.png')



label1 = tk.Label(master= window, text='Formularz składania zamówienia', fg='white', bg='grey', width='40', height='3', cursor = 'dot', anchor = tk.CENTER, font = 'Stencil 24 bold')
label1.pack()


label2 = tk.Label(master=window, image=samochod, width=250, height=150)
label2.place(x = 440, y= 120)
label3 = tk.Label(master= window, text='BMW Motorsport 450KM', fg='white', bg='grey', width='25', height='1', cursor = 'dot', anchor = tk.S, font = 'Perpetua 13 bold')
label3.place(x = 439, y = 280)



label4 = tk.Label(master =window, text='Imię: *', fg='black', width='5', height='1', anchor = tk.W, font = 'Cambria 15 italic')
label4.place(x = 10, y = 130)
entry4 = tk.Entry(window)
entry4.place(x = 120, y = 137)

 


label5 = tk.Label(master= window, text='Nazwisko: *', fg='black', width='10', height='1', anchor = tk.W, font = 'Cambria 15 italic')
label5.place(x = 10, y = 180)
entry5 = tk.Entry(window)
entry5.place(x = 120, y = 187)


label6 = tk.Label(master= window, text='E-mail: *', fg='black', width='7', height='1', anchor = tk.W, font = 'Cambria 15 italic')
label6.place(x = 10, y = 230)
entry6 = tk.Entry(window, width=30)
entry6.place(x = 120, y = 237)

label7 = tk.Label(master= window, text='Wiek: ', fg='black', width='5', height='1', anchor = tk.W, font = 'Cambria 15 italic')
label7.place(x = 10, y = 280)
spin = tk.Spinbox(window, from_ = 0, to = 70)
spin.place(x = 120, y=287)


label8 = tk.Label(master= window, text='Płeć: ', fg='black', bg='pink', width='5', height='1', anchor = tk.W, font = 'Cambria 15 italic')
label8.place(x = 10, y = 330)

radioValue = tk.StringVar()
radio1 = tk.Radiobutton(window, text='Mężczyzna', variable=radioValue, value= 'Mężczyzna')
radio1.place(x = 100, y = 336)
radio2 = tk.Radiobutton(window, text='Kobieta', variable=radioValue, value='Kobieta')
radio2.place(x = 190, y = 336)
radio3 = tk.Radiobutton(window, text='Inna', variable=radioValue, value= 'ZAGROŻONY KLIENT')
radio3.place(x = 260, y = 336)
radio4 = tk.Radiobutton(window, text='Nie chce podawać', variable=radioValue, value='Nie chciał podać')
radio4.place(x = 320, y = 336)


label9 = tk.Label(master= window, text='Liczba dni wypożyczenia: *', fg='black', width='20', height='1', font = 'Cambria 15 italic')
label9.place(x = 10, y = 380)
scale = tk.Scale(window, from_ = 0, to = 14, orient=tk.HORIZONTAL)
scale.place(x = 260, y = 367)

label10 = tk.Label(master= window, text='* - pola wymagane', fg='black', width='20', height='1', font = 'Cambria 10 italic')
label10.place(x = 5, y = 430)


button = tk.Button(text='Potwierdź', command=show_info, bg='green', fg='black', bd=10, activebackground='red', activeforeground='white', font='Helvetica 16 bold italic', height=2, width=8)
button.place(x = 400, y=400)


window.mainloop()