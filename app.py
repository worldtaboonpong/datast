from flask import Flask
from flask import render_template
from Clustering.func_clustering import clustering 
from Statistics.StatisticFunction import statistics
from AssociationRule.assocrule import association

import pandas as pd

app = Flask(__name__)

# df = pd.read_excel('./MRTuser.xlsx' , 'สายฉลองรัชธรรม'  )


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