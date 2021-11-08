from tkinter import *
from tkinter.ttk import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv("chess_games.csv")
quest=["Common openings","Games result","Player ratings","Rating gap","Victory status"]
tid=["white_id","black_id"]
x=0
allid=[]
for i in range(2):
    for j in df.index:
        if (df[tid[i]][j]) not in allid:
            allid.append(df[tid[i]][j])


sample=df[["winner","white_rating","black_rating"]]
sample["white higher"]=(sample["white_rating"] > sample["black_rating"])
sample["high_rank win"]=df["turns"]
for i in sample.index:
    if sample["winner"].loc[i]=="White" and sample["white higher"].loc[i]== True:
        sample["high_rank win"].loc[i]=True
    elif sample["winner"].loc[i]=="Black" and sample["white higher"].loc[i]== False:
        sample["high_rank win"].loc[i]=True
    else:
        sample["high_rank win"].loc[i]=False
window=Tk()
window.title("Chess data")
window.geometry("400x400")
task=Combobox(window)
task["values"]=quest
task.current(0)
playerbox=Combobox(window)
def graph():
    if task.get()=="Games result":
        pie_labels=["White","Black","Draw"]
        pct_gameres=df['winner'].value_counts(normalize=True)
        plt.title("Result of games")
        plt.pie(pct_gameres,labels=pie_labels, autopct='%1.0f%%')
        plt.show()
    if task.get()=="Common openings":
        opening=df["opening_shortname"].value_counts().nlargest(5)
        plt.title("Most common openings")
        plt.xlabel("Games")
        plt.barh(opening.keys(),opening.values,)
        plt.show()
    if task.get()=="Rating gap":
        pie_labels2=["High rank won", "Low rank won"]
        plt.title("High rank vs low rank")
        plt.pie(sample["high_rank win"].value_counts(),labels=pie_labels2,autopct='%1.0f%%')
        plt.show()
    if task.get()=="Player ratings":
      
        global Wgame,W_id,Bgame,B_id,x
        playerbox["values"]=allid
        playerbox.current(0)
        playerbox.grid(column=0,row=1)    
        playerbt=Button(window,text="Track",command=track)
        playerbt.grid(column=1,row=1)
        if x==0:
            Wlab=Label(window,text="Games as white")
            Blab=Label(window,text="Games as black")
            W_winlab=Label(window,text="W-L")
            B_winlab=Label(window,text="W-L")
            Wlab.grid(column=0,row=3)
            Blab.grid(column=2,row=3)
            W_winlab.grid(column=0,row=6)
            B_winlab.grid(column=2,row=6)
            Wgame=Label(window,text=" ")
            Wgame.grid(column=0,row=4)
            W_id=Label(window,text=" ")
            W_id.grid(column=0,row=5)
            Bgame=Label(window,text=" ")
            Bgame.grid(column=2,row=4)
            B_id=Label(window,text=" ")
            B_id.grid(column=2,row=5)
            x+=1
    if task.get()=="Victory status":
        pie_labels3=["Resign","Mate","Out of time","Draw"]
        pct_vst=df['victory_status'].value_counts(normalize=True)
        plt.title("How games ended")
        plt.pie(pct_vst,labels=pie_labels3, autopct='%1.0f%%')
        plt.show()
def track():
    Res_W=[]
    WinasW=[]
    LossasW=[]
    Res_B=[]
    WinasB=[]
    LossasB=[]
    gameidasW=(df.loc[df["white_id"]==playerbox.get()].game_id.values)
    gameidasB=(df.loc[df["black_id"]==playerbox.get()].game_id.values)
    Wgame.configure(text=len(gameidasW))
    Bgame.configure(text=len(gameidasB))
    W_id.configure(text=gameidasW)
    B_id.configure(text=gameidasB)






#display win and lost
#display win game and lost game id
#track each player's ratings with graph
#rated
        





graphbt=Button(window,text="Graph",command=graph)





graphbt.grid(column=1,row=0)
task.grid(column=0,row=0)
window.mainloop()