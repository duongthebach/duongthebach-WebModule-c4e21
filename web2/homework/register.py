from mongoengine import Document, StringField

class Register(Document):
    fullname = StringField()
    email = StringField()
    username = StringField()
    password = StringField()