from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
  return '<h1>This is a test of the web deployment</h1>'
  #render_template('index.html')

#@app.route('/about')
#def about():
#  return render_template('about.html')

if __name__ == '__main__':
  app.run()