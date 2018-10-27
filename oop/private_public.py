#Private and Public
#underscore means private
#There is no such thing as private or public in python
class Math:
    def __init__(self,x,y):
        self._x=x
        self._y=y

    def _sum(self):
        return self._x + self._y

math=Math(2,4)
print(math._x) #wrong 