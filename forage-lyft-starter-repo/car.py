from abc import ABC, abstractmethod
from serviceable import Serviceable
from engine import Engine

class Car(Serviceable):
    def __init__(self, engine):
        self.engine = engine

    @abstractmethod
    def needs_service(self):
        pass
