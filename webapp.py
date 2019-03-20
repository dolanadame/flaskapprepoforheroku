from flask import Flask, render_template, request, redirect

webapp = Flask(__name__)

@webapp.route('/')
def index():
  return '<h> This is a header test </h>'

@webapp.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  webapp.run()
