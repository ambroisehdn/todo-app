from flask_restful import Resource, Api, reqparse, abort


def elementNotFound(id):
    
    abort(404, message="ressource {} doesn't exist".format(id))
        
class User(Resource):

	def get(self,id):
        # elementNotFound(id)
		return {
			"Hello": "User ok ok "+str(id)
		},200

	def delete(self, id):
            # elementNotFound(id)
		return {
			"Hello": "User ok ok "
		}, 200

	def put(self, id):
            # elementNotFound(id)
		return {
			"Hello": "User ok ok "
		}, 201

class UserList(Resource) :
    
    def get(self):
        return {}
    
    def post(self):
        return '',201


