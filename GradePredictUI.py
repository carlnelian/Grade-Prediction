import numpy as np
import pandas as pd

df = pd.read_csv('grades.csv')
df.dropna(axis=0, inplace = True)
X = df.iloc[:, 0:4].values #independent
y = df.iloc[:, 4:5].values #dependent

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(1, 5))
scaled_X = scaler.fit_transform(X)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(scaled_X,y, test_size = 0.33, random_state = 42)
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(x_train, y_train)
y_predict = classifier.predict(x_test)

#======================================================================

from tkinter import *
import os
import pandas as pd

DF = pd.DataFrame()
grades = Tk()
grades.title('Grade Prediction')
grades.resizable(False, False)
grades.geometry("500x550")
grades.configure(bg = '#285A51')

anya_pass = PhotoImage(file = r'C:\Users\Carl Astig\Documents\Programs\Grade-Prediction\anyapass.png')
anya_fail = PhotoImage(file = r'C:\Users\Carl Astig\Documents\Programs\Grade-Prediction\anyafail.png')

PrelimGrade_var = StringVar()
MidtermGrade_var = StringVar()
FQuiz_var = StringVar()
FLab_var = StringVar()
result = StringVar()
pr = IntVar()

def validate_entry(inp):
    try:
        float(inp)
    except:
        return False
    return True

def clearframe():
    for widget in result_frame.winfo_children():
        widget.destroy()
        
def action():
    global DB 
    DF = pd.DataFrame(columns=['PrelimGrade','MidtermGrade','FQuiz','FLab'])
    PrelimGrade = PrelimGrade_var.get()
    MidtermGrade = MidtermGrade_var.get()
    FQuiz = FQuiz_var.get()
    FLab = FLab_var.get()
    DF.loc[0,'PrelimGrade'] = PrelimGrade
    DF.loc[0,'MidtermGrade'] = MidtermGrade
    DF.loc[0,'FQuiz'] = FQuiz
    DF.loc[0,'FLab'] = FLab
    DB = DF
    pr = classifier.predict(DB)
    print(pr)
    if pr == 1:
        clearframe()
        er = Label(result_frame, text = "Higher probability of Passing", fg = "blue", font = ("Consolas", 20), image = anya_pass, compound = BOTTOM)
        er.pack()
    elif pr == 0:
        clearframe()
        er = Label(result_frame, text = "Higher probability of Failing", fg = "red", font = ("Consolas", 20), image = anya_fail, compound = BOTTOM)
        er.pack()
    
#=====================================================================================================================================================

top_frame = Frame(grades, bg='#B0EFEF',)
top_frame.pack(side = TOP, pady = 12, fill = X)
mid_frame = Frame(grades, bg='#285A51')
mid_frame.pack()
result_frame = Frame(grades)
result_frame.pack(side = BOTTOM, fill=X) 


lbl_title = Label(top_frame, text="Logic Circuit Design\nGrade Prediction.", font = ("Bahnschrift bold", 14), bg='#B0EFEF', fg ='#002A2A')
lbl_title.pack(fill=X)
    
lbl_instruct = Label(mid_frame, text="\nEnter the following:\n", font = ("Consolas", 12), bg='#285A51', fg ="#5A9899")
lbl_instruct.grid(row = 0, columnspan = 3)
lbl_PrelimGrade = Label(mid_frame, text="Prelim Grade: ", font = ("Consolas", 15), bg='#285A51', fg ="#D8D2CC")
lbl_PrelimGrade.grid(row = 1, sticky = W)
lbl_MidtermGrade = Label(mid_frame, text="Midterm Grade: ", font = ("Consolas", 15), bg='#285A51', fg ="#D8D2CC")
lbl_MidtermGrade.grid(row = 2, sticky = W)
lbl_FQuiz = Label(mid_frame, text="Final Quiz 1: ", font = ("Consolas", 15), bg='#285A51', fg ="#D8D2CC")
lbl_FQuiz.grid(row = 3, sticky = W)
lbl_FLab = Label(mid_frame, text="Final Lab 1: ", font = ("Consolas", 15), bg='#285A51', fg ="#D8D2CC")
lbl_FLab.grid(row = 4, sticky = W)

PrelimGrade_entry = Entry(mid_frame, textvariable = PrelimGrade_var, width=30, font = ("Calibri", 12), validate='key', vcmd = (grades.register(validate_entry), '%d', '%P', '%s'))
PrelimGrade_entry.grid(row = 1, pady=3, column = 1, sticky = W)
MidtermGrade_entry = Entry(mid_frame, textvariable = MidtermGrade_var, width=30, font = ("Calibri", 12), validate='key', vcmd = (grades.register(validate_entry), '%d', '%P', '%s'))
MidtermGrade_entry.grid(row = 2, pady=3, column = 1, sticky = W)
FQuiz_entry = Entry(mid_frame, textvariable = FQuiz_var, width=30, font = ("Calibri", 12), validate='key', vcmd = (grades.register(validate_entry), '%d', '%P', '%s'))
FQuiz_entry.grid(row = 3, pady=3, column = 1, sticky = W)
FLab_entry = Entry(mid_frame, textvariable = FLab_var, width=30, font = ("Calibri", 12), validate='key', vcmd = (grades.register(validate_entry), '%d', '%P', '%s'))
FLab_entry.grid(row = 4, pady=3, column = 1, sticky = W)
btn_predict = Button(mid_frame, text = "Predict", width = 30, font = ("Bahnschrift bold", 12), command = action)
btn_predict.grid(row = 5, columnspan = 2, pady = 20)

