def print_params(a=1, b='string', c=True):
    print(a, b, c)
print_params(b=25)
print_params(c=[1, 2, 3])
values_list = [31, 'Alyona', [3,8,2,4]]
values_dict = {'a': 31, 'b': 'Alyona', 'c': [3,8,2,4]}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)