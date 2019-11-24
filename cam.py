import numpy as np
import cv2
import requests
import json
from sgmnt import MaskRCNN
import time

model = MaskRCNN()

cap = cv2.VideoCapture(0)
url = 'http://127.0.0.1:8080/'

company_name = 'Pyaterochka'
args = json.dumps({'company': company_name})
response = json.loads(requests.post(url + 'new-shop/', data = args).json())
id_shop = response['id']

args = json.dumps({'company': company_name, 'shop': id_shop})
response = json.loads(requests.post(url + 'new-cam/', data = args).json())
id_cam = response['id']
print(id_cam)

#index_frame = 0

last_time = time.time()
delta_time = 30 

i = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #model.predict(frame)
    #frame = model.magix(point=True)
    #gray = cv2.cvtColor(frame)

    #path = 'capture%.4d.jpg' % index_frame
    #cv2.imwrite(path,frame)
    

    #index_frame += 1
    # Display the resulting frame
    cv2.imshow('frame', frame)
    current_time = time.time()
    if (abs(current_time - last_time) > delta_time):
        last_time = current_time
        args = json.dumps({"company": company_name, "shop": id_shop, "cam": id_cam, "index_frame": i, "time" : current_time})
        data = requests.post(url + 'predict-cam/', data=args)
        i += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()