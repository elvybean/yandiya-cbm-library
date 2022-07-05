numbers = [-1,-2,-4,0,3,-7]
#manuatly looping
has_positives = False
for n in numbers:
    if n > 0:
        has_positives = True
        break
#refactor using any()
has_positives = any (n > 0 for n in numbers)
print(has_positives)