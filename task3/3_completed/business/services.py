from .models import User, Order

class OrderService:
    def __init__(self, storage):
        self.storage = storage
        data = self.storage.load()
        self.users = [User(**u) for u in data.get("users", [])]
        self.orders = [Order(**o) for o in data.get("orders", [])]

    def add_user(self, name, email):
        user = User(len(self.users)+1, name, email)
        self.users.append(user)
        self.storage.save(self.users, self.orders)
        return user

    def add_order(self, user_id, product, price):
        order = Order(len(self.orders)+1, user_id, product, price)
        self.orders.append(order)
        self.storage.save(self.users, self.orders)
        return order

    def get_users(self):
        return self.users

    def get_orders(self):
        return self.orders
