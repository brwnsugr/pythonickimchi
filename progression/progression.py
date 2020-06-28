class Progression:
### Iterator producing a generic progression.
### Default iterator produces the whole numbers 0, 1, 2, ... 
    def __init__(self, start=0):
        self._current = start ## _current 는 private 변수 

    def _advance(self):
        self._current += 1

    def __next__(self): 
    ### 여기서의 __next__는 special Method 임 
    ### (super class 에서 정의되어 있는 method 이다. 
    ### iteratable object의 다음 원소를 반환하는 method임)
        if self._current is None: # python 에서의 None은 ? None object임. 값을 부재를 의미함
            raise StopIteration()
        else:
            answer = self._current # record current value to return
            self._advance() # advance to prepare for next time
            return answer

    def __iter__(self):
        ### By convention, an iterator must return itself as an iterator.
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))

if __name__ == "__main__":
    a = Progression(1)
    a.print_progression(4)