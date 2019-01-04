import datetime

from bson import ObjectId
from mongoengine import Document, StringField, DateTimeField


class NoteModel(Document):
    id: ObjectId
    user = StringField(required=True)
    text = StringField(max_length=5000)
    date_created = DateTimeField(default=datetime.datetime.utcnow)
    date_modified = DateTimeField(default=datetime.datetime.utcnow)
