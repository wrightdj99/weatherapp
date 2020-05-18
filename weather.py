import tkinter as tk
import requests
HEIGHT = 500
WIDTH = 500

def test_function(entry):
    print('This is the entry: ', entry)

def format_response(weather):
    try:
            name = weather['name']
            description = weather['weather'][0]['description']
            temp = weather['main']['temp']
            feels_like_temp = weather['main']['feels_like']

            final_str = 'Location: %s \nConditions: %s \nTemperature (°F): %s \nFeels Like (°F): %s \n' % (name, description, temp, feels_like_temp)
    except:
            final_str = 'Sorry, we could not get weather for that location.'
    
    return final_str
#95a1c4093c6e57482e9778f967ab2b75
#api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}
def get_weather(city):
    weather_key = '95a1c4093c6e57482e9778f967ab2b75'
    url = 'http://api.openweathermap.org/data/2.5/weather?'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)



#Setting up the whole window and making it gray
root = tk.Tk( )
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#ccffcc')
canvas.pack()

#Creating the frame in which everything will really be shown
frame = tk.Frame(root, bg='#00cc66', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

#Making a search field
entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

#Making a button, also we have a lambda instance here
button = tk.Button(frame, text="Get Weather", bg='gray', fg='green', command=lambda: get_weather(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

#Making the output frame
lower_frame = tk.Frame(root, bg='#00cc66', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

#Making a label
label = tk.Label(lower_frame, bg='#ffff66')
label.place(relwidth=1, relheight=1)



root.mainloop( )


#FEATURES TO KEEP ADDING:

#Setting a background image
# background_image = tk.PhotoImage(file = 'forest.png')
# background_label = tk.Label(root, image=background_image)
# background_label.place(relwidth=1, relheight=1)

#Adding in a radar map
