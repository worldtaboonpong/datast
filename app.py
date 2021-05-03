from flask import Flask
from flask import render_template,request
from utils.func_clustering import clustering
from utils.StatisticFunction import statistics
from utils.func_cleanexcel import cleanDataframe
from utils.decisiontree import DecisionTree
from utils.func_grouping import grouping
from utils.assocrule import association
from werkzeug.utils import secure_filename
import os
import pandas as pd
from flask_cors import CORS
import json
import gunicorn
import xlrd
import openpyxl
import psutil
from operator import xor
import math 

app = Flask(__name__,static_folder = "static")
CORS(app)
app.config['UPLOAD_EXTENSION'] = ['.xls','.xlsx','.csv']
app.config['UPLOAD_PATH'] = 'Files'
app.config['STATIC_PATH'] = 'static'
MYDIR = os.path.dirname(__file__)
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

file_to_be_analyze = ''

@app.route('/')
def hello():

    files_dir = app.config['UPLOAD_PATH']
    for root, dirs, files in os.walk(files_dir):
        for name in files:
            # if (name == file_to_be_analyze):
            os.remove(os.path.join(root,name))
            print('We gonna remove' + os.path.join(root,name))

    files_dir_2 = app.config['STATIC_PATH']
    for root,dirs,files in os.walk(files_dir_2):
        for name in files:
            if ('.png' in name):
                os.remove(os.path.join(root,name))
                print('We gonna remove' + os.path.join(root,name))


    return render_template('index.html')


@app.route('/upload')
def upload():
    return render_template('upload.html')


@app.route('/submit', methods=['POST'])
def submitFile():

    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSION']:
            return
        uploaded_file.save(os.path.join(MYDIR + '/' + app.config['UPLOAD_PATH'],filename))
        global file_to_be_analyze
        file_to_be_analyze = filename   
    msg = "Your file is uploaded , the file is" + file_to_be_analyze
    print(msg)
    return render_template('submit.html', msg=msg)


@app.route('/analyze', methods=['GET','POST'])
def analyze():
 
    file = app.config['UPLOAD_PATH']+'/'+ file_to_be_analyze
    df = pd.read_excel(file)
    qa_clustering = clustering(df)
    qa_statistic = statistics(df)
    qa_assoocrule = association(df)
    qa_grouping = grouping(df)
    qa={**qa_clustering,**qa_assoocrule,**qa_statistic,**qa_grouping}
    number_of_item = len(qa)
    list_number_of_item = list(range(0,number_of_item))
    i = 0
    qx = {}

    for question in qa:
        question_answer = [question]
        for answer in qa[question]:
            question_answer.append(answer)
            # question_answer.append(answer[1])
        qx[list_number_of_item[i]] = question_answer
        # print(question_answer[1:])
        i=i+1

    msg = 'This page will analyze data from your uploaded file '+ app.config['UPLOAD_PATH']+'/' + file_to_be_analyze
    print(msg)
    if (request.method == 'POST'):
        # print(qx)
        return render_template('analyze.html',  msg=msg, qa=qx, zip=zip)
    # else:
    #     return render_template('answers.html',  msg=msg, qa=qa)


@app.route('/predict' , methods=['POST'])
def predict():
    file = app.config['UPLOAD_PATH']+'/' + file_to_be_analyze
    df_before_clean = pd.read_excel(file)
    df_after_clean = cleanDataframe(df_before_clean)

    columns = list(df_after_clean)
    columns_values = {}
    for col in columns:
        value_of_col = sorted(list(set(df_after_clean[col])))
        # print(col)
        # print(value_of_col)
        columns_values[col] = value_of_col
    # print(columns_values)
    
    print('We gonna predict '+app.config['UPLOAD_PATH']+'/' + file_to_be_analyze)


    msg = 'This page will predict data from your uploaded file'
    return render_template('predict.html',  msg=msg, columns_values=columns_values,columns=columns)


@app.route('/showoutput', methods=['POST'])
def showOutput():

    # test = request.form.get("selector")
    # print(test)

    file = app.config['UPLOAD_PATH']+'/'+ file_to_be_analyze
    df_before_clean = pd.read_excel(file)
    df_after_clean = cleanDataframe(df_before_clean)
    columns = list(df_after_clean)
    #col_val_selector is the user's inputs
    col_val_selector = {}
    #target_column will be the last column of dataframe
    target_column = request.form.get("target_column")
    # print(target_column)
    for col in columns:
        if col != target_column:
            col_val_selector[col] = request.form.get("selector-for-"+col)
    # print(col_val_selector)
    x = DecisionTree()
    answer = x.getanswer(df_after_clean,col_val_selector)
    print('We gonna show output for  '+app.config['UPLOAD_PATH']+'/' + file_to_be_analyze)

    return render_template('predict-answer.html', target_column=target_column, answer=answer)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)