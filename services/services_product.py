from batch import Batch
from product import Product


def create_product(id, name, barcode, unit_type, price, quantity, category):
    product = Product()
    product.set_product(id, name, barcode, unit_type, price, quantity, category)
    return product

def create_batch(id, product_id, expiration_date, quantity):
    batch = Batch()
    batch.set_batch(id, product_id, expiration_date, quantity)
    return batch