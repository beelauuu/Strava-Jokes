import requests
import joke
from flask import json 
from flask import request
from flask import Flask
from flask_restful import reqparse
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome guys to the Strava App'

@app.route('/strava', methods=['POST'])
def api_strava_message():
    if request.headers['Content-Type'] == 'application/json':
        print(my_info)
        my_info = request.json
        if(my_info['aspect_type'] == 'create'):
            joke.update_joke()
        return my_info
        
if __name__ == '__main__':
    app.run(debug=True)

