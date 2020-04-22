# Copyright (C) 2020 Scott Henshaw

import os
import sys
print( sys.path )
#sys.path.insert( 0, os.path.abspath( os.path.dirname(__file__)))

from flask import Flask, render_template, make_response, request, jsonify

import logging
import jinja2
import urllib.request

app = Flask(__name__, template_folder="server/templates") # , 'template folder path')
app.jinja_loader = jinja2.FileSystemLoader('client/dist')


# sets up CORS

from flask_cors import CORS, cross_origin
CORS(app, resources = { r"/api/*": { "origins":"*" } })
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



@app.route('/api/store/get', methods=['POST'])
def getRecordList ():
    
    # creates the query filter
    query = datastore_client.query(kind="testing") #/ here we can add large queries // https://googleapis.dev/python/datastore/latest/queries.html#google.cloud.datastore.query.Query
    # query.add_filter('property', '=', 'val')

    # TODO: our api should be pagenated, not returning full lists
    # loops through all items and adds them to a list
    entityList = []
    query_iter = query.fetch()
    for entity in query_iter:
        entityList.append(entity)
    
    # returns the list
    return jsonify(
        success=True,
        entityList=entityList
    )



# Sending Telemetry Records to Google

@app.route('/api/singe/<app_id>/<session_id>', methods = ['GET', 'POST'])
@cross_origin()
def do_single ( app_id, session_id ):
    resp = make_response({ 'error':-1 })

    if request.method == 'GET':
        #update this to pull the key from the request and then









### RUNNING DEV SERVER ###

if __name__=='__main__':
    app.run( host='127.0.0.1', port=4000, debug=True )



