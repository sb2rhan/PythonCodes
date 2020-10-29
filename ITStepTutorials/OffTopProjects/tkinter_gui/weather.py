import tkinter as tk
import os
import requests
import pprint
import PIL
from PIL import ImageTk
from dotenv import load_dotenv
load_dotenv()


FONT_MAIN = 'Arial 16'
KEY = os.getenv('WEATHER_KEY')
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={KEY}'


app = tk.Tk()
app.title('Weather app')
app['bg'] = '#fff'

app.geometry('600x450')
app.resizable(width=False, height=False)

# main frame
frame = tk.Frame(app)
frame['bg'] = '#fff'
frame.pack(fill=tk.X, ipadx=8, padx=10, pady=10)

# output frame
out_frame = tk.Frame(app)
out_frame['bg'] = '#fff'
out_frame.pack(fill=tk.X, ipadx=10, padx=10, pady=10)


city_label = tk.Label(frame, text='City:', font=FONT_MAIN, bg='#fff')
city_label.pack(side=tk.LEFT)

city_name = tk.StringVar()
entry_city = tk.Entry(frame, textvar=city_name, font=FONT_MAIN)
entry_city.pack(side=tk.LEFT)


def get_data():
    city = entry_city.get()
    response = requests.get(WEATHER_URL.format(city=city, KEY=KEY))
    json_res = response.json()
    pprint.pprint(json_res)
    state_code['text'] = (json_res['name'] + ', ' + json_res['sys']['country'])
    temperature['text'] = str(json_res['main']['temp'] - 273.15) + ' ℃'
    description['text'] = (json_res['weather'][0]['description'])
    weather_icon = f"D:\\Projects\\PythonCodes\\ITStepTutorials\\OffTopProjects\\tkinter_gui\\weather_icon\\{json_res['weather'][0]['icon']}@2x.png"
    image = ImageTk.PhotoImage(image=PIL.Image.open(weather_icon))
    icons = tk.Label(out_frame, image=image)
    icons['bg'] = '#fff'
    icons.image = image
    icons.pack(side=tk.BOTTOM)

btn = tk.Button(frame, text='Get weather', width=12, font=FONT_MAIN,
                command=get_data)
btn.pack(side=tk.LEFT)


state_code = tk.Label(out_frame, text='', font=FONT_MAIN)
state_code['bg'] = '#fff'
state_code.pack()

temperature = tk.Label(out_frame, text='', font=FONT_MAIN)
temperature['bg'] = '#fff'
temperature.pack()

description = tk.Label(out_frame, text='', font=FONT_MAIN)
description['bg'] = '#fff'
description.pack()


app.mainloop()
