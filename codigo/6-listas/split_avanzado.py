parrafo = "Lorem ipsum dolor sit amet, consectetur adipiscing elit..."
lista = parrafo.split()
print(lista)  # ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit...']
lista = parrafo.split(',')
print(lista)  # ['Lorem ipsum dolor sit amet', ' consectetur adipiscing elit...']
lista = parrafo.split('e')
print(lista)  # ['Lor', 'm ipsum dolor sit am', 't, cons', 'ct', 'tur adipiscing ', 'lit...']