from tkinter import *
import tkinter as tk
import webbrowser
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

root=Tk()
root.title('Weather App')
root.geometry('890x470+300+200')
root.configure(bg = 'light sea green')
root.resizable(False,False)

def getWeather():
    city=textfield.get()

    geolocator= Nominatim(user_agent='geoapiExercises')
    location= geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f'{round(location.latitude,4)}°N,round{location.longitude,4}°E')

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime('%I:%M %p')
    clock.config(text=current_time)
    

#logo

image_icon=PhotoImage(file='C:/Users/Acer/Pictures/pics/logo.png')
root.iconphoto(False,image_icon)

Round_box=PhotoImage(file='C:/Users/Acer/Pictures/2.png')
Label(root,image=Round_box,bg='light sea green').place(x=30,y=110)

#label

label1=Label(root,text='Temperature',font=('Helvetica',11),fg='white',bg='black')
label1.place(x=50,y=120)

label2=Label(root,text='Humidity',font=('Helvetica',11),fg='white',bg='black')
label2.place(x=50,y=140)

label3=Label(root,text='Pressure',font=('Helvetica',11),fg='white',bg='black')
label3.place(x=50,y=160)

label4=Label(root,text='Wind Speed',font=('Helvetica',11),fg='white',bg='black')
label4.place(x=50,y=180)

label5=Label(root,text='Description',font=('Helvetica',11),fg='white',bg='black')
label5.place(x=50,y=200)

textfield=tk.Entry(root,justify='center',width=15,font=('poppins',25,'bold'),bg='black',border=0,fg='white')
textfield.place(x=450,y=130)
textfield.focus()

Search_icon=PhotoImage(file='C:/Users/Acer/Pictures/pics/cc.png')
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor='hand2',bg='black',command=getWeather)
myimage_icon.place(x=675,y=125)

#search

Search_image=PhotoImage(file='C:/Users/Acer/Pictures/Untitled.png')
myimage=Label(image=Search_image,bg='black')
myimage.place(x=350,y=120)

weat_image=PhotoImage(file='C:/Users/Acer/Pictures/pics/ccc.png')
weatherimage=Label(root,image=weat_image,bg='black')
weatherimage.place(x=370,y=127)

textfield=tk.Entry(root,justify='center',width=15,font=('poppins',25,'bold'),bg='black',border=0,fg='white')
textfield.place(x=450,y=130)
textfield.focus()

Search_icon=PhotoImage(file='C:/Users/Acer/Pictures/pics/cc.png')
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor='hand2',bg='black',command=getWeather)
myimage_icon.place(x=675,y=130)

#BOTTOM BOX

frame=Frame(root,width=900,height=180,bg='black')
frame.pack(side=BOTTOM)

#boxes

firstbox=PhotoImage(file='C:/Users/Acer/Pictures/pics/box1.png')
secondbox=PhotoImage(file='C:/Users/Acer/Pictures/pics/box2.png')
Label(frame,image=firstbox,bg='black').place(x=10,y=20)
Label(frame,image=secondbox,bg='black').place(x=285,y=30)
Label(frame,image=secondbox,bg='black').place(x=385,y=30)
Label(frame,image=secondbox,bg='black').place(x=485,y=30)
Label(frame,image=secondbox,bg='black').place(x=585,y=30)
Label(frame,image=secondbox,bg='black').place(x=685,y=30)
Label(frame,image=secondbox,bg='black').place(x=785,y=30)


#clock

clock=Label(root,font=('Helvetica',30,'bold'),fg='khaki',bg='black')
clock.place(x=30,y=20)

#timezone

timezone=Label(root,font=('Helvetica',20),fg='khaki',bg='black')
timezone.place(x=700,y=20)

long_lat=Label(root,font=('Helvetica',10),fg='khaki',bg='black')
long_lat.place(x=700,y=50)

#thpwd
t=Label(root,text='temp',font=('Helvetica',11),fg='white',bg='black')
t.place(x=150,y=120)
h=Label(root,text='temp',font=('Helvetica',11),fg='white',bg='black')
h.place(x=150,y=140)
p=Label(root,text='temp',font=('Helvetica',11),fg='white',bg='black')
p.place(x=150,y=160)
w=Label(root,text='temp',font=('Helvetica',11),fg='white',bg='black')
w.place(x=150,y=180)
d=Label(root,text='temp',font=('Helvetica',11),fg='white',bg='black')
d.place(x=150,y=200)



import webbrowser
def open_webpage():
    url = "https://www.vogue.in/culture-and-living/content/diet-tips-that-will-help-you-stay-healthy-during-the-changing-weather"  # Replace with your desired hyperlink
    webbrowser.open(url)
F_icon = PhotoImage(file='C:/Users/Acer/Pictures/pics/B.png')
myimage_icon = Button(image=F_icon, borderwidth=0, cursor='hand2', bg='black',command= open_webpage)
myimage_icon.place(x=775, y=125)

def open_webpage():
    url = "https://www.goibibo.com/"  # Replace with your desired hyperlink
    webbrowser.open(url)

A_icon = PhotoImage(file='C:/Users/Acer/Pictures/pics/n.png')
myimage_icon = Button(image=A_icon, borderwidth=0, cursor='hand2', bg='black',command=open_webpage )
myimage_icon.place(x=775, y=165)

def open_webpage():
    url = "https://brilliantmaps.com/top-100-tourist-destinations/"  # Replace with your desired hyperlink
    webbrowser.open(url)

B_icon = PhotoImage(file='C:/Users/Acer/Pictures/pics/m.png')
myimage_icon = Button(image=B_icon, borderwidth=0, cursor='hand2', bg='black',command=open_webpage )
myimage_icon.place(x=775, y=205)

firstframe=Frame(root,width=230,height=132,bg='black')
firstframe.place(x=35,y=315)
day1=Label(firstframe,font='arial 20',bg='black')
day1.place(x=10,y=5)

secondframe=Frame(root,width=70,height=115,bg='black')
secondframe.place(x=305,y=325)
day2=Label(secondframe,bg='black')
day2.place(x=10,y=5)

thirdframe=Frame(root,width=70,height=115,bg='black')
thirdframe.place(x=405,y=315)
day3=Label(thirdframe,bg='black')
day3.place(x=10,y=5)

fourthframe=Frame(root,width=70,height=115,bg='black')
fourthframe.place(x=505,y=315)
day4=Label(firstframe,bg='black')
day4.place(x=100,y=5)

fifthframe=Frame(root,width=70,height=115,bg='black')
fifthframe.place(x=605,y=315)
day5=Label(firstframe,bg='black')
day5.place(x=100,y=5)

sixthframe=Frame(root,width=70,height=115,bg='black')
sixthframe.place(x=705,y=315)
day6=Label(firstframe,bg='black')
day6.place(x=10,y=5)

seventhframe=Frame(root,width=70,height=115,bg='black')
seventhframe.place(x=905,y=315)
day7=Label(firstframe,bg='black')
day7.place(x=10,y=5)


first=datetime.now()
day1.config(text=first.strftime('%A'))

second=first+timedelta(days=1)
day2.config(text=first.strftime('%A'))

third=first+timedelta(days=2)
day3.config(text=first.strftime('%A'))

fourth=first+timedelta(days=3)
day4.config(text=first.strftime('%A'))

fifth=first+timedelta(days=4)
day5.config(text=first.strftime('%A'))

sixth=first+timedelta(days=5)
day6.config(text=first.strftime('%A'))

seventh=first+timedelta(days=6)
day7.config(text=first.strftime('%A'))
