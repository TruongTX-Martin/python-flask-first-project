
from os import name
from app.main import db
from app.main.model.product import Product


def product_create(data):
    product = Product.query.filter_by(name=data['name']).first()
    if product is None:
        new_product = Product(
            name = data['name'],
            description = data['description'],
            images = data['images'],
            old_price = data['old_price'],
            new_price = data['new_price'],
            number = data['number'],
        )
        save_changes(new_product)
        response = {
            'isSuccess': True,
            'message': 'Create product success'
        }
        return response, 201
    else: 
        response = {
            'isSuccess': False,
            'message': 'Product name already exits'
        }
        return response, 409

def product_update(data,id):
    product = get_a_product(id)
    product.name = data['name']
    product.description = data['description']
    product.images = data['images']
    product.old_price = data['old_price']
    product.new_price = data['new_price']
    product.number = data['number']
    db.session.commit()
    return product
    
def product_get_list():
    return Product.query.all();


def product_detail(id):
    return get_a_product(id)

def get_a_product(id):
    return Product.query.filter_by(id=id).first()
    
    
def save_changes(data):
    db.session.add(data)
    db.session.commit()
    
    

    
    