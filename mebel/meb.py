from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton


class Core:

    def entry():
        global case_ch, up, Combo, combo, lenght, width, height, door_amount, y_amount, p_amount, s_amount, chk, right, up, down
        if case_ch.get() == 'Встроенный':
            '''стенки'''
            left = IntVar()
            chk = Checkbutton(window, text='левая стенка', var=left)  
            left.set(0) # False
            chk.grid(column=0, row=5)
            right = IntVar()
            chk2 = Checkbutton(window, text='правая стенка', var=right)  
            right.set(0) # False
            right.set(1) # True
            chk2.grid(column=1, row=5)
            up = IntVar()
            chk3 = Checkbutton(window, text='верхняя стенка', var=up)  
            up.set(0) # False
            up.set(1) # True
            chk3.grid(column=2, row=5)
            down = IntVar()
            chk4 = Checkbutton(window, text='нижняя стенка', var=down)  
            down.set(0) # False
            down.set(1) # True
            chk4.grid(column=3, row=5)
        else:
            left = 1 
            right = 1
            up = 1
            down = 1

        '''Размеры шкафа'''
        lenght = Entry(window,width=10) 
        lenght.grid(column=1, row=1) 
        lbl = Label(window, text="Введите Глубину - ")  
        lbl.grid(column=0, row=1) 
        height = Entry(window,width=10)  
        height.grid(column=3, row=1) 
        lbl2 = Label(window, text="Ширину - ")  
        lbl2.grid(column=2, row=1) 
        width = Entry(window,width=10)  
        width.grid(column=5, row=1) 
        lbl3 = Label(window, text="Высоту - ")  
        lbl3.grid(column=4, row=1) 

        '''Двери'''
        file = open('costs.txt')
        mat = file.read()
        Combo = Combobox(window)
        Combo['values'] = mat
        Combo.grid(column = 5, row = 2)
        lbl_mat = Label(window, text = "Материал двери - ")
        lbl_mat.grid(column = 4, row = 2)
        file = open('door_system.txt')
        door_system = file.read()
        combo = Combobox(window)  
        combo['values'] = door_system
        combo.grid(column=3, row=2) 
        lbl_door = Label(window, text = "Система дверей - ")
        lbl_door.grid(column = 2, row = 2)
        door_amount = Entry(window, width = 10)
        door_amount.grid(column = 1, row = 2)
        lbl_door2 = Label(window, text = "Кол-во дверей - ")
        lbl_door2.grid(column = 0, row = 2)

        '''Внутренности шкафа'''
        lbl_y = Label(window, text = "Количество ящиков - ")
        y_amount = Entry(window, width = 10)
        lbl_y.grid(column = 0, row = 3)
        y_amount.grid(column = 1, row = 3)
        lbl_p = Label(window, text = "Количество полок - ")
        p_amount = Entry(window, width = 10)
        lbl_p.grid(column = 2, row = 3)
        p_amount.grid(column = 3, row = 3)
        lbl_s = Label(window, text = "ширина полок - ")
        s_amount = Entry(window, width = 10)
        lbl_s.grid(column = 4, row = 3)
        s_amount.grid(column = 5, row = 3)

        '''Кнопка подсчёта'''
        btn = Button(window, text = "Рез-таты", command = Core.count)
        btn.grid(column = 3, row = 6)

    def count():    
        summ = 0 
        cpy = 2700
        ldsp = 2500
        up = up.get()
        s = float(s_amount.get())
        p = int(p_amount.get())
        y = int(y_amount.get())
        l = float(lenght.get())
        w = float(width.get())
        h = float(height.get())
        c = int(combo.get())
        C = int(Combo.get())
        d = int(door_amount.get())
        inside = (cpy * y) + (p * ldsp * l * s)
        outside = (l * w  * ldsp * up) + (l * w  * ldsp * down) *  + (w * h * 600) + (h * l * ldsp * chk) + (h * l * ldsp * right) + (c * d) + (C * w * h)
        summ = outside + inside
        lbl_ans = Label(window, text = summ)
        lbl_ans.grid(column = 3, row = 7)


window = Tk()
window.title("Счёт мебели")
window.geometry('900x900')
case = Label(window, text = "Выберите тип шкафа")
case.grid(column = 1, row = 0)
case_ch = Combobox(window)
case_ch['values'] = ['Стандартный', 'Встроенный']
case_ch.grid(column = 3, row = 0)
btn2= Button(window, text = "Выбрать", command = Core.entry)
btn2.grid(column = 0, row = 0)
window.mainloop()