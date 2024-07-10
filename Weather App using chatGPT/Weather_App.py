# import requests
# import tkinter as tk

# # Create a GUI window
# root = tk.Tk()
# root.title("Weather App")
# root.iconbitmap("youtube.ico")
# # root.configure(bg='black')


# # Function to get weather information
# def get_weather():
#     # Get the city name from the user
#     city = city_entry.get()

#     # API URL and parameters
#     url = "http://api.openweathermap.org/data/2.5/weather"
#     params = {"q": city, "appid": "0ffac5f006a04cf23ea30e9488a59775", "units": "metric"}

#     # Send a GET request to the API and get the response
#     response = requests.get(url, params=params)

#     # Check if the request was successful
#     if response.status_code == 200:
#         # Parse the JSON data
#         data = response.json()

#         # Update the weather information labels
#         weather_label.config(text="Weather: " + data["weather"][0]["main"])
#         temp_label.config(text="Temperature: " + str(data["main"]["temp"]) + "°C")
#         desc_label.config(text="Description: " + data["weather"][0]["description"])
#     else:
#         # Display an error message
#         weather_label.config(text="Error: Could not retrieve weather information")


# # Create widgets
# city_label = tk.Label(root, text="Enter city name:")
# city_entry = tk.Entry(root)
# weather_label = tk.Label(root, text="")
# temp_label = tk.Label(root, text="")
# desc_label = tk.Label(root, text="")
# get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
# # get_weather_button = tk.Button(root, text="Get Weather")

# # Pack all the widgets
# city_label.pack()
# city_entry.pack()
# get_weather_button.pack()
# weather_label.pack()
# temp_label.pack()
# desc_label.pack()


# # Run the GUI loop
# root.mainloop()

import tkinter as tk
import requests
import json

root = tk.Tk()
root.title("Weather App")

def get_weather():
    city = entry.get()
    api_key = "0ffac5f006a04cf23ea30e9488a59775"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = json.loads(response.text)
    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    formatted_temp = f"{temp:.1f} °C"
    label.config(text=f"{city}: {weather}, {formatted_temp}")

label = tk.Label(root, text="Enter a city:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Get Weather", command=get_weather)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()