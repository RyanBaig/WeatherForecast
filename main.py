import tkinter as tk
from tkinter import messagebox
import requests


def get_weather(city):
    api_key = '4aa5f1ba716a4b499c9120633232807'
    base_url = 'http://api.weatherapi.com/v1/current.json'

    params = {
        'key': api_key,
        'q': city
    }

    try:
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            weather_info = f"""Weather Information for {data['location']['name']}, {data['location']['country']}:\n
Current Temperature: {data['current']['temp_c']}°C ({data['current']['temp_f']}°F)\n
Feels Like: {data['current']['feelslike_c']}°C ({data['current']['feelslike_f']}°F)\n
Condition: {data['current']['condition']['text']}\n
Wind: {data['current']['wind_kph']} kph ({data['current']['wind_mph']} mph) {data['current']['wind_dir']}\n
Humidity: {data['current']['humidity']}%\n
Pressure: {data['current']['pressure_mb']} mb ({data['current']['pressure_in']} inHg)\n
Precipitation: {data['current']['precip_mm']} mm ({data['current']['precip_in']} in)\n
Cloud Cover: {data['current']['cloud']}%\n
"""

            messagebox.showinfo("Weather Information", weather_info)
        else:
            messagebox.showerror("Error", f"Failed to retrieve data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred during the API request: {str(e)}")


# Create the main Tkinter window
root = tk.Tk()
root.title("Weather Information")
root.geometry("400x350")
root.resizable(False, False)

# Custom Colors and Fonts
bg_color = "#34495e"
fg_color = "#ecf0f1"
font_family = "Helvetica"
font_size_heading = 18
font_size_label = 12
font_size_entry = 12
font_size_button = 12

# Set the background color for the entire window
root.config(bg=bg_color)

# Create widgets
heading_label = tk.Label(root, text="Weather Information", font=(font_family, font_size_heading), fg=fg_color,
                         bg=bg_color)
label_city = tk.Label(root, text="Enter City:", font=(font_family, font_size_label), fg=fg_color, bg=bg_color)
entry_city = tk.Entry(root, font=(font_family, font_size_entry), bg=bg_color, bd=0, fg=fg_color)
button_get_weather = tk.Button(root, text="Get Weather", font=(font_family, font_size_button), bg="#3498db",
                               fg=fg_color,
                               activebackground="#2980b9", relief=tk.FLAT, command=lambda: get_weather(entry_city.get()))
icon_label = tk.Label(root, bg=bg_color)

# Grid layout (center-aligned)
heading_label.grid(row=0, column=0, columnspan=2, padx=20, pady=(30, 10), sticky="ew")
label_city.grid(row=1, column=0, padx=20, pady=5, sticky="e")
entry_city.grid(row=1, column=1, padx=20, pady=5, sticky="ew")
button_get_weather.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

# Set focus to the entry widget when the window opens
root.bind("<Map>", lambda event: entry_city.focus_set())

# Bind the return key to get_weather
root.bind("<Return>", lambda event: get_weather(entry_city.get()))

# Start the Tkinter event loop
root.mainloop()
