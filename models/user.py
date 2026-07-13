from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, root):
        self._root = root
        self._name = ""
        self._identifier = ""
        self._table_name = ""

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, value):
        self._root = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = str(value).strip()

    @property
    def identifier(self):
        return self._identifier

    @identifier.setter
    def identifier(self, value):
        self._identifier = str(value).strip()

    @property
    def table_name(self):
        return self._table_name

    @table_name.setter
    def table_name(self, value):
        self._table_name = str(value).strip()

    @abstractmethod
    def get_role_label(self):
        pass

    @abstractmethod
    def build_profile(self):
        pass

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

    def describe(self):
        return f"{self.get_role_label()} - {self.get_name() or '-'}"
