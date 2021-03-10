#!/usr/bin/python

import json
from bottle import request, response
from bottle import post, get, put, delete
import bottle


@post('/users/')
def user_creation():
    '''Handles name creation'''
##    try:
##        # parse input data
##        try:
##            data = request.json()
##        except:
##            raise ValueError
##        if data is None:
##            raise ValueError
##        username=data['username']  
##        password=data['password']
##        email=data['email']
##        response.status = "200 OK"
##    except:
##        #response.headers['Content-Type'] = 'application/json'
##        #print("hi")
##        response.status = "400 invalid"
##    finally:
    test = "Hello, world"
    return test   

@get('/users/checkPassword/<username>/<password>/')
def checkPassword(username,password):

    
    if "select * username" != password:
        response.status = "400 Invalid" 

    else:
    # return 200 Success
        response.status = "200 Success"
        #response.headers['Content-Type'] = 'application/json'
    return response.status


@put('/users/addfollower')
def addFollower():
##    try:
##        # parse input data
##        try:
##            data = request.json()
##        except:
##            raise ValueError
##        if data is None:
##            raise ValueError
##        username=data['username']
##        usernameToFollow=data['usernametofollow']
#Í#        response.status = "200 OK"
##
##
##    except:
##        response.status = "400 INVALID"
##

    test = "Hello, world"
    return test  

    
       
@delete('/users/removefollower/<username>/')
def deletefollower():
##    try:
##        # parse input data
##        try:
##            data = request.json()
##        except:
##            raise ValueError
##        if data is None:
##            raise ValueError
##        usernameToFollow=data['usernametounfollow']
##        response.status = 200
##    except:
##        response.status = 400
    test = "Hello, world"
    return test 


@get('/users/<username>/')
def getFollowers(username):
    
    test = "Hello, world"
    return test 

if __name__ == '__main__':
    bottle.run(host = '127.0.0.1', port = 8000) 
    
