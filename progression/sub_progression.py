from progression import Progression

class ArithmeticProgression(Progression):

    def __init__(self, increment=1, start=0):

        super().__init__(start) ## initialize base class
        self._increment = increment

    def _advance(self): ## 다음 항 업디에트 
        self._current += self._increment

class GeometricProgression(Progression): # Gemotric progression

    def __init__(self, base=2, start=1):
        super().__init__(start)
        self._base = base
    
    def _advance(self):
        self._current *= self._base

class FibonacciProgression(Progression):

    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self._current = self._current, self._prve + self._current

if __name__ == '__main__':
    p = ArithmeticProgression(0)
    p.print_progression(5)
