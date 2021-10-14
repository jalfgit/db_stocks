# application code goes here
# from flask import render_template, Flask
from flask import Flask,render_template
import pandas as pd
# from datetime import datetime

from sqlalchemy import create_engine
# import sys
import os

# db_string ='dbstocks.cslin35wcm7x.us-east-2.rds.amazonaws.com'

app = Flask(__name__)

db_string = os.getenv('DBT')
passwd = os.getenv('DBPW')

engine = create_engine(f'postgresql://postgres:{passwd}@{db_string}:5432/stocks')


@app.route('/')
def main():
    sql_query = 'select * from aapl'
    df = pd.read_sql(sql_query, engine)
    records_count = len(df)
    return f'<H1>access to database works, there are {str(records_count)} </H1>'

if __name__ == "__main__":
    app.run(debug=True)