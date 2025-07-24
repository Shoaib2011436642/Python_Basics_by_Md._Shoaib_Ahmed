#Machine start stop using Abstraction
from abc import ABC, abstractmethod

# Abstract class defining machine behavior
class Machine(ABC):
    @abstractmethod
    def start(self):
        pass  # No implementation yet

    @abstractmethod
    def stop(self):
        pass  # No implementation yet

# A concrete class representing a Fan
class Fan(Machine):
    def start(self):
        print("Fan started spinning")  # Specific start behavior

    def stop(self):
        print("Fan stopped")  # Specific stop behavior

# Creating a Fan object and calling its methods
fan = Fan()
fan.start()  # Outputs: Fan started spinning
fan.stop()   # Outputs: Fan stopped