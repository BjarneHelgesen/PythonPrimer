def add(a, b):
    return a + b

def get_007_name():
    return "James", "Bond"


first_name, last_name = get_007_name() 

counting = [1,2,3,4]
more_counting = [5,6,7,8]
some_counting = counting[0:2] #slice the first two elements of counting

print(add(1, 2)) # 3
print(add(1.1, 2.2)) # 3.3000000000000003
print(add('hello', 'world')) # helloworld
print(add(counting, more_counting)) # [1, 2, 3, 4, 5, 6, 7, 8]


def double(x):
    x = x + x
    return x

a = 10 
b = double(a)

double_count = double(counting)
print(double_count) # [1, 2, 3, 4, 1, 2, 3, 4]
print(counting) # [1, 2, 3, 4, 1, 2, 3, 4] 
