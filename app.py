from flask import Flask
from flask import render_template,request
from Clustering.func_clustering import clustering 
from Statistics.StatisticFunction import statistics
from AssociationRule.assocrule import association
from werkzeug.utils import secure_filename
import os

import pandas as pd

app = Flask(__name__)
app.config['UPLOAD_EXTENSION'] = ['.xls','.xlsx','.csv']
app.config['UPLOAD_PATH'] = ''
# qa_clustering = clustering(df)
# qa_statistic = statistics(df)
# qa_assoocrule = association(df) # default association(dataframe, min_support=0.01, min_confidence=0.4, min_lift=6, min_length=2)
# qa={**qa_clustering,**qa_statistic,**qa_assoocrule}


@app.route('/')
def hello():
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
        # df = pd.read_excel(uploaded_file)
        # qa_clustering = clustering(df)
        # qa_statistic = statistics(df)
        # qa_assoocrule = association(df)
        # qa={**qa_clustering,**qa_statistic,**qa_assoocrule}
    
    msg = "Your file is uploaded"
    print(msg)
    

    return render_template('submit.html', msg=msg)

@app.route('/analyze', methods=['POST'])
def analyze():
    # THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    # file_path = os.path.abspath(fileToBeDataframe)
    # df = pd.read_excel(file_path)
    # qa_clustering = clustering(df)
    # qa_statistic = statistics(df)
    # qa_assoocrule = association(df)
    # qa={**qa_clustering,**qa_statistic,**qa_assoocrule}
    msg = 'This page will analyze data from your uploaded file'
    return render_template('analyze.html',  msg=msg)

if __name__ == '__main__':
    app.run(debug=True)