contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

v = input("")

for i in range(len(contacts)):
    if v in contacts[i]:
        print(v, "is", contacts[i][1])
        break
if v not in contacts[i]:
    print('Not Found')