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
    files_dir = 'Files'
    for root, dirs, files in os.walk(files_dir):
        for name in files:
            if (name == file_to_be_analyze):
                os.remove(os.path.join(root,name))

    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submitFile():

    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSION']:
            return
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
        global file_to_be_analyze
        file_to_be_analyze = filename   
    msg = "Your file is uploaded , the file is" + file_to_be_analyze
    print(msg)
    return render_template('submit.html', msg=msg)


@app.route('/analyze', methods=['GET','POST'])
def analyze():
 
    file = 'Files/'+ file_to_be_analyze
    df = pd.read_excel(file)
    qa_clustering = clustering(df)
    qa_statistic = statistics(df)
    qa_assoocrule = association(df)
    qa={**qa_clustering,**qa_statistic,**qa_assoocrule}
    msg = 'This page will analyze data from your uploaded file '+ file_to_be_analyze
    if (request.method == 'POST'):
        return render_template('analyze.html',  msg=msg, qa=qa)
    # else:
    #     return render_template('answers.html',  msg=msg, qa=qa)


@app.route('/predict' , methods=['POST'])
def predict():

    msg = 'This page will predict data from your uploaded file'
    return render_template('predict.html',  msg=msg)


if __name__ == '__main__':
    app.run(debug=True)