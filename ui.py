import tkinter as tk
from tkinter import ttk, messagebox
from weather_api import fetch_weather, fetch_forecast
from utils import plot_forecast
import threading

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather APP")
        self.root.config(bg='lightblue')
        self.root.geometry("700x800")

        self.city_list = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"]
        
        self.history = []
        self.favorites = []

        self.create_widgets()

    def create_widgets(self):
        name_label = tk.Label(self.root, text='WEATHER APP', font=("Time New Roman", 40, "bold"), bg='lightblue')
        name_label.place(x=125, y=20, height=50, width=450)

        self.com = ttk.Combobox(self.root, font=("Time New Roman", 20, "bold"), values=self.city_list)
        self.com.place(x=50, y=100, height=50, width=400)

        done_button = tk.Button(self.root, text='Get Weather', font=("Time New Roman", 16, "bold"), command=self.fetch_weather)
        done_button.place(x=500, y=100, height=50, width=150)

        history_button = tk.Button(self.root, text='History', font=("Time New Roman", 20, "bold"), command=self.show_history)
        history_button.place(x=50, y=170, height=40, width=150)

        favorites_button = tk.Button(self.root, text='Favorites', font=("Time New Roman", 20, "bold"), command=self.show_favorites)
        favorites_button.place(x=250, y=170, height=40, width=150)

        self.loading_label = tk.Label(self.root, text='', font=("Time New Roman", 12), bg='lightblue')
        self.loading_label.place(x=300, y=210, height=40, width=100)

        labels = {
            'Weather Climate': (260, 'w_label1'),
            'Weather Description': (330, 'wb_label1'),
            'Temperature': (400, 'temp_label1'),
            'Pressure': (470, 'press_label1'),
            'Humidity': (540, 'humidity_label1'),
            'Wind Speed': (610, 'wind_label1')
        }

        self.label_vars = {}
        for text, (y, var_name) in labels.items():
            label = tk.Label(self.root, text=text, font=("Time New Roman", 16), bg='lightblue')
            label.place(x=25, y=y, height=50, width=210)
            self.label_vars[var_name] = tk.Label(self.root, text='', font=("Time New Roman", 16), bg='lightblue')
            self.label_vars[var_name].place(x=250, y=y, height=50, width=200)

        forecast_button = tk.Button(self.root, text='Show Forecast', font=("Time New Roman", 20, "bold"), command=self.show_forecast)
        forecast_button.place(x=250, y=680, height=50, width=200)

    def fetch_weather(self):
        threading.Thread(target=self.get_weather).start()

    def get_weather(self):
        city = self.com.get()
        if not city:
            messagebox.showerror("Input Error", "Please select a city")
            return
        
        self.loading_label.config(text="Loading...")
        data = fetch_weather(city)
        
        if "error" in data:
            messagebox.showerror("Error", data["error"])
        elif data["cod"] != "404":
            main = data["main"]
            weather = data["weather"][0]
            wind = data["wind"]
            
            self.label_vars['w_label1'].config(text=weather["main"])
            self.label_vars['wb_label1'].config(text=weather["description"])
            self.label_vars['temp_label1'].config(text=f"{main['temp']} °C")
            self.label_vars['press_label1'].config(text=f"{main['pressure']} hPa")
            self.label_vars['humidity_label1'].config(text=f"{main['humidity']} %")
            self.label_vars['wind_label1'].config(text=f"{wind['speed']} m/s")

            self.history.append(city)
            if city not in self.favorites:
                self.favorites.append(city)
        else:
            messagebox.showerror("Error", "City Not Found")
        self.loading_label.config(text="")

    def show_history(self):
        history_win = tk.Toplevel(self.root)
        history_win.title("Search History")
        history_win.geometry("300x400")
        tk.Label(history_win, text="Search History", font=("Time New Roman", 20, "bold")).pack()

        for city in self.history:
            tk.Label(history_win, text=city, font=("Time New Roman", 16)).pack()

    def show_favorites(self):
        favorites_win = tk.Toplevel(self.root)
        favorites_win.title("Favorites")
        favorites_win.geometry("300x400")
        tk.Label(favorites_win, text="Favorites", font=("Time New Roman", 20, "bold")).pack()

        for city in self.favorites:
            tk.Label(favorites_win, text=city, font=("Time New Roman", 16)).pack()

    def show_forecast(self):
        city = self.com.get()
        if not city:
            messagebox.showerror("Input Error", "Please select a city")
            return

        data = fetch_forecast(city)
        if "error" in data:
            messagebox.showerror("Error", data["error"])
        elif data["cod"] != "404":
            plot_forecast(data)
            forecast_win = tk.Toplevel(self.root)
            forecast_win.title("5-Day Forecast")
            forecast_win.geometry("600x400")
            tk.Label(forecast_win, text="5-Day Weather Forecast", font=("Time New Roman", 20, "bold")).pack()
            img = tk.PhotoImage(file='forecast.png')
            tk.Label(forecast_win, image=img).pack()
            forecast_win.mainloop()
        else:
            messagebox.showerror("Error", "City Not Found")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

