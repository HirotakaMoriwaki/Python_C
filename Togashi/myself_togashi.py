import introduce

import sys
args = sys.argv

name = args[1]
age = args[2]

myselfintro = introduce.Intro(name, age)

print(myselfintro.name_out())
print(myselfintro.age_out())