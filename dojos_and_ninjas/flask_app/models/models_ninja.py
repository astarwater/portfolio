from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import models_dojo
from flask_app.models import models_ninja


class Ninjas:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_ninjas(cls, data):
        query = "SELECT * FROM ninjas"
        results = connectToMySQL('mydb').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojos_id) VALUES ( %(first_name)s, %(last_name)s, %(age)s, %(dojos_id)s);"
        return connectToMySQL('mydb').query_db(query, data)

    @classmethod
    def get_ninjas_from_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojos_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('mydb').query_db(query, data)
        print(results)
        dojo = models_dojo.Dojo(results[0])
        for row in results:
            n = {
                "id": row["ninjas.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "age": row["age"],
                "created_at": row["ninjas.created_at"],
                "updated_at": row["ninjas.updated_at"]
            }
            dojo.ninjas.append(cls(n))
        return dojo

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL('mydb').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
