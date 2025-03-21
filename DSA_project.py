from tkinter import *

def home_page():
    window = Tk()
    window.title("My Tkinter Window")
    window.config(background='#303030')
    window.geometry("1000x600")

    button1 = Button(window, text='Line_intersection_1', fg='#303030', bg='#FFFA86', command=Line_intersection_1, padx=20, relief='raised')
    button1.grid(row=1, column=1, padx=50, pady=50)

    button2 = Button(window, text='Line_intersection_2', fg='#303030', bg='#FFFA86', command=Line_intersection_2, padx=20, relief='raised')
    button2.grid(row=2, column=1, padx=50, pady=50)

    button3 = Button(window, text='Line_intersection_3', fg='#303030', bg='#FFFA86', command=Line_intersection_3, padx=20, relief='raised')
    button3.grid(row=3, column=1, padx=50, pady=50)

    button4 = Button(window, text='     Grahm_scan     ', fg='#303030', bg='#FFFA86', command=Grahm_scan, padx=20, relief='raised')
    button4.grid(row=4, column=1, padx=50, pady=50)


    window.mainloop()


def Line_intersection_1():
      
    def are_lines_intersecting_by_slope(line1, line2):
        x1, y1 = line1[0]
        x2, y2 = line1[1]
        m1 = (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else float('inf')

        x1, y1 = line2[0]
        x2, y2 = line2[1]
        m2 = (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else float('inf')

        return m1 != m2

    def plot_lines_with_tkinter(line1, line2, intersection_point):
        window2 = Toplevel()
        window2.title("Lines Intersection by Slope")
        window2.config(background='#303030')

        canvas = Canvas(window2, width=400, height=400, background='#303030')
        canvas.pack()

        x1, y1 = line1[0]
        x2, y2 = line1[1]
        line1_obj = canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)
        display_input_points(canvas, line1, "blue")

        x1, y1 = line2[0]
        x2, y2 = line2[1]
        line2_obj = canvas.create_line(x1, y1, x2, y2, fill="green", width=2)
        display_input_points(canvas, line2, "green")

        if are_lines_intersecting_by_slope(line1,line2):
            x, y = intersection_point
            canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="red")
            display_intersection_point(canvas, intersection_point)
        else: 
            window2.after(1000, lambda: glow_line(canvas, line1_obj))
            window2.after(2000, lambda: glow_line(canvas, line2_obj))

        window2.mainloop()


    def plot_lines_with_tkinter2(line1, line2):
        window2 = Toplevel()
        window2.title("Lines Intersection by Slope")
        window2.config(background='#303030')
        window2.geometry("1000x600")

        canvas = Canvas(window2, width=800, height=800, background='#303030')
        canvas.pack()

        x1, y1 = line1[0]
        x2, y2 = line1[1]
        line1_obj = canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)
        display_input_points(canvas, line1, "blue")

        x1, y1 = line2[0]
        x2, y2 = line2[1]
        line2_obj = canvas.create_line(x1, y1, x2, y2, fill="green", width=2)
        display_input_points(canvas, line2, "green")

        window2.after(1000, lambda: glow_line(canvas, line1_obj))
        window2.after(2000, lambda: glow_line(canvas, line2_obj))

        text = canvas.create_text(400, 780, text="No intersection found", fill="white", font=('bold', 14))
        text.place(x=10, y=10)

        window2.mainloop()

    def display_input_points(canvas, line, color):
        for x, y in line:
            canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill=color)
            canvas.create_text(x + 15, y, text=f"({x}, {y})", fill=color, anchor=W)

    def display_intersection_point(canvas, intersection_point):
        x, y = intersection_point
        canvas.create_text(x + 15, y, text=f"Intersection\n({x}, {y})", fill="red", anchor=W, font=('bold', 10))

    def glow_line(canvas, line_obj, iterations=10, delay=100):
        for _ in range(iterations):
            canvas.itemconfig(line_obj, width=4)
            canvas.update()
            canvas.after(delay)
            canvas.itemconfig(line_obj, width=2)
            canvas.update()
            canvas.after(delay)

    def main_prog(line1, line2):
        if are_lines_intersecting_by_slope(line1, line2):
            intersection_point = ((line2[0][0] + line2[1][0]) / 2, (line2[0][1] + line2[1][1]) / 2)
            plot_lines_with_tkinter(line1, line2, intersection_point)
        else:
            plot_lines_with_tkinter2(line1, line2)

    def input():
        window3 = Toplevel()
        window3.config(background='#303030')
        window3.geometry("1000x600")

        header = Label(window3, bg='#FFFA86', text='Enter values for plotting the lines', width=50, fg='#303030', font=('bold', 14))
        header.pack(pady=10)

        frame = Frame(window3, bg='#303030')
        frame.pack(pady=20)

        values1 = Label(frame, text='Enter values for First line:', bg='#303030', fg='white', font=('bold', 12))
        values1.grid(row=0, column=0, padx=10)

        x11_label = Label(frame, text='X1:', bg='#303030', fg='white', font=('bold', 10))
        y11_label = Label(frame, text='Y1:', bg='#303030', fg='white', font=('bold', 10))
        x12_label = Label(frame, text='X2:', bg='#303030', fg='white', font=('bold', 10))
        y12_label = Label(frame, text='Y2:', bg='#303030', fg='white', font=('bold', 10))

        x11_label.grid(row=1, column=0, padx=10, pady=5)
        y11_label.grid(row=2, column=0, padx=10, pady=5)
        x12_label.grid(row=3, column=0, padx=10, pady=5)
        y12_label.grid(row=4, column=0, padx=10, pady=5)

        x11 = Entry(frame, bg='#f2e694', font=('bold', 10))
        y11 = Entry(frame, bg='#f2e694', font=('bold', 10))
        x12 = Entry(frame, bg='#f2e694', font=('bold', 10))
        y12 = Entry(frame, bg='#f2e694', font=('bold', 10))

        x11.grid(row=1, column=1, padx=10, pady=5)
        y11.grid(row=2, column=1, padx=10, pady=5)
        x12.grid(row=3, column=1, padx=10, pady=5)
        y12.grid(row=4, column=1, padx=10, pady=5)

        values2 = Label(frame, text='Enter values for Second line:', bg='#303030', fg='white', font=('bold', 12))
        values2.grid(row=0, column=2, padx=10)

        x21_label = Label(frame, text='X1:', bg='#303030', fg='white', font=('bold', 10))
        y21_label = Label(frame, text='Y1:', bg='#303030', fg='white', font=('bold', 10))
        x22_label = Label(frame, text='X2:', bg='#303030', fg='white', font=('bold', 10))
        y22_label = Label(frame, text='Y2:', bg='#303030', fg='white', font=('bold', 10))

        x21_label.grid(row=1, column=2, padx=10, pady=5)
        y21_label.grid(row=2, column=2, padx=10, pady=5)
        x22_label.grid(row=3, column=2, padx=10, pady=5)
        y22_label.grid(row=4, column=2, padx=10, pady=5)

        x21 = Entry(frame, bg='#f2e694', font=('bold', 10))
        y21 = Entry(frame, bg='#f2e694', font=('bold', 10))
        x22 = Entry(frame, bg='#f2e694', font=('bold', 10))
        y22 = Entry(frame, bg='#f2e694', font=('bold', 10))

        x21.grid(row=1, column=3, padx=10, pady=5)
        y21.grid(row=2, column=3, padx=10, pady=5)
        x22.grid(row=3, column=3, padx=10, pady=5)
        y22.grid(row=4, column=3, padx=10, pady=5)

        submit_button = Button(window3, text='Submit', command=lambda: submit_button_click(x11, x12, y11, y12, x21, x22, y21, y22), padx=20, bg='#FFFA86', relief='raised', font=('bold', 12))
        submit_button.place(x=500,y=270)

        window3.mainloop()

    def submit_button_click(x11, x12, y11, y12, x21, x22, y21, y22):
        line1 = [(float(x11.get()), float(y11.get())), (float(x12.get()), float(y12.get()))]
        line2 = [(float(x21.get()), float(y21.get())), (float(x22.get()), float(y22.get()))]
        main_prog(line1, line2)

    input()















def Line_intersection_2():
    window2 = Toplevel()  
    window2.title("New Window")
    window2.geometry("1000x600")
    window2.config(background='#303030')
    window2.mainloop()

def Line_intersection_3():
    window2 = Toplevel()  
    window2.title("New Window")
    window2.geometry("1000x600")
    window2.config(background='#303030')
    window2.mainloop()

def Grahm_scan():
    window2 = Toplevel()  
    window2.title("New Window")
    window2.geometry("1000x600")
    window2.config(background='#303030')
    window2.mainloop()




home_page()
