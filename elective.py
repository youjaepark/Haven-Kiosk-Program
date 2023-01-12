#모듈 import
from tkinter import *
import os
import urllib.request
import shutil
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

#사진 업데이트
def lunchmenuupdate():
    lunchmenu_url = requests.get("https://haven.or.kr/%ec%a0%90%ec%8b%ac%ec%8b%9d%eb%8b%a8%ed%91%9c/")

    # Parse the HTML content
    lunchmenu_url_parse = BeautifulSoup(lunchmenu_url.text, "html.parser")
    recent_lunchmenu_loc = lunchmenu_url_parse.find_all("td", {"class": "kboard-list-title"})[1]
    lunchmenu_url_recent= "https://haven.or.kr"+recent_lunchmenu_loc.find("a")["href"]


    # Navigate to the latest post
    lunchmenu_url = requests.get(lunchmenu_url_recent)
    # Parse the HTML content of the latest post
    lunchmenu_url_parse = BeautifulSoup(lunchmenu_url.text, "html.parser")

    # Find the image in the latest post
    lchimage = lunchmenu_url_parse.find_all("img")[1]
    image_url = lchimage["src"]

    # Download the image
    recent_lunchmenu_image = requests.get(image_url)

    # Save the image to a local file
    with open("recentlunchmenu.jpg", "wb") as f:
        f.write(recent_lunchmenu_image.content)

def schoolphotoupdate():
    schoolphoto_url = requests.get("https://haven.or.kr/school-life/%ec%82%ac%ec%a7%84/")

    # Parse the HTML content
    schoolphoto_url_parse = BeautifulSoup(schoolphoto_url.text, "html.parser")
    recent_schoolphoto_loc = schoolphoto_url_parse.find("li", {"class": "kboard-list-item"})
    schoolphoto_url_recent= "https://haven.or.kr"+recent_schoolphoto_loc.find("a")["href"]

    # Directory to save the images to
    save_dir = "imgsamples"

    #image clear
    for f in os.listdir(save_dir):
        os.remove(os.path.join(save_dir, f))

    # Make sure the directory exists
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Download the webpage
    schoolphoto_url_recent_html = urllib.request.urlopen(schoolphoto_url_recent)
    html = schoolphoto_url_recent_html.read()

    # Parse the HTML
    schoolphoto_url_parse = BeautifulSoup(html, "html.parser")

    # Find all image tags
    images = schoolphoto_url_parse.find_all("img")

    # Download the images
    for phimage in images:
        # Get the image URL
        img_url = phimage["src"]
        # Open the image URL
        with urllib.request.urlopen(img_url) as schoolphoto_url_recent:
            # Get the image file name
            file_name = os.path.basename(img_url)
            # Open a file to save the image to
            with open(os.path.join(save_dir, file_name), "wb") as f:
                # Use shutil to copy the image from the URL to the file
                shutil.copyfileobj(schoolphoto_url_recent, f)

def noticeupdate():
    notice_url = requests.get("https://haven.or.kr/school-notice/%ea%b0%80%ec%a0%95%ed%86%b5%ec%8b%a0%eb%ac%b8/")

    # Parse the HTML content
    notice_url_parse = BeautifulSoup(notice_url.text, "html.parser")

    # Find the second item in the list of "td" elements with class "kboard-list-title"
    recent_notice_loc = notice_url_parse.find_all("td", {"class": "kboard-list-title"})[1]

    # Extract the value of the "href" attribute from the "a" element
    notice_url_recent = "https://haven.or.kr" + recent_notice_loc.find("a")["href"]

    # Navigate to the latest post
    notice_url = requests.get(notice_url_recent)

    # Parse the HTML content of the latest post
    notice_url_parse = BeautifulSoup(notice_url.text, "html.parser")

    # Find the second and third images in the latest post
    image1 = notice_url_parse.find_all("img")[1]
    image2 = notice_url_parse.find_all("img")[2]

    # Extract the value of the "src" attribute from each image
    image_url1 = "https://haven.or.kr"+image1["src"]
    image_url2 = "https://haven.or.kr"+image2["src"]

    # Download the images
    recent_lunchmenu_image1 = requests.get(image_url1)
    recent_lunchmenu_image2 = requests.get(image_url2)

    # Save the images to local files
    with open("notice1.jpg", "wb") as f:
        f.write(recent_lunchmenu_image1.content)
    with open("notice2.jpg", "wb") as f:
        f.write(recent_lunchmenu_image2.content)   

