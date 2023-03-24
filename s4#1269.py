a,b = map(int, input().split(' '))

a_ = list(map(int, input().split(' ')))
b_ = list(map(int, input().split(' ')))

s= list(set(a_) - set(b_))
n= list(set(b_) - set(a_))
print(len(s) + len(n))