import numpy as np
import cv2
import requests
import json
import time


url = 'http://127.0.0.1:8080/'

company_name = 'Pyaterochka'
id_shop = 0


args = json.dumps({"company": company_name})
data = requests.post(url + 'new-shop/', data=args)
args = json.dumps({'company': company_name, 'shop': 0})
response = json.loads(requests.post(url + 'new-cam/', data = args).json())

last_time = time.time()
delta_time = 60 

i = 0
while(True):
    current_time = time.time()
    if (abs(current_time - last_time) > delta_time):
        last_time = current_time
        args = json.dumps({"company": company_name, "shop": id_shop})
        data = requests.post(url + 'shop-status/', data=args).json()
        print(data)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
