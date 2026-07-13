from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, root):
        self._root = root
        self._name = ""
        self._identifier = ""
        self.__table_name = ""

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

    def get_root(self):
        return self._root

    def set_root(self, value):
        self._root = value

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = str(value).strip()

    def get_identifier(self):
        return self._identifier

    def set_identifier(self, value):
        self._identifier = str(value).strip()

    def get_table_name(self):
        return self.__table_name

    def set_table_name(self, value):
        self.__table_name = str(value).strip()

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
