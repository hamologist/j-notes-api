from typing import List

from flask import request
from flask_auth0 import requires_auth
from flask_restful import Resource
from j_notes_api.notes.models import NoteModel


class NotesListResource(Resource):

    @requires_auth
    def get(self):
        current_user_id: str = request.current_user_id
        user_notes: List[NoteModel] = NoteModel.objects(user=current_user_id)
        response = []
        for user_note in user_notes:
            response.append({
                'id': str(user_note.id),
                'text': user_note.text
            })

        return response

    @requires_auth
    def post(self):
        current_user_id: str = request.current_user_id
        new_note = NoteModel(user=current_user_id,
                             text=request.form['data'])
        new_note.save()

        return 'success'
