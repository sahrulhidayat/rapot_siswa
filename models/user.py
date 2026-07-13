from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, root):
        self.root = root

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def search(self):
        pass

    @abstractmethod
    def get_data(self, event):
        pass
