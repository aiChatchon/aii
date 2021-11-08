from tkinter import *
from tkinter.ttk import *
import pandas as pd
country=['United States of America', "People's Republic of China", 'Japan', 'Great Britain', 'ROC', 'Australia', 'Netherlands', 'France', 'Germany', 'Italy', 'Canada', 'Brazil', 'New Zealand', 'Cuba', 'Hungary', 'Republic of Korea', 'Poland', 'Czech Republic', 'Kenya', 'Norway', 'Jamaica', 'Spain', 'Sweden', 'Switzerland', 'Denmark', 'Croatia', 'Islamic Republic of Iran', 'Serbia', 'Belgium', 'Bulgaria', 'Slovenia', 
'Uzbekistan', 'Georgia', 'Chinese Taipei', 'Turkey', 'Greece', 'Uganda', 'Ecuador', 'Ireland', 'Israel', 'Qatar', 'Bahamas', 'Kosovo', 'Ukraine', 'Belarus', 'Romania', 'Venezuela', 'India', 'Hong Kong, China', 'Philippines', 'Slovakia', 'South Africa', 'Austria', 'Egypt', 'Indonesia', 'Ethiopia', 'Portugal', 'Tunisia', 'Estonia', 'Fiji', 'Latvia', 'Thailand', 'Bermuda', 'Morocco', 'Puerto Rico', 'Colombia', 'Azerbaijan', 'Dominican Republic', 'Armenia', 'Kyrgyzstan', 'Mongolia', 'Argentina', 'San Marino', 'Jordan', 'Malaysia', 'Nigeria', 'Bahrain', 'Saudi Arabia', 'Lithuania', 'North Macedonia', 'Namibia', 'Turkmenistan', 'Kazakhstan', 'Mexico', 'Finland', 'Botswana', 'Burkina Faso', "Côte d'Ivoire", 'Ghana', 'Grenada', 'Kuwait', 'Republic of Moldova', 'Syrian Arab Republic']
x=0
all=0
df=pd.read_csv("Medals.csv")
#Gold medals
for i in df.index:
    x+=df["Gold"].loc[i]
gold_amount=("There are ")+str(x)+(" Gold medals.")
#all medals
for i in df.index:
    all=all+df["Gold"].loc[i]+df["Silver"].loc[i]+df["Bronze"].loc[i]
all_amount=("There are ")+str(all)+(" medals.")
#country/medals
def find(): 
    g_am=0   
    s_am=0
    b_am=0
    for i in df.index:
        if df["Team/NOC"].loc[i]==dropbox.get():
                g_am=g_am+df["Gold"].loc[i]
                s_am=s_am+df["Silver"].loc[i]
                b_am=b_am+df["Bronze"].loc[i]
                val_med1.configure(text=g_am)
                val_med2.configure(text=s_am)
                val_med3.configure(text=b_am)
window=Tk()
window.title("Medals")
window.geometry("400x400")
gold=Label(window,text=gold_amount)
allme=Label(window,text=all_amount)
findmed=Label(window,text=("How many medals does this country get?"))
dropbox=Combobox(window)
dropbox["values"]=['United States of America', "People's Republic of China", 'Japan', 'Great Britain', 'ROC', 'Australia', 'Netherlands', 'France', 'Germany', 'Italy', 'Canada', 'Brazil', 'New Zealand', 'Cuba', 'Hungary', 'Republic of Korea', 'Poland', 'Czech Republic', 'Kenya', 'Norway', 'Jamaica', 'Spain', 'Sweden', 'Switzerland', 'Denmark', 'Croatia', 'Islamic Republic of Iran', 'Serbia', 'Belgium', 'Bulgaria', 'Slovenia', 
'Uzbekistan', 'Georgia', 'Chinese Taipei', 'Turkey', 'Greece', 'Uganda', 'Ecuador', 'Ireland', 'Israel', 'Qatar', 'Bahamas', 'Kosovo', 'Ukraine', 'Belarus', 'Romania', 'Venezuela', 'India', 'Hong Kong, China', 'Philippines', 'Slovakia', 'South Africa', 'Austria', 'Egypt', 'Indonesia', 'Ethiopia', 'Portugal', 'Tunisia', 'Estonia', 'Fiji', 'Latvia', 'Thailand', 'Bermuda', 'Morocco', 'Puerto Rico', 'Colombia', 'Azerbaijan', 'Dominican Republic', 'Armenia', 'Kyrgyzstan', 'Mongolia', 'Argentina', 'San Marino', 'Jordan', 'Malaysia', 'Nigeria', 'Bahrain', 'Saudi Arabia', 'Lithuania', 'North Macedonia', 'Namibia', 'Turkmenistan', 'Kazakhstan', 'Mexico', 'Finland', 'Botswana', 'Burkina Faso', "Côte d'Ivoire", 'Ghana', 'Grenada', 'Kuwait', 'Republic of Moldova', 'Syrian Arab Republic']
dropbox.current(0)
med1=Label(window,text=("Gold(s)"))
med2=Label(window,text=("Silver(s)"))
med3=Label(window,text=("Bronze(s)"))
val_med1=Label(window,text=("0"))
val_med2=Label(window,text=("0"))
val_med3=Label(window,text=("0"))
                
bt=Button(window,text="Enter",command=find)


med1.grid(column=0,row=3)
med2.grid(column=1,row=3)
med3.grid(column=2,row=3)
val_med1.grid(column=0,row=4)
val_med2.grid(column=1,row=4)
val_med3.grid(column=2,row=4)
bt.grid(column=2,row=2)
findmed.grid(column=1,row=2)
dropbox.grid(column=0,row=2)
gold.grid(column=0,row=0)
allme.grid(column=0,row=1)
window.mainloop()