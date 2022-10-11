input_lst=list(map(int, input('쉼표로 구분된 정수를 여러개 입력하세요').split(',')))
print('입력된 정수의 리스트',input_lst)
for i in range(len(input_lst)-1):
    for j in range(i+1,len(input_lst)):
        if(input_lst[i]>=input_lst[j]):
            re=input_lst[i]
            input_lst[i]=input_lst[j]
            input_lst[j]=re
print('정렬된 정수의 리스트:',end=' ')
for i in range(len(input_lst)):
    print(input_lst[i],end=' ')

