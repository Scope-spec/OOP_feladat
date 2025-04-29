from Route import Route

class Domestic(Route):
    def __init__(self, id, destination, ticket_price):
        super().__init__(id, destination, ticket_price)

    def info(self):
        return f"Route number: {self.get_id}, Destination: {self.get_destination}, Ticket price: {self.get_ticket_price} huf"

