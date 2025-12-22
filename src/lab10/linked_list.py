from typing import Any, Iterator


class Node:
    def __init__(self, value: Any, next: "Node | None" = None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self._size: int = 0

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            assert self.tail is not None
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, value: Any) -> None:
        new_node = Node(value, self.head)
        self.head = new_node
        if self._size == 0:
            self.tail = new_node
        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
        if idx < 0 or idx > self._size:
            raise IndexError("index out of range")

        if idx == 0:
            self.prepend(value)
            return

        if idx == self._size:
            self.append(value)
            return

        current = self.head
        for _ in range(idx - 1):
            assert current is not None
            current = current.next

        new_node = Node(value, current.next)
        current.next = new_node
        self._size += 1

    def remove(self, value: Any) -> None:
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            if self._size == 1:
                self.tail = None
            self._size -= 1
            return

        prev = self.head
        current = self.head.next

        while current is not None:
            if current.value == value:
                prev.next = current.next
                if current == self.tail:
                    self.tail = prev
                self._size -= 1
                return
            prev = current
            current = current.next

    def __iter__(self) -> Iterator[Any]:
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"SinglyLinkedList({list(self)})"

    def pretty_print(self) -> str:
        parts = []
        current = self.head
        while current is not None:
            parts.append(f"[{current.value}]")
            current = current.next
        parts.append("None")
        return " -> ".join(parts)


if __name__ == "__main__":
    print("=== SinglyLinkedList ===")
    lst = SinglyLinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.prepend(0)
    lst.insert(2, 99)

    print(lst)
    print(lst.pretty_print())
    print("length:", len(lst))


" python3 -m src.lab10.linked_list "