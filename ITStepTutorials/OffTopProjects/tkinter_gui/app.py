import tkinter as tk


app = tk.Tk()
# title
app.title('Test app')
app['bg'] = '#ee99cc'

# size of window
app.geometry('500x400')
# not we cannot change size of window
app.resizable(width=False, height=False)


def hello_world():
    label_hello = tk.Label(app, text='Hello World!', font='Arial 20')
    label_hello['bg'] = '#fff'
    label_hello.pack(side=tk.TOP) # position of label top, left, right or bottom

# button calling hello_world
btn = tk.Button(text='Get Hello', command=hello_world, width=20)
btn.pack(pady=10)

#  Using frames
# frame_message = tk.Frame(app)
# frame_message.pack()
# message = tk.Label(frame_message, text='Frame label', font='Roboto 15')
# message.pack()

frame_one = tk.Frame(app)
frame_one.pack()
frame_two = tk.Frame(app)
frame_two.pack()
frame_three = tk.Frame(app)
frame_three.pack()
frame_op = tk.Frame(app)
frame_op.pack()

# test
saved_input = ""
def on_button_press(expression):
    global saved_input
    print(expression)
    saved_input += str(expression)
    raw_result.set(saved_input)

def get_result():
    result.set('= ' + str(eval(saved_input)))

# Number buttons
btn_one = tk.Button(frame_one, text='1', width=12, bg='#fefefe',
                    command=lambda: on_button_press(1))
btn_two = tk.Button(frame_one, text='2', width=12, bg='#fefefe',
                    command=lambda: on_button_press(2))
btn_three = tk.Button(frame_one, text='3', width=12, bg='#fefefe',
                      command=lambda: on_button_press(3))
btn_four = tk.Button(frame_two, text='4', width=12, bg='#fefefe',
                     command=lambda: on_button_press(4))
btn_five = tk.Button(frame_two, text='5', width=12, bg='#fefefe',
                     command=lambda: on_button_press(5))
btn_six = tk.Button(frame_two, text='6', width=12, bg='#fefefe',
                    command=lambda: on_button_press(6))
btn_seven = tk.Button(frame_three, text='7', width=12, bg='#fefefe',
                      command=lambda: on_button_press(7))
btn_eight = tk.Button(frame_three, text='8', width=12, bg='#fefefe',
                      command=lambda: on_button_press(8))
btn_nine = tk.Button(frame_three, text='9', width=12, bg='#fefefe',
                     command=lambda: on_button_press(9))

# Operation buttons
subtraction = tk.Button(frame_op, text='-', width=12,
                        command=lambda: on_button_press('-'))
addition = tk.Button(frame_op, text='+', width=12,
                     command=lambda: on_button_press('+'))
equals = tk.Button(frame_op, text='=', width=12,
                   command=lambda: get_result())

raw_result = tk.StringVar()
oper_expr = tk.Entry(app, textvar=raw_result, font='cursive 15')
oper_expr.pack()

result = tk.StringVar()
entry_expr = tk.Entry(app, textvar=result, font='cursive 15')
entry_expr.pack()

# Locations of number buttons
btn_one.pack(side=tk.LEFT)
btn_two.pack(side=tk.LEFT)
btn_three.pack(side=tk.LEFT)
btn_four.pack(side=tk.LEFT)
btn_five.pack(side=tk.LEFT) 
btn_six.pack(side=tk.LEFT)
btn_seven.pack(side=tk.LEFT)
btn_eight.pack(side=tk.LEFT)
btn_nine.pack(side=tk.LEFT)

# Locations of operation buttons
subtraction.pack(side=tk.LEFT)
addition.pack(side=tk.LEFT)
equals.pack(side=tk.LEFT)

app.mainloop()
