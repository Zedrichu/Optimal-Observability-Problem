from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_next_states(self):
        raise NotImplementedError()

    @abstractmethod
    def __eq__(self, other) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def __hash__(self) -> int:
        raise NotImplementedError()


class Placement(State):
    def __init__(self, n: int, bits: bytearray, g: int, parent: State | None = None):
        super().__init__()
        self.n = n
        self.bits = bits

        self.parent = parent
        self.g = g

        self._str = ""
        self._hash = None

    def get_next_states(self) -> list[State]:
        next_states = []
        for i in range(self.n):
            next_bits = self.bits[:]
            next_bits[i] ^= 1
            next_state = Placement(n=self.n, bits=next_bits, g=self.g + 1, parent=self)
            next_states.append(next_state)
        return next_states

    def __str__(self):
        if self._str:
            return self._str
        else:
            self._str = ''.join(str(bit) for bit in self.bits)
        return self._str

    def __eq__(self, other):
        if not isinstance(other, Placement):
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
            self._hash = int(self.bits, 2)
        return self._hash
