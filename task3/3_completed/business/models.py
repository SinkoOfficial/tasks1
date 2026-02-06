import datetime

class User:
    def __init__(self, user_id, name, email):
        self.id = user_id
        self.name = name
        self.email = email
        self.created_at = str(datetime.datetime.now())

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email, "created_at": self.created_at}

    def __str__(self):
        return f"{self.id}: {self.name} ({self.email})"


class Order:
    def __init__(self, order_id, user_id, product, price):
        self.id = order_id
        self.user_id = user_id
        self.product = product
        self.price = price
        self.created_at = str(datetime.datetime.now())

    def to_dict(self):
        return {"id": self.id, "user_id": self.user_id, "product": self.product, "price": self.price, "created_at": self.created_at}

    def __str__(self):
        return f"{self.id}: {self.product} ({self.price}₸)"
