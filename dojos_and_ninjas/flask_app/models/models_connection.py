from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL


# @classmethod
# def save(cls, data):
#     query = "INSERT INTO users (first_name, last_name, email) VALUES ( %(first_name)s, %(last_name)s, %(email)s)"
#     return connectToMySQL('user_cr_db').query_db(query, data)

# @classmethod
# def destroy(cls, data):
#     query = "DELETE FROM users WHERE id = %(id)s;"
#     return connectToMySQL('user_cr_db').query_db(query, data)

# @classmethod
# def edit_user(cls, data):
#     query = "UPDATE USERS SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id = %(id)s;"
#     return connectToMySQL('user_cr_db').query_db(query, data)
