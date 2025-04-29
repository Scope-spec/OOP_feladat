class Route:
    def __init__(self, id, destination, ticket_price):
        self._id = id
        self._destination = destination
        self._ticket_price = ticket_price

    @property
    def get_id(self):
        return self._id

    @property
    def get_destination(self):
        return self._destination

    @property
    def get_ticket_price(self):
        return self._ticket_price