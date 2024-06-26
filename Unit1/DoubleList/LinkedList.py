from __future__ import annotations

from typing import List, Any


class ObjList:
    """Класс ноды"""

    def __init__(self, data: str) -> None:
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj: ObjList) -> None:
        self.__next = obj

    def set_prev(self, obj: ObjList) -> None:
        self.__prev = obj

    def get_next(self) -> ObjList:
        return self.__next

    def get_prev(self) -> ObjList:
        return self.__prev

    def set_data(self, data: str) -> None:
        self.__data = data

    def get_data(self) -> str:
        return self.__data

    def __str__(self) -> str:
        return f'Data of node: {self.get_data()}'


class LinkedList:
    """Класс двусвязного списка"""

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add_obj(self, obj: ObjList) -> None:
        """Добавление в конец двусвязного списка"""
        new_node = obj
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            new_node.set_prev(self.tail)
            self.tail = new_node

    def remove_obj(self) -> None:
        """Удаление из конца двусвязного списка"""
        if self.tail:
            prev_node = self.tail.get_prev()
            if prev_node:
                prev_node.set_next(None)
            self.tail = prev_node
            if not self.tail:
                self.head = None

    def get_data(self) -> List[str]:
        """Получаем список строк дата"""
        head = self.head
        data = []
        while head is not None:
            data.append(head.get_data())
            head = head.get_next()
        return data


if __name__ == '__main__':
    lst = LinkedList()
    lst.add_obj(ObjList('данные 1'))
    lst.add_obj(ObjList('данные 2'))
    lst.add_obj(ObjList('данные 3'))
    res = lst.get_data()
    print(res)
    lst.remove_obj()
    res = lst.get_data()
    print(res)
    lst.remove_obj()
    lst.remove_obj()
    res = lst.get_data()
    print(res)
    print(ObjList('fjefkejkf'))

