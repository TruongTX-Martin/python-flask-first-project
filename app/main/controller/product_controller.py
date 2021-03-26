from typing import NewType
from app.main import create_app
from flask import request
from flask_restplus import Resource

from ..util.dto import ProductDto
from ..service.product_service import product_create, product_detail, product_get_list, product_update

api = ProductDto.api
product = ProductDto.product


@api.route('/')
class ProductList(Resource):
    
    @api.doc('Get list product')
    @api.marshal_list_with(product)
    def get(self):
        return product_get_list()
    
    @api.doc('Create product')
    @api.expect(product, validate=True)
    def post(self):
        data = request.json;
        return product_create(data);
    
@api.route('/<id>')
class Product(Resource):
    
    @api.doc('Get product detail')
    @api.marshal_with(product)
    def get(self,id):
        return product_detail(id)
    
    @api.doc('update product')
    @api.marshal_with(product)
    def put(self,id):
        data = request.json;
        return product_update(data,id)  

