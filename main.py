a = 'Python is the best programming language in the world'

b = a[5: -6]

print(b)

a = 'Guido van Rossum is the benevolent dictator for life'
b = a[::3]
print(b)

a = 'You have a problem with authority, Mr. Anderson.'
a_l = list(map(a.count, set(a)))
b = list(zip(set(a), a_l))

print(b)