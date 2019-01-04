import logging

from flask import Flask
from flask_auth0 import handle_auth_error
from flask_auth0.auth_error import AuthError
from flask_restful import Api
from mongoengine import connect
from .notes.resources import NotesResource, NotesListResource

logging.basicConfig(level=logging.DEBUG)

connect('jNotesDB')

APP = Flask(__name__)
APP.errorhandler(AuthError)(handle_auth_error)

API = Api(APP)
API.add_resource(NotesResource, '/notes/<string:note_id>')
API.add_resource(NotesListResource, '/notes')
