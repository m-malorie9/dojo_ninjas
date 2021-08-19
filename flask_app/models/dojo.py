from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.ninja import Ninja

class Dojo():

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas=[]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        for d in results:
            dojos.append(Dojo(d))
        return dojos

    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(dojo_name)s);"
        result = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return result

# blue %s need data as well

    @classmethod
    def show_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojos_id WHERE dojos.id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        dojo = Dojo(result[0])
        for n in result:
            if n["ninjas.id"]!= None:
                ninja_data={
                    'id': n['ninjas.id'],
                    'first_name': n['first_name'],
                    'last_name': n['last_name'],
                    'age': n['age'],
                    'created_at': n['ninjas.created_at'],
                    'updated_at': n['ninjas.updated_at'],
                    'dojos_id': n['dojos_id']
                }
                ninja = Ninja(ninja_data)
                dojo.ninjas.append(ninja)
        return dojo
