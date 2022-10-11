def area(x1,y1,x2,y2):
    a=x2-x1
    b=y2-y1
    answer=a*b*(1/2)
    return answer

x1=int(input('x1의 좌표를 입력하세요:'))
y1=int(input('y1의 좌표를 입력하세요:'))
x2=int(input('x2의 좌표를 입력하세요:'))
y2=int(input('y2의 좌표를 입력하세요:'))
print('직각삼각형의 면적은 :',area(x1,y1,x2,y2))