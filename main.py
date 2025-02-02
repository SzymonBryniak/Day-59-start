from flask import Flask, render_template
import requests
from datetime import datetime

response = requests.get('https://api.npoint.io/674f5423f73deab1e9a7').json()

app = Flask(__name__)
# title, subtitle, author and dates
@app.route('/')
def home():
  return render_template('index.html', data= response, author="Api author", date=datetime.today().date())


@app.route('/contact')
def get_contact():
  return render_template('contact.html', data= response, author="Szymon Bryniak", date=datetime.today().date())


@app.route('/post')
def get_post():
  return render_template('post.html', data= response, author="Szymon Bryniak", date=datetime.today().date().strftime('%B, %d, %Y'))


@app.route('/about')
def get_about():
  return render_template('about.html', data= response, author="Api author", date=datetime.today().date())


@app.route('/ind_post/<int:id>')
def goto_post(id):
  return render_template('ind_post.html', data= response[id - 1], author="Api author", date=datetime.today().date().strftime('%B, %d, %Y'))

print(datetime.today().date())
 
if __name__ == "__main__":
  app.run(debug=True)