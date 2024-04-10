immutable_var = 1, 2, '10.04.2024', False
print(immutable_var)
# immutable_var[0] = 3   TypeError: 'tuple' object does not support item assignment
mutable_list = ['judas priest', 'sonata arctica', 'king diamond']
mutable_list [0] = 'helloween'
print(mutable_list)
mutable_list.append('kamelot')
print(mutable_list)
mutable_list.extend('HIM')
print(mutable_list)