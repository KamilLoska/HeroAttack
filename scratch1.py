#my_container = ['Larry', 'Moe', 'Curly']
#for index, element in enumerate(my_container):
    #print ('{} {}' .format(index, element))



def f(a, L=None):
    if L is None:
        L = []

    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))



some_list = ['a', 'b', 'c', 'd', 'e']
(first, second, *rest) = some_list
print(rest)
(first, *middle, last) = some_list
print(middle)
(*head, penultimate, last) = some_list
print(head)




result_list = ['True', 'False', 'File not found']
result_string = ''.join(result_list)
print(result_string)


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return '{0}, {1}'.format(self.x, self.y)
p = Point('Dupa', 123)
print (p)
print(set('Python'))
# Prints '1
