import shelve

print(dir())

for m in dir(__builtins__):
    print(m)

for obj in dir(shelve.Shelf):
    if obj[0] != '_':
        print(obj)