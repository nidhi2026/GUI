import tkinter as tk
import requests

root = tk.Tk()
root.title("Weather Report")

### FROMATTING THE WEATHER REPORT
def format_response(weather):
  try:
    city = weather['name']
    temp = weather['main']['temp']
    desc = weather['weather'][0]['description']
    result = ' WEATHER REPORT\n\n City: %s \n Temperature: %s°C \n Condition: %s \n'%(city, temp, desc)
  except:
    result = 'Something went wrong \nMaybe you mistyped'
  return result
  

### GETTING WEATHER REPORT USING API
def get_weather(city):
  weather_key = 'a3386ef3375a83ad0a2fb46f6065648c'
  url = 'https://api.openweathermap.org/data/2.5/weather'
  params = {'APPID': weather_key, 'q':city, 'units': 'metric'}
  response = requests.get(url, params = params)
  weather = response.json()
  display_label['text'] = format_response(weather)
  
### CANVAS
canvas_height=200
canvas_width=300
canvas = tk.Canvas(root, width= canvas_width, height=canvas_height)
canvas.pack()

### BACKGROUNG IMAGE
background_image = tk.PhotoImage(file = 'landscape.png')
background = tk.Label(root, image = background_image)
background.place(relwidth=1, relheight=1)

### FRAMES
# ENTRY FRAME
entry_frame = tk.Frame(root, bg = '#66e0ff')
entry_frame.place(relx=0.1, rely=0.15, relheight=0.2, relwidth=0.5)
entry = tk.Entry(entry_frame, font= ('DejaVu Serif', 25))
entry.place(relx=0.025, rely=0.1, relheight=0.8, relwidth=0.9)

# BUTTON FRAME
button_frame = tk.Frame(root, bg = '#66e0ff')
button_frame.place(relx=0.55, rely = 0.15, relwidth=0.25, relheight=0.2)
button = tk.Button(button_frame, text="Get Weather", command=lambda: get_weather(entry.get()), font=100)
button.place(relx=0.05, rely=0.1, relheight=0.8, relwidth=0.9)

# DISPLAY FRAME
display_frame = tk.Frame(root, bg = '#66e0ff')
display_frame.place(relx=0.1, rely = 0.45, relheight = 0.5, relwidth = 0.7)
display_label = tk.Label(display_frame, bg = '#ffffff', font= ('DejaVu Serif', 20), anchor='nw', justify='left', bd=2)
display_label.place(relx=0.05, rely=0.1, relheight=0.8, relwidth=0.9)

root.mainloop()