lunchmenuupdate()
schoolphotoupdate()
noticeupdate()

#gui 생성
bc="#FFFFF0"
bbg="#E6D2B5"
wd=1080
ht=1440
window = Tk()
window.title("헤이븐 키오스크")
window.configure(bg=bc)
window.resizable(True, True)
window.attributes('-fullscreen',True)

#프레임 생성
frame1=tk.Frame(window, relief="solid", height=ht, width=wd)
frame2=tk.Frame(window, relief="solid", height=ht, width=wd)
frame3=tk.Frame(window, relief="solid", height=ht, width=wd,bg=bc,borderwidth=2)
frame4=tk.Frame(window, relief="solid", height=ht, width=wd)
frame5=tk.Frame(window, relief="solid", height=ht, width=wd)
frame6=tk.Frame(window, relief="solid", height=ht, width=wd)
#화면 전환
def open1():
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()
    frame1.pack()

def open2():
    frame1.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()
    frame2.pack()

def open3():
    frame1.pack_forget()
    frame2.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()
    frame3.pack()

def open4():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()
    frame4.pack()

def open5():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame6.pack_forget()
    frame5.pack()

def open6():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    frame6.pack()

#이메일 기본 설정
email_sender = 'havenkiosk.counseling@gmail.com'
email_password = 'pblrjphidixgfxyi'
email_receiver_teacher1 = 'haeyang.lee@haven.or.kr'
email_receiver_teacher2 = 'shawn.shim@haven.or.kr'
date=datetime.today().strftime("%Y/%m/%d")

name_entry=StringVar()
wanttime = StringVar()
wanttime2= StringVar()
c=StringVar()
monday= StringVar()
tuesday= StringVar()
wednesday= StringVar()
thursday= StringVar()
friday= StringVar()
reason_entry=StringVar()
teacher = StringVar() 
list1 = ['Praise','Love','Purity','Truth','Light','Wisdom','Grace','Hope','Joy','Victory','Charity','Honor','Honesty','Glory']
#에러메세지
def error():
   messagebox.showinfo("오류","모든 입력란을 채워주세요.")

def clearentry():
   name_entry.delete(0,'end')
   reason_entry.delete(0,'end')
   teacherselect2.deselect()
   teacherselect1.select()
   mondaybox.deselect()
   tuesdaybox.deselect()
   wednesdaybox.deselect()
   thursdaybox.deselect()
   fridaybox.deselect()
   wanttime1box.deselect()
   wanttime2box.deselect()
   c.set('반을 선택하세요')
#전송 버튼 눌렀을 때
def submit():
   wantdate=[]
   wanttimelist=[]
   name= name_entry.get()
   c1=c.get()
   monday1=monday.get()
   tuesday1=tuesday.get()
   wednesday1=wednesday.get()
   thursday1=thursday.get()
   friday1=friday.get()
   wanttime1=wanttime.get()
   wanttime21=wanttime2.get()
   reason=reason_entry.get()
   email_receiver=teacher.get()
   if monday1 !="":
      wantdate.append('월요일')
   if tuesday1 !="":
      wantdate.append('화요일')
   if wednesday1 !="":
      wantdate.append('수요일')
   if thursday1 !="":
      wantdate.append('목요일')
   if friday1 !="":
      wantdate.append('금요일')
   if wanttime1 !="":
      wanttimelist.append('수업시간')
   if wanttime21 !="":
      wanttimelist.append('방과 후')

   if name==""or c1=='반을 선택하세요'or reason=="":
      error()
   elif monday1=="" and tuesday1==""and wednesday1=="" and thursday1==""and friday1=="":
      error()
   elif wanttime1==""and wanttime21=="":
      error()
   else:
    #메일 보내기
      smtp_gmail = smtplib.SMTP('smtp.gmail.com', 587)
      smtp_gmail.ehlo()
      smtp_gmail.starttls()

      smtp_gmail.login(user=email_sender,password= email_password)
      subject = '헤이븐 상담신청'
      body= f'신청 날짜:{date} \n상담자명: {name}\n반: {c1}\n상담 희망 요일: {wantdate}\n원하는 시간대: {wanttimelist}\n상담사유: {reason}'
      em = MIMEText(body)
      em['From'] = email_sender
      em['To'] = email_sender
      em['Subject'] = subject
      smtp_gmail.sendmail(from_addr=email_sender,to_addrs=email_receiver, msg=em.as_string())
      smtp_gmail.quit()
      messagebox.showinfo("성공","상담 신청이 완료되었습니다.")
      open6()
      clearentry() 
      pyautogui.hotkey('win','ctrl','o')

    #상담 신청 창 클리어   

