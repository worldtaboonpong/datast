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


@app.route('/analyze', methods=['POST'])
def analyze():
    file = 'Files/'+ file_to_be_analyze
    df = pd.read_excel(file)
    qa_clustering = clustering(df)
    qa_statistic = statistics(df)
    qa_assoocrule = association(df)
    qa={**qa_clustering,**qa_statistic,**qa_assoocrule}
    return 

