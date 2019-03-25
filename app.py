from flask import Flask, render_template, request, redirect
from bokeh.embed import components 
from bokeh.plotting import figure

import quandl
import pandas

app = Flask(__name__)
api_key='jbRSL-X-sdwcuPrSpM8w'
quandl.ApiConfig.api_key=api_key


def get_plot(df):
	#Make plot and customize
	p=figure(x_axis_type="datetime",title= request.form['symbol']+' Stock Price')
	p.xaxis.axis_label='Date'
	p.yaxis.axis_label='Stock Price (USD)'
	r=p.line(df.date,df.close)
	return(p)

@app.route('/')
def home():
  return render_template('home.html')

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
		p=get_plot(data)
		script, div=components(p)
		return render_template('post.html', script=script, div=div)

if __name__ == '__main__':
  app.run(port=33507)