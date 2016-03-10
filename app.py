from flask import Flask
import os

app = Flask(__name__)

#app begin
@app.route('/')



def printHello():
   print("hello")
return printHello()
    
    
    
#app end

if __name__ == '__main__':
    # gets Heroku's suggested port out of the environment dictionary if exists:
    port = int(os.environ.get('PORT', 5000))
    # this is the wsgi hook:
    app.run(host='0.0.0.0', port=port)
