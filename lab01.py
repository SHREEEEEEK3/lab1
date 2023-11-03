import tkinter as tk

def clickbut():
    a = entry1.get()
    b = entry2.get()
    c = entry3.get()

    if a.isdigit() and b.isdigit() and c.isdigit():
        a, b, c = int(a), int(b), int(c)

        if a + b > c and b + c > a and a + c > b:
            if a == b == c:
                reslabel.config(text="Равносторонний треугольник")
            elif a == b or a == c or b == c:
                reslabel.config(text="Равнобедренный треугольник")
            else:
                reslabel.config(text="Разносторонний треугольник")
        else:
            reslabel.config(text="Такого тругольника не существует")
    else:
        reslabel.config(text="Нужно вводить только целые положительные числа")

root = tk.Tk()
root.title("Тип треугольника")
root.geometry("350x200")

label1 = tk.Label(root, text="Длина первой стороны:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Длина второй стороны:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

label3 = tk.Label(root, text="Длина третьей стороны:")
label3.pack()
entry3 = tk.Entry(root)
entry3.pack()
button = tk.Button(root, text="Подтвердить", command=clickbut)
button.pack()
reslabel = tk.Label(root, text="")
reslabel.pack()

root.mainloop()