from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        wear = 0
        for i in self.tire_wear:
            wear = wear + i
        if wear > 3:
            return True
        else:
            return False
