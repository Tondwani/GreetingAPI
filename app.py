from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/greeting', methods=['GET'])
def get_greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        greeting = 'Good morning'
    elif hour < 18:
        greeting = 'Good afternoon'
    else:
        greeting = 'Good evening'
    return greeting

if __name__ == '__main__':
    app.run(debug=True)
