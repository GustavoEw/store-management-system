
class Batch:
    def __init__(self):
        self.id = None
        self.product_id = None
        self.expiration_date = None
        self.quantity = None
    def set_batch(self, id, product_id, expiration_date, quantity):
        self.id = id
        self.product_id = product_id
        self.expiration_date = expiration_date
        self.quantity = quantity
    def get_batch(self):
        return {
            "id": self.id,
            "product": self.product_id,
            "expiration_date": self.expiration_date,
            "quantity": self.quantity
        }