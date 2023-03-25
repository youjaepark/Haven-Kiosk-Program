#모듈 import
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
def schoolphotoupdate():
    randomconcept =  random.randrange(0,7)
    schoolphoto_url = "https://haven.or.kr/school-life/%ec%82%ac%ec%a7%84/"

    schoolphoto_url_parse = BeautifulSoup(requests.get(schoolphoto_url).content, "html.parser")
    recent_schoolphoto_loc = schoolphoto_url_parse.find_all("li", {"class": "kboard-list-item"})[7]
    schoolphoto_url_recent= "https://haven.or.kr"+recent_schoolphoto_loc.find("a")["href"]
    save_dir = "imgsamples"

    for f in os.listdir(save_dir):
        os.remove(os.path.join(save_dir, f))

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    schoolphoto_url_recent_html = requests.get(schoolphoto_url_recent)
    html = schoolphoto_url_recent_html.content

    schoolphoto_url_parse = BeautifulSoup(html, "html.parser")

    images = schoolphoto_url_parse.find_all("img")

    for phimage in images:

        img_url = phimage["src"]
        if "haven.or.kr" not in img_url:
            img_url ="https://haven.or.kr"+ img_url

        with requests.get(img_url) as schoolphoto_url_recent:

            file_name = os.path.basename(img_url)

            with open(os.path.join(save_dir, file_name), "wb") as f:

                f.write(schoolphoto_url_recent.content) 
                #shutil.copyfileobj(schoolphoto_url_recent.raw, f)

schoolphotoupdate()
