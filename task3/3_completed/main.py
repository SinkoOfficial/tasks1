from data.storage import FileStorage
from business.services import OrderService
from presentation.ui import ConsoleUI

if __name__ == "__main__":
    storage = FileStorage()
    service = OrderService(storage)
    ui = ConsoleUI(service)
    ui.menu()
