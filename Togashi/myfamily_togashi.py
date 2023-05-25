import introfamily

import sys
args = sys.argv

name = args[1]
age = args[2]
cat = args[3]

famintro = introfamily.IntroFam(name, age, cat)

print(famintro.name_out())
print(famintro.age_out())
print(famintro.cat_out())