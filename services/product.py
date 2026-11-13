class Product:
    def __init__(self):
        self.id = None
        self.name = None
        self.unit = None
        self.category = None
        self.barcode = None
        self.expiration_date = None
        self.price = None
        self.cost = None
        self.quantity = None
        self.active = True
        self.observations = None
    def set_product(self, id, name, unit, category, barcode, expiration_date, price, cost, quantity, observations):
            self.id = id
            self.name = name
            self.unit = unit
            self.category = category
            self.barcode = barcode
            self.expiration_date = expiration_date
            self.price = price
            self.cost = cost
            self.quantity = quantity
            self.observations = observations

    def get_product(self):
            return {
                "id": self.id,
                "name": self.name,
                "category": self.category,
                "barcode": self.barcode,
                "expiration_date": self.expiration_date,
                "price": self.price,
                "cost": self.cost,
                "quantity": self.quantity,
                "active": self.active,
                "observations": self.observations
            }
    def set_active(self, active):
            self.active = active    
