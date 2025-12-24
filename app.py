from flask import Flask, render_template
import requests 
from dotenv import load_dotenv
load_dotenv() 
import os
apikey= os.getenv("APIKEY")
url="https://api.api-ninjas.com/v1/quotes"
headers={'X-Api-Key': apikey}
def get_quote():
    response=requests.get(url,headers=headers)
    data=response.json()
    if isinstance(data,list) and len(data)>0:
        quote_value = data[0]['quote']
        author_value = data[0]['author']
        category_value = data[0] ['category']
        return quote_value, author_value,category_value
    else:
        return "No quote found"
    
app=Flask(__name__)
@app.route('/')
def home():
    quote,author,category=get_quote()
    return render_template('ai_quote.html',quote1=quote,author1=author,category1=category)
@app.route('/registration')
def registration():
      return render_template('registration.html')
@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/home')
def homepage():
    return render_template('home.html')
app.run(use_reloader=True)