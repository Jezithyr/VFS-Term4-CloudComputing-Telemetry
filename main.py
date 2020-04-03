# Copyright (C) 2020 Scott Henshaw

import os
import sys
print( sys.path )
#sys.path.insert( 0, os.path.abspath( os.path.dirname(__file__)))

from flask import Flask, render_template, make_response

import logging
import jinja2
import urllib.request

app = Flask(__name__, template_folder="server/templates") # , 'template folder path')
app.jinja_loader = jinja2.FileSystemLoader('client/dist')

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
        url = 'http:/localhost:3000/{0}'.format( path )
        return urllib.request.urlopen( url ).read()



"""
Add additional Flask Routes Here

"""


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

if __name__=='__main__':
    app.run( host='127.0.0.1', port=4000, debug=True )




