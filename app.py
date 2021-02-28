from flask import Flask
from flask import render_template
from Clustering.func_clustering import clustering 
from Statistics.StatisticFunction import statistics
from AssociationRule.assocrule import association

import pandas as pd

app = Flask(__name__)

# qa_clustering = clustering(df)
# qa_statistic = statistics(df)
# qa_assoocrule = association(df) # default association(dataframe, min_support=0.01, min_confidence=0.4, min_lift=6, min_length=2)
# qa={**qa_clustering,**qa_statistic,**qa_assoocrule}


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/analyze')
def analyze():
    # qa_clustering = clustering(df)
    # qa_statistic = statistics(df)
    # qa_assoocrule = association(df)
    # qa={**qa_clustering,**qa_statistic,**qa_assoocrule}

    return

if __name__ == '__main__':
    app.run(debug=True)