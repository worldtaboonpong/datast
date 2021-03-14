from flask import Flask
from flask import render_template,request
from Clustering.func_clustering import clustering 
from Statistics.StatisticFunction import statistics
from AssociationRule.assocrule import association
from werkzeug.utils import secure_filename
import os
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_EXTENSION'] = ['.xls','.xlsx','.csv']
app.config['UPLOAD_PATH'] = 'Files'

file_to_be_analyze = ''

@app.route('/')
def hello():
    return {'result' : "Hello World"}

