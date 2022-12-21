import requests 
import joke
from flask import json 
from flask import request
from flask import Flask
from flask_restful import reqparse
from flask import jsonify

#Basic Flask App
app = Flask(__name__)

#Home Page (just to make sure the application is up and running)
@app.route('/')
def api_root():
    return 'Welcome guys to the Strava App'

#/strava route to listen for any new activity and run the joke whenever an activity is uploaded
@app.route('/strava', methods=['POST'])
def api_strava_message():
    if request.headers['Content-Type'] == 'application/json':
        my_info = request.json
        if(my_info['aspect_type'] == 'create'):
            joke.update_joke()
        return my_info
        
if __name__ == '__main__':
    app.run(debug=True)

