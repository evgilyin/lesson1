def get_summ(one, two, delimeter='&'):
    one = str(one).upper()
    two = str(two).upper()
    return f'{one}{delimeter}{two}'

print(get_summ('Learn','Python'))


def f1(a, b):
    
    return str(a), str(b)


def f2(a, b):
    a = str(a)
    b = str(b)
    return a, b
one, two = f2(1,2)

print(f1(1, 2))
print(f2(1, 2))

