from flask import Flask, render_template, request, redirect
from bokeh.io import push_notebook, show, output_notebook
from bokeh.layouts import row
from bokeh.plotting import figure

import requests
import quandl
import pandas

app = Flask(__name__)
api_key='jbRSL-X-sdwcuPrSpM8w'
quandl.ApiConfig.api_key=api_key


@app.route('/')
def home():
  return render_template('home.html')

timestart='2016-01-01'
timestop='2016-12-31'

@app.route('/', methods=['POST'])
def my_form_post():
	symbol = request.form['symbol']
	processed_symbol = symbol.upper()
	symbol=processed_symbol

	date_start = request.form['datestart']
	processed_date_start = date_start.upper()
	date_start = processed_date_start

	date_end = request.form['dateend']
	processed_date_end = date_end.upper()
	date_end = processed_date_end

	timestop='2016-12-31'
	data = quandl.get_table('WIKI/PRICES', qopts = { 'columns': ['ticker', 'date', 'close'] }, ticker = symbol, date = { 'gte': date_start, 'lte': date_end })
	if data.empty:
		return render_template('postfail.html')
		
	else:
		p1=figure(x_axis_type="datetime",title=' Stock Price')
		p1.xaxis.axis_label='Date'
		p1.yaxis.axis_label='Stock Price (USD)'
		r1=p1.line(data.date,data.close)
		t=show(p1,notebook_handle=True)
		return render_template('post.html')

	print(data)




if __name__ == '__main__':
  app.run()