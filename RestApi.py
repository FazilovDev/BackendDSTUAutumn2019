from flask import Flask,session, request, json, render_template, url_for,redirect
from flask_restful import Resource, Api
from json import dumps
from flask import jsonify
from flask_uploads import UploadSet, configure_uploads, DATA
import os
import cv2
from werkzeug.utils import secure_filename
from PIL import Image
import random
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import Server
from Company import *
import json


UPLOAD_FOLDER = 'C:\\Users\\fazil\\Desktop\\DSTUAutumn\\uploads'
ALLOWED_EXTENSIONS = set(['txt','pdf','png','jpg','jpeg','gif'])

logic = Server.Logic()

camera_record = []
density = 0


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class Photo(Resource):
    def get(self):
        
        return "Good"
    
    def post(self):
        #if request.method == 'POST':
            #if 'file' not in request.files:
           #     print('No file part')
           #     return redirect(request.url)
           # file = request.files['file']
           # if file.filename == '':
           #     print('No selected file')
           #     return redirect(request.url)
           # if file and allowed_file(file.filename):
           #     filename = secure_filename(file.filename)
           #     file.save(os.path.join(UPLOAD_FOLDER, filename))
        data = request.data
        frame = data['frame']
        path = '/uploads'
        cv2.imwrite(path, frame) 
        return {"Result:": "good"}, 201

class ShopStatus(Resource):
    def get(self):
        return {"Status: ": "Shop"}
    
    def post(self):
        global density
        body = json.loads(request.data)
        print(body['company'])
        '''
        name_company = body['company']
        id_shop = body['shop']
        comp = logic.get_company(name_company)
        print(' info ', comp.name)
        shop = comp.get_shop(id_shop)
        result = shop.get_status()
        '''
        result = sum(camera_record) / len(camera_record)
        print("result density: ",result)
        return json.dumps({"density:": result}), 201


class CamPredictRest(Resource):
    def get(self):
        return {"Status: ": "Camera"}
    
    def post(self):
        global density
        global camera_record
        body = json.loads(request.data)
        name_company = body['company']
        id_shop = body['shop']
        id_cam = body['cam']
        for i in range(len(body['density'])):
            if (body['density'] is None):
                body['density'] = 0
        data_predict = sum(body['density'])
        #shop = logic.get_company(name_company).get_shop(id_shop)
        #print(type(shop))
        #print(shop.get_cameras_id())
        #shop.get_camera(id_cam).add_density(data_predict)
        if (data_predict is None):
            data_predict = 0

        if (len(camera_record) == 2):
            density = sum(camera_record) / len(camera_record)
            camera_record = []
        camera_record.append(data_predict)
        print(camera_record)
        print("dencity : " ,data_predict)
        return {"density:": data_predict}, 201

class ShopInitRest(Resource):
    def post(self):
        body = json.loads(request.data)
        name_company = body['company']
        print(name_company)
        if (name_company not in logic.get_company_names()):
            new_company = Company(name_company)
            logic.add_company(new_company)

        current_company = logic.get_company(name_company)

        _id = current_company.add_shop()
        return json.dumps({"id": _id}), 201

class CompaniesInfo(Resource):
    def get(self):
        data = {}
        companies = logic.get_company_names()
        
        return companies

class CamInitRest(Resource):
    def get(self):
        return {"Status: ": "Camera"}
    
    def post(self):
        body = json.loads(request.data)

        if (body['company'] not in logic.get_company_names()):
            name_company = str(body['company'])
            new_company = Company(name_company)
            logic.add_company(new_company)
            
        
        current_company = logic.get_company(body['company'])
        if (body['shop'] not in current_company.get_shop_names()):
            current_company.add_shop()
        

        current_shop = current_company.get_shop(body['shop'])
        _id = current_shop.add_camera()
        print('id ', _id)

        return json.dumps({"id": _id}), 201



class StartedServer(Resource):
    def get(self):
        return {"Status: ": "Server start"}
    
    def post(self):
        return {"Status: ": "Server working"}, 201