#급식 메뉴 화면
lunch=ImageTk.PhotoImage(Image.open('recentlunchmenu.jpg').resize((wd,ht)))
lun=Label(frame1)
lun.config(image=lunch)
lun.pack()
#학교 소개 화면
intro=ImageTk.PhotoImage(Image.open('introduce.jpg').resize((wd,ht)))
tro=Label(frame2)
tro.config(image=intro)
tro.pack()
#상담 신청 화면
Label(frame3,bg=bc,text="헤이븐 상담신청",font=(tf.Font(family="맑은 고딕", size=55))).place(x=60,y=0)
Label(frame3,bg=bc,text="이름:",font=(tf.Font(family="맑은 고딕", size=31))).place(x=20,y=190)
Label(frame3, text="반:",font=(tf.Font(family="맑은 고딕", size=31)),bg=bc).place(x=90,y=300)
Label(frame3, text="상담받을 선생님:",font=(tf.Font(family="맑은 고딕", size=31)),bg=bc).place(x=20,y=410)
Label(frame3, text="원하는 요일을 모두 선택하세요:",font=(tf.Font(family="맑은 고딕", size=31)),bg=bc).place(x=20,y=640)
Label(frame3, text="원하는 시간대를 모두 고르세요:",bg=bc,font=(tf.Font(family="맑은 고딕", size=31))).place(x=20,y=860)
Label(frame3, text="상담 사유를 적어주세요:",bg=bc,font=(tf.Font(family="맑은 고딕", size=31))).place(x=20,y=1080)

def keyboard():
   pyautogui.hotkey('win','ctrl','o')

keybotton=Button(frame3, text='⌨',bg='black',fg='white',font=(tf.Font(family="맑은 고딕", size=18)),command=keyboard)
keybotton.place(x=940,y=190)

name_entry = Entry(frame3,font=(tf.Font(family="맑은 고딕",size=31)))
name_entry.place(x=190,y=190,width=750,height=100)

droplist=OptionMenu(frame3,c, *list1)
droplist.config(bg=bbg,font=(tf.Font(family="맑은 고딕",size=28)))
c.set('반을 선택하세요',) 
droplist.place(x=190,y=300)
classlist = window.nametowidget(droplist.menuname)  
classlist.config(font=(tf.Font(family="맑은 고딕", size=28))) 

teacherselect1= Radiobutton(frame3, text="이해양 선생님",font=(tf.Font(family="맑은 고딕", size=31)),bg=bbg, value=email_receiver_teacher1,variable=teacher,indicatoron=False)
teacherselect1.select()
teacherselect1.place(x=50,y=520)
teacherselect2= Radiobutton(frame3, text="Shawn 선생님",font=(tf.Font(family="맑은 고딕", size=31)),bg=bbg, value=email_receiver_teacher2,variable=teacher,indicatoron=False)
teacherselect2.place(x=560,y=520)

mondaybox=Checkbutton(frame3, text="월",font=(tf.Font(family="맑은 고딕", size=31)),bg=bbg,width=3,variable=monday,onvalue='월요일',offvalue="",indicatoron=False)
mondaybox.deselect()
mondaybox.place(x=50,y=740)

tuesdaybox=Checkbutton(frame3, text="화",font=(tf.Font(family="맑은 고딕", size=31)),bg=bbg,width=3, variable=tuesday,onvalue='화요일',offvalue="",indicatoron=False)
tuesdaybox.deselect()
tuesdaybox.place(x=260,y=740)

wednesdaybox=Checkbutton(frame3, text="수",font=(tf.Font(family="맑은 고딕", size=31)),bg=bbg,width=3, variable=wednesday,onvalue='수요일',offvalue="",indicatoron=False)
wednesdaybox.deselect()
wednesdaybox.place(x=470,y=740)

thursdaybox=Checkbutton(frame3, text="목",font=(tf.Font(family="맑은 고딕", size=31)),bg=bbg,width=3, variable=thursday,onvalue='목요일',offvalue="",indicatoron=False)
thursdaybox.deselect()
thursdaybox.place(x=680,y=740)

fridaybox=Checkbutton(frame3, text="금",font=(tf.Font(family="맑은 고딕", size=31)),bg=bbg,width=3,variable=friday,onvalue='금요일',offvalue="",indicatoron=False)
fridaybox.deselect()
fridaybox.place(x=890,y=740)

