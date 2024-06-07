import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import os
def plot_forecast(forecast_data):
    dates = [item['dt_txt'] for item in forecast_data['list']]
    temps = [item['main']['temp'] for item in forecast_data['list']]

    fig = go.Figure(data=go.Scatter(x=dates, y=temps, mode='lines+markers'))
    fig.update_layout(title='5-Day Weather Forecast', xaxis_title='Date', yaxis_title='Temperature (°C)') 

    # Get the current directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Define the path to save the HTML file in the same directory
    html_file_path = os.path.join(script_dir, 'forecast.html')
    fig.write_html(html_file_path)

    plt.figure(figsize=(10, 5))
    plt.plot(dates, temps, marker='o')
    plt.xticks(rotation=45)
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('5-Day Weather Forecast')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('forecast.png')
    plt.close()
