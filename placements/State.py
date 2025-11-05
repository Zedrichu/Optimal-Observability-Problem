from abc import ABC, abstractmethod


class State:
    def __init__(self, n: int, goal: int, bits: bytearray, g: int, parent = None):
        super().__init__()
        self.n = n
        self.bits = bits
        self.goal = goal

        self.parent = parent
        self.g = g

        self._str = ""
        self._hash = None

    def get_next_states(self) -> list:
        next_states = []
        for i in range(self.n):
            if i == self.goal:
                continue
            next_bits = self.bits[:]
            next_bits[i] ^= 1
            next_state = State(n=self.n, goal=self.goal, bits=next_bits, g=self.g + 1, parent=self)
            next_states.append(next_state)
        return next_states

    def __str__(self):
        if self._str:
            return self._str
        else:
            self._str = ''.join(str(bit) for bit in self.bits)
        return self._str

    def __eq__(self, other):
        if not isinstance(other, State):
            return False
        if self.n != other.n:
            return False
        for i in range(self.n):
            if self.bits[i] != other.bits[i]:
                return False
        return True

    def __hash__(self):
        if self._hash:
            return self._hash
        else:
            self._hash = int(''.join(str(bit) for bit in self.bits), 2)
        return self._hash

    def __lt__(self, other):
        return self.__hash__() < other.__hash__()