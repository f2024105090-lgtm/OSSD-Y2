import tkinter as tk
count=0

def increment():
    global count
    count+=1
    counter.config(text=str(count))


root = tk.Tk()

counter=tk.Label(root, text="0").pack()
incremet=tk.Button(root, text="Increment").pack()
decrement=tk.Button(root, text="Decrement").pack()
reset=tk.Button(root, text="Reset").pack()












import tkinter as tk

count = 0

def increment():
    global count
    count += 1
    label.config(text=str(count))

def decrement():
    global count
    count -= 1
    label.config(text=str(count))

def reset():
    global count
    count = 0
    label.config(text=str(count))

root = tk.Tk()
root.title("Counter App")
root.geometry("300x200")

label = tk.Label(root, text="0", font=("Arial", 20))
label.pack(pady=20)

btn1 = tk.Button(root, text="Increment", command=increment)
btn1.pack()

btn2 = tk.Button(root, text="Decrement", command=decrement)
btn2.pack()

btn3 = tk.Button(root, text="Reset", command=reset)
btn3.pack()

root.mainloop()







