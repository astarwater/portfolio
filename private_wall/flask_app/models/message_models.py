from unittest import result
from flask import flash, session
from flask import flash, redirect, request
from flask_app.config.mysqlconnection import connectToMySQL
db = 'private_wall_db'


class Message:
    def __init__(self, data):
        self.id = data['id']
        self.message = data['message']
        self.recipient_id = data['recipient_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']
        self.sender = data['sender']
        self.receiver = data['receiver']

    @classmethod
    def send_message(cls, data):
        query = "INSERT into messages (message, recipient_id, users_id) VALUES (%(message)s, %(recipient_id)s, %(users_id)s);"
        result = connectToMySQL(db).query_db(query, data)
        return result

    @classmethod
    def sent_message_count(cls, data):
        query = "SELECT * FROM messages WHERE users_id = (%(id)s);"
        result = connectToMySQL(db).query_db(query, data)
        return result

    @classmethod
    def get_all_messages(cls):
        query = "SELECT * FROM  messages WHERE recipient_id = (%(id)s);"
        results = connectToMySQL(db).query_db(query)
        messages = []
        for message in results:
            messages.append(cls(message))
        return messages

    @classmethod
    def get_message(cls, data):
        query = "SELECT users.first_name as sender, users2.first_name as receiver, messages.* FROM users LEFT JOIN messages on users.id = messages.users_id LEFT JOIN users as users2 on users2.id = messages.recipient_id WHERE users2.id = %(id)s;"
        messages = connectToMySQL(db).query_db(query,data)
        all_messages = []
        if not messages:
            return False
        else:
            for message in messages:
                all_messages.append(cls(message))
            return all_messages

    @classmethod
    def delete_message(cls, data):
        query = "DELETE FROM messages where id = %(id)s;"
        result = connectToMySQL(db).query_db(query, data)
        return result

    @classmethod
    def get_sender_name(cls):
        query = "SELECT first_name FROM users INNER JOIN messages ON  users.id = messages.users_id;"
        result = connectToMySQL(db).query_db(query)
        return result
