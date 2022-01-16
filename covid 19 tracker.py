import json
import tkinter as tk
import requests
import datetime
#Extract the info from the api
def getCovidReport():
    api= "https://disease.sh/v3/covid-19/all"
    json_data= requests.get(api).json()
    total_cases= str(json_data['cases'])
    total_deaths= str(json_data["deaths"])
    today_cases= str(json_data["todayCases"])
    today_deaths= str(json_data["todayDeaths"])
    today_recovered= str(json_data["todayRecovered"])
    updated_at = json_data["updated"]
    date= datetime.datetime.fromtimestamp(updated_at/1e3)
    label.config(text= "Total Cases: "+total_cases + "\n"
    +"Total Deaths: "+ total_deaths + "\n"
    +"Today\'s Cases: "+ today_cases + "\n"
    +"Today\'s Deaths:" + today_deaths + "\n"
    +"Today\'s Recovery:" + today_recovered
    )
#Setting up the GUI Canvas    
canvas= tk.Tk()
canvas.geometry("460x360")
canvas.title("Covid-19 Tracker Application")

f = ("Helvetica", 20, "bold")

button = tk.Button(canvas, font = f, text= "Load",command= getCovidReport)
button.pack(pady= 20)

label = tk.Label(canvas,font=f)
label.pack(pady=20)

label2=tk.Label(canvas,font=9)
label2.pack()
getCovidReport()

canvas.mainloop()