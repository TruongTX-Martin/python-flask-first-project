from email.utils import decode_params
from flask_restplus import Namespace, fields

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user',{
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })
    

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
    
class ProductDto: 
    api = Namespace('product', description='product related operations')
    product = api.model('product',{
        'id': fields.Integer(required=False, description='The id product'),
        'name': fields.String(required=True, description='The name product'),
        'description': fields.String(required=True, description='The description product'),
        'images': fields.String(required=False, description='The images product'),
        'old_price': fields.Integer(required=True, description='The old price product'),
        'old_price': fields.Integer(required=True, description='The new price product'),
        'number': fields.Integer(required=True, description='The number product'),
    })
    