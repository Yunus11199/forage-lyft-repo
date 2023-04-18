from tyre.tyres import Tyres


class Carrigantyres(Tyres):
    def __init__(self, tyre_wear):
        self.tyre_wear = tyre_wear

    def needs_service(self):
        for tyre in self.tyre_wear:
            if tyre >= 0.9:
                return True
        return False