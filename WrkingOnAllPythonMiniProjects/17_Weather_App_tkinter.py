import tkinter as tk
import requests

class WeatherApp:
    def __init__(self):
        self.api_key = "YOUR_API_KEY"
        self.root = tk.Tk()
        self.root.title("Weather App")

        self.city_label = tk.Label(self.root, text="City:")
        self.city_label.grid(row=0, column=0)

        self.city_entry = tk.Entry(self.root, width=30)
        self.city_entry.grid(row=0, column=1)

        self.submit_button = tk.Button(self.root, text="Get Weather", command=self.get_weather)
        self.submit_button.grid(row=0, column=2)

        self.weather_label = tk.Label(self.root, text="")
        self.weather_label.grid(row=1, column=0, columnspan=3)

    def get_weather(self):
        city = self.city_entry.get()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        try:
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"].capitalize()
            message = f"The temperature in {city} is {temperature:.1f}°C and the weather is {description}."
        except KeyError:
            message = f"Could not find weather information for {city}."
        self.weather_label.config(text=message)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = WeatherApp()
    app.run()
