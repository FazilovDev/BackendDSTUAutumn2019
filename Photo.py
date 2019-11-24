from flask import Flask, request, json, render_template, url_for,redirect
from flask_restful import Resource, Api
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'C:\\Users\\fazil\\Desktop\\DSTUAutumn\\uploads'
ALLOWED_EXTENSIONS = set(['txt','pdf','png','jpg','jpeg','gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class Photo(Resource):
    def get(self):
        
        return "Good"
    
    def post(self):
        if request.method == 'POST':
            if 'file' not in request.files:
                print('No file part')
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                print('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                return {"Result:": "good"}, 201
