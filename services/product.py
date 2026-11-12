class Product:
    def __init__(self):
        self.id = None
        self.name = None
        self.price = None
        self.quantity = None
        self.active = True
    
    def set_product(self, id, name, price, quantity):
            self.id = id
            self.name = name
            self.price = price
            self.quantity = quantity

    def get_product(self):
            return {
                "id": self.id,
                "name": self.name,
                "price": self.price,
                "quantity": self.quantity,
                "active": self.active
            }
    def set_active(self, active):
            self.active = active    
