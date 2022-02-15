from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.fav_language = data['fav_language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name, location, fav_language, comment) VALUES (%(name)s, %(location)s, %(fav_language)s, %(comment)s);"
        results = connectToMySQL(
            'dojo_survey_schema').query_db(query, data)
        return results

    @classmethod
    def last_survey(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
        results = connectToMySQL(
            'dojo_survey_schema').query_db(query)
        print(results[0])
        return Dojo(results[0])

    @staticmethod
    def validate_dojo(dojo):
        validate_dojo = True  # we assume this is true
        if len(dojo['name']) < 3:
            flash("Can't be blank.")
            validate_dojo = False
        if len(dojo['location']) < 1:
            flash("Must select one")
            validate_dojo = False
        if len(dojo['fav_language']) < 1:
            flash("Must select one")
            validate_dojo = False
        if len(dojo['comment']) < 3:
            flash("Can't be blank.")
            validate_dojo = False
        return validate_dojo
