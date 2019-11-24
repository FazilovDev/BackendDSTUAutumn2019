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

class Logic():
    def __init__(self):
        self.dict_company = []

    def get_count_partner(self):
        return len(self.dict_company)
    
    def add_company(self, company):
        self.dict_company.append(company)

    def get_company(self, name):
        i = 0
        for company in self.dict_company:
            if (company.get_name() == name):
                return self.dict_company[i]
            i += 1
        return -1

    def get_company_names(self):
        companies = []
        for company in self.dict_company:
            companies.append(company.get_name())
        return companies

