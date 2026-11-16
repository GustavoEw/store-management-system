class Product:
    def __init__(self):
       self.id = None
       self.name = None
       self.barcode = None
       self.unity = None
       self.price = None
       self.quantity = None
       self.category = None
       self.active = True

    def set_product(self, id, name, barcode,unity, price, quantity, category):
        self.id = id
        self.name = name
        self.barcode = barcode
        self.unity = unity
        self.price = price
        self.quantity = quantity
        self.category = category
    def get_product(self):
        return {
            "id": self.id,
            "name": self.name,
            "barcode": self.barcode,
            "unity":self.unity,
            "price": self.price,    
            "quantity": self.quantity,
            "category": self.category,
            "active": self.active
        }
    def deactivate(self):
        self.active = False
    def get_id(self):
        return self.id
