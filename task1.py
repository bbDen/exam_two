def discribe_city(name,**kwargs):
    print(f'{name}')
    for i in kwargs:
       print(f'{i} - {kwargs[i]}')


discribe_city(name='USA', population = '330 million', is_democratic = True)
