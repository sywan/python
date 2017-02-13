
class PPAP(object):
    def __getattr(self):
        def missing(*args, **kwargs):
            print("".join(args) + name)
        return missing

# ppap = PPAP()
# ppap.pen("Apple")   # applepen

class Human(object):
    def greeting(self):
        print('hello')

me= Human()
me.greeting()   # hello

setattr(Human, "greeting", lambda s: print("I have an Apple"))

you = Human()
you.greeting()  # I have an Apple
me.greeting()   # I have an Apple

from unittest.mock import Mock

real = Human()
real.method = Mock(return_value=3)
real.method(3,4,5, key='value')

real.method.assert_called_with(3,4,5, key='value')

#
from forbiddenfruit import curse, reverse
def times(self):
    return range(0,self)

curse(int, "times", times)
print('Add a new function "times()" to int type..')
for i in (3).times():
    print(i)


