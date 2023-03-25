from tkinter import *
import os
from bs4 import BeautifulSoup
import requests
from PIL import ImageTk, Image
import glob
import tkinter as tk
from tkinter import messagebox
import pyautogui
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import tkinter.font as tf
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random

# Set up the Google Sheets API credentials
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
json = 'fourth-way-369505-c550bf5ca587.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json, scope)
gc = gspread.authorize(credentials)
sheet_url = 'https://docs.google.com/spreadsheets/d/18vaU1FjN1kBWtRRdoRjOz_jW5eUkZxKk4fiTJ49d7VM/edit#gid=0'
doc = gc.open_by_url(sheet_url)
librarysheet = doc.worksheet('Studentlist')
studentname_list = librarysheet.col_values(1)
studentnumber_list = librarysheet.col_values(3)
password_list = librarysheet.col_values(4)
#이름 없을때 기본 설정 (에러 방지용)
studentindex = 0
# Set up the GUI
window = Tk()
window.title('헤이븐 도서 대출')
bc="#FFFFF0"
bbg="#E6D2B5"
window.geometry("1100x600")
# Add a book loan
frame2=Frame(window, relief="solid", height=1100, width=600)
frame7=Frame(window, relief="solid", height=1100, width=600)
frame8=Frame(window, relief="solid", height=1100, width=600)
frame9=Frame(window, relief="solid", height=1100, width=600)
def openmypage():
    frame2.pack_forget()
    frame8.pack_forget()
    frame9.pack_forget()   
    frame7.pack()
    usertitle = Label(frame7,bg=bc,text="안녕하세요, "+studentname_list[studentindex]+" 님",font=(tf.Font(family="맑은 고딕", size=31)))
    usertitle.place(x=20,y=190)
def open2():
    frame7.pack_forget()
    frame8.pack_forget()
    frame9.pack_forget()
    frame2.pack()
def autherror():
     messagebox.showinfo("오류","학번 또는 비밀번호가 다릅니다. 다시 시도하세요")

def submit():
    global studentindex
    stn = studentnumber.get()
    pw = password.get()
    try:
        if  stn in studentnumber_list:
            studentindex = studentnumber_list.index(stn)
            if pw == password_list[studentindex]:
                openmypage()
            else:
                autherror()
        else: 
            autherror()
    except IndexError or ValueError:
        autherror()
    
def clearentry():
    studentnumber.delete(0,'end')
    password.delete(0,'end')

authtitle = Label(frame2,bg=bc,text="이름과 학번을 입력하여 주세요:",font=(tf.Font(family="맑은 고딕", size=31)))
authtitle.place(x=20,y=190)
studentnumber = Entry(frame2,font=(tf.Font(family="맑은 고딕",size=31)))
studentnumber.place(x=20,y=0,width=1040,height=100)
password = Entry(frame2,font=(tf.Font(family="맑은 고딕",size=31)))
password.place(x=20,y=200,width=1040,height=100)

submitbutton=Button(frame2, text='제출',bg='brown',fg='white',font=(tf.Font(family="맑은 고딕", size=31)),command=submit)
submitbutton.place(x=0,y=400,width=300,height=120)

clearbutton=Button(frame2, text='초기화',bg='black',fg='white',font=(tf.Font(family="맑은 고딕", size=31)),command=clearentry)
clearbutton.place(x=160,y=400,width=300,height=120)


# Start the GUI
open2()
window.mainloop()
