class ConsoleUI:
    def __init__(self, service):
        self.service = service

    def menu(self):
        while True:
            print("1. Добавить пользователя")
            print("2. Добавить заказ")
            print("3. Показать пользователей")
            print("4. Показать заказы")
            print("0. Выход")

            choice = input("Выберите пункт: ")

            if choice == "1":
                name = input("Имя: ")
                email = input("Email: ")
                user = self.service.add_user(name, email)
                print("Пользователь добавлен:", user)

            elif choice == "2":
                user_id = int(input("ID пользователя: "))
                product = input("Товар: ")
                price = float(input("Цена: "))
                order = self.service.add_order(user_id, product, price)
                print("Заказ добавлен:", order)

            elif choice == "3":
                for u in self.service.get_users():
                    print(u)

            elif choice == "4":
                for o in self.service.get_orders():
                    print(o)

            elif choice == "0":
                break
