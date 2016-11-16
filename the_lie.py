# coding: utf-8
from copy import deepcopy

variable1 = 5
variable2 = variable1
variable1 = 6
print(variable1)
print(variable2)
print('')

# now the lie!
colours1 = ["red", "green"]
colours2 = colours1
colours2[1] = "blue"
print(colours1)
print(colours2)
print('')

# now the lie fix to the lie
thing1 = ["red", "green"]
thing2 = deepcopy(thing1)
thing2[1] = "blue"
print(thing1)
print(thing2)
