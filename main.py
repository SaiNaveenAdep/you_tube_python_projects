from flask import Flask, render_template
from replit import db

app = Flask(__name__)

if 'number' not in db:
  db['number'] = 0

@app.route('/')
def home():
  #return show(home_page, number = db['number'])
  return render_template('index.html', number = db['number'])

@app.route('/Increment')
def increment():
  # increment a number
  db['number']+= 1
  print(db)
  return render_template('index.html', number = db['number'])

@app.route('/Decrement')
def decrement():
  # decrement a number
  db['number']-=1
  print(db)
  return render_template('index.html', number = db['number'])

app.run(host='0.0.0.0', port=81)









# # root 👉 '/'
# # inctrement 👉 '/increment'

# #db👉 {'number' : 0}
# ### HTML & CSS ### Static
#   '''
#   <link rel = 'stylesheet' href='./static/counter_styles.css'>

# <span>{{number}}</span> 
# <div>
#   <form action = '/Decrement'>
#     <button>-</button>
#   </form>  
#   <form action = '/Increment'>
#     <button>+</button>
#   </form>
# </div>
# '''

# '''
# This if statement initializes the database by storing a vlaue of 0 by default,
# even if a number is not present
# '''
# if 'number' not in db:
#   db['number'] = 0