wanttime1box=Checkbutton(frame3, text="수업시간",font=(tf.Font(family="맑은 고딕", size=31)),bg=bbg, variable=wanttime,onvalue='수업시간',offvalue="",indicatoron=False)
wanttime1box.deselect()
wanttime1box.place(x=180,y=960)

wanttime2box=Checkbutton(frame3, text="방과 후",font=(tf.Font(family="맑은 고딕", size=31)),bg=bbg,width=7,variable=wanttime2,onvalue='방과 후',offvalue="",indicatoron=False)
wanttime2box.deselect()
wanttime2box.place(x=600,y=960)

reason_entry = Entry(frame3,font=(tf.Font(family="맑은 고딕",size=31)))
reason_entry.place(x=20,y=1190,width=1040,height=100)

submitbutton=Button(frame3, text='제출',height=1,bg='brown',fg='white',font=(tf.Font(family="맑은 고딕", size=31)),command=submit)
submitbutton.place(x=620,y=1300,width=300,height=120)

clearbutton=Button(frame3, text='초기화',bg='black',fg='white',font=(tf.Font(family="맑은 고딕", size=31)),command=clearentry)
clearbutton.place(x=160,y=1300,width=300,height=120)

#학교 일정 화면
noticeimage1=ImageTk.PhotoImage(Image.open('notice1.jpg').resize((wd,ht)))
noticeimage2=ImageTk.PhotoImage(Image.open('notice2.jpg').resize((wd,ht)))
imagestate=0
image_label = tk.Label(frame4)
image_label.configure(image=noticeimage1)
image_label.pack()
def update_image():
   global imagestate    
   if imagestate== 1:
      image_label.configure(image=noticeimage2)
      imagestate=0
   else:
      image_label.configure(image=noticeimage1)
      imagestate=1


imagenextbutton = tk.Button(frame4, text="➜",pady=-10,font=(tf.Font(family="맑은 고딕", size=27)),bg='black',fg='white')
imagenextbutton.configure(command=update_image)
imagenextbutton.place(x=980, y=1367,width="100", height="75")

#만든 사람들 화면
madeby=ImageTk.PhotoImage(Image.open('madeby.jpg').resize((wd,ht)))
made=Label(frame5)
made.config(image=madeby)
made.pack()

#사진 모음 화면
jpg_files = glob.glob('.\\imgsamples\\*.jpg')
images = []
for file in jpg_files:
    img = Image.open(file)
    img = img.resize((wd,ht))
    images.append(ImageTk.PhotoImage(img))
    img.close()
label = tk.Label(frame6, image=images[0])
label.pack()

def update_image():
   global current_image
   if current_image >= len(images):
      current_image = 0
   label.config(image=images[current_image])
   current_image += 1
   label.after(3000, update_image)
current_image = 0

update_image()

#화면 전환 버튼
m=380
xxx = 55
bh=150
bw=150
by=1540

buttonfont=(tf.Font(family="카페 24 써라운드",weight="bold",size=13))
Btn_take1=Button(window,relief="solid",borderwidth=4,fg="black",bg=bbg,text="급식메뉴",font=buttonfont, command=lambda:open1()).place(x=xxx, y=by,width=bw, height=bh)
Btn_take2=Button(window,relief="solid",borderwidth=4,fg="black",bg=bbg,text="학교설명",font=buttonfont, command=lambda:open2()).place(x=bw+xxx*2, y=by,width=bw, height=bh)
Btn_take3=Button(window,relief="solid",borderwidth=4,fg="black",bg=bbg,text="상담신청",font=buttonfont, command=lambda:open3()).place(x=bw*2+xxx*3,y=by,width=bw, height=bh)
Btn_take4=Button(window,relief="solid",borderwidth=4,fg="black",bg=bbg,text="공지사항",font=buttonfont, command=lambda:open4()).place(x=bw*3+xxx*4, y=by,width=bw, height=bh)
Btn_take5=Button(window,relief="solid",borderwidth=4,fg="black",bg=bbg,text="만든이들",font=buttonfont, command=lambda:open5()).place(x=bw*4+xxx*5, y=by,width=bw, height=bh)
Btn_take6=Button(window,relief="solid",borderwidth=4,fg="black",bg=bbg,text="홈 화면",font=(tf.Font(family="카페 24 써라운드",weight="bold",size=20)), command=lambda:open6()).place(x=bw*2+xxx*3-25, y=by+220,width=200, height=100)

#프로그램 시작
open6()
window.mainloop()