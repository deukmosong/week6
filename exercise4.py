def find_answer(rember,n):
    for i in range(rember,(rember*n)+1):
        if i%rember==0 and i%n==0:
            rember=i
            break
    return rember 


start=int(input('범위의 시작 정수:'))
end=int(input('범위의 마지막 정수:'))

rember=start

for i in range(start,end+1):
            rember=find_answer(rember,i)

print('{}에서 {}까지의 정수들의 최소 공배수는:{}'.format(start,end,rember))