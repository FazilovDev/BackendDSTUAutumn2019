
import requests
import shutil
import os

url = 'http://127.0.0.1:8080/'

def sendPhoto(url, filename):
    files = {"file": open(filename, "rb")}
    args = {"key": "API_KEY"}
    data = requests.post(url + 'images/', files=files, data=args)
    print(data.text)


for i in range(100):
    filename = 'cat' + str(i) + '.jpg'
    shutil.copy2('cat.jpg', filename)
    sendPhoto(url, filename)
    os.remove(filename)
