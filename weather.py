import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # ✅ Required import
#import requests
#city_name="jodhpur"
#data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=cca1b7bd59fe56f9b341ee2b84bb5865").json()
#print(data)

import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=cca1b7bd59fe56f9b341ee2b84bb5865").json()
    label1.config(text=data["weather"][0]["main"])
    label2.config(text=data["weather"][0]["description"])
    label3.config(text=str(int(data["main"]["temp"]-273.15)))
    label4.config(text=data["main"]["pressure"])
   
window=tk.Tk()
window.title("weather App") 
window.geometry("500x700")


bg_image = Image.open("cli.jpg")
bg_image = bg_image.resize((500, 700))  # Resize to match window size
bg_photo = ImageTk.PhotoImage(bg_image)

# Create canvas and set image as background
canvas = tk.Canvas(window, width=500, height=700)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")


label=tk.Label(window,text="WEATHER APP",font=("Time New Roman",15,"bold"),fg="black",bg="mint cream")  # White text, no box
label.place(x=30, y=50,height=50,width=400)  


list_name = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir",
    "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
    "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands",
    "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep",
    "National Capital Territory of Delhi", "Puducherry"
]

city_name = tk.StringVar()
combo = ttk.Combobox(window, values=list_name, font=("Times New Roman", 15, "bold"), state="normal", textvariable=city_name,)
combo.place(x=30, y=120, height=50, width=400)

button=tk.Button(window,text="Done",font=("Times New Roman", 15, "bold"),command=data_get)
button.place(y=190,height=50,width=100,x=200)
 

label=tk.Label(window,text="Weather Climate",font=("Time New Roman",13,"bold"))
label.place(x=25, y=260,height=50,width=210)          
label1=tk.Label(window,text=" ",font=("Time New Roman",13,"bold"))
label1.place(x=250,y=260,height=50,width=210)  


label=tk.Label(window,text="Weather Description",font=("Time New Roman",13,"bold"))
label.place(x=25, y=330,height=50,width=210)
label2=tk.Label(window,text=" ",font=("Time New Roman",13,"bold"))
label2.place(x=250,y=330,height=50,width=210)    

label=tk.Label(window,text="Weather Temperature",font=("Time New Roman",13,"bold"))
label.place(x=25, y=400,height=50,width=210) 
label3=tk.Label(window,text=" ",font=("Time New Roman",13,"bold"))
label3.place(x=250,y=400,height=50,width=210)   

label=tk.Label(window,text="Pressure",font=("Time New Roman",13,"bold"))
label.place(x=25, y=470,height=50,width=210)  
label4=tk.Label(window,text=" ",font=("Time New Roman",13,"bold"))
label4.place(x=250,y=470,height=50,width=210)  







window.mainloop()