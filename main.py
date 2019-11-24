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
from Photo import Photo
import RestApi

app = Flask(__name__)
#app.secret_key = os.urandom(24)

api = Api(app)
api.add_resource(RestApi.StartedServer,'/')
api.add_resource(RestApi.Photo, '/photos/')
api.add_resource(RestApi.CamInitRest, '/new-cam/')
api.add_resource(RestApi.ShopInitRest, '/new-shop/')
api.add_resource(RestApi.ShopStatus, '/shop-status/')
api.add_resource(RestApi.CamPredictRest, '/predict-cam/')
api.add_resource(RestApi.CompaniesInfo, '/companies-info/')


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8080)