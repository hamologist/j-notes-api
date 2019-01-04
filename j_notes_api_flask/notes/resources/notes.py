import datetime

from bson import ObjectId
from bson.errors import InvalidId
from flask import request
from flask_auth0 import requires_auth
from flask_restful import Resource
from j_notes_api_flask.notes.models import NoteModel


class NotesResource(Resource):

    @requires_auth
    def get(self, note_id: str):
        current_user_id: str = request.current_user_id
        try:
            user_notes: NoteModel = NoteModel.objects(id=ObjectId(note_id), user=current_user_id).first()
        except InvalidId:
            return {'error': 'Invalid note id'}

        return {
            'id': str(user_notes.id),
            'text': user_notes.text
        } if user_notes else {'error': 'The provided note id could not be found'}

    @requires_auth
    def put(self, note_id: str):
        current_user_id: str = request.current_user_id
        try:
            user_notes: NoteModel = NoteModel.objects(id=ObjectId(note_id), user=current_user_id).first()
        except InvalidId:
            return {'error': 'Invalid note id'}
        user_notes.text = request.form['data']
        user_notes.date_modified = datetime.datetime.utcnow()
        user_notes.save()

        return 'success'
