from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
  return '<h> This is a header test </h>'

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run()
