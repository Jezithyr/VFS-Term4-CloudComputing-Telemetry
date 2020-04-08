# Copyright (C) 2020 Scott Henshaw

import os
import sys
print( sys.path )
#sys.path.insert( 0, os.path.abspath( os.path.dirname(__file__)))

from flask import Flask, render_template, make_response, request

import logging
import jinja2
import urllib.request

app = Flask(__name__, template_folder="server/templates") # , 'template folder path')
app.jinja_loader = jinja2.FileSystemLoader('client/dist')


# sets up CORS

from flask_cors import CORS, cross_origin
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


###   POST localhost:3000/hello ###

@app.route('/hello')
def hello():
    return 'Hello World'


### Main Route - Get the index page - local or on GAE ###

@app.route('/', defaults={'path':''})
@app.route('/<path:path>')
def vue_client( path ):
    logging.info( path )

    # runs the standard environment when in google app enviroment (GAE)
    if os.getenv('GAE_ENV','').startswith('standard'):
        templateVarList = {
            'title': 'hey this is my cool title'
        }
        return render_template('index.html', templateVarList)

    # when testing localy, just use local host
    else:
        url = 'http://localhost:3000/{0}'.format( path )
        return urllib.request.urlopen( url ).read()




### API CALLS ###

# Imports google libarary and creates a client
from google.cloud import datastore
datastore_client = datastore.Client.from_service_account_json("service_account.json")


# example edge

@app.route('/api/generic/<param>', methods=['GET','POST'])
def handler( param ):
    
    # request is a global object we can use to pull apart data sent to us
    if request.method == 'GET':
        # handle the get style of the request
        query = request.args.get('arg')  # ?arg=val&arg2=val2

    elif request.method == 'POST':
        # handle the post style of request
        post_data = request.data  # json object/string posted to this route
        form_data = request.form['fieldname'] # pulling data from form submissions

    # HTTP headers in/out
    request.headers



### APIS - STORING DATA ###


# Sending Telemetry Records to Google

@app.route('/api/store/send', methods=['POST'])
def sendRecord():

    # handle the post style of request
    post_data = request.data  # json object/string posted to this route

    print('recieved data: {}'.format(request.data))
    
    # creates the task to upload
    task_key = datastore_client.key('testing', 'sample-task') #/ takes in a categorY (testing) and unique id (sample-task)
    task = datastore.Entity(key=task_key)

    # inserts data to task from input
    for attr, value in request.form.items():
        task[attr] = value

    # upload
    datastore_client.put(task)

    print('Saved {}: {}'.format(task.key.name, task['description']))









### RUNNING DEV SERVER ###

if __name__=='__main__':
    app.run( host='127.0.0.1', port=4000, debug=True )



