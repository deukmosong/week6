def print_root(a, b, c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    print( r1, '또는', r2)

print('x^2+4x-21의 근은',end=' ')
print_root(1,4,-21)
print("x^2-6x+8",end=' ')
print_root(1,-6,8)
####6-6 2번문제
def print_area(a,b):
    area=a*b//2
    print('밑변 ',a,' 높이 ',b,'인 삼각형의 면적은:',area)
print_area(10,20)