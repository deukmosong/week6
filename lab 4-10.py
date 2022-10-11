def sum_sums(*numbers):
    sum=0
    print(len(numbers),'개의 인자',numbers)
    for i in numbers:
        sum+=i
    print('합계 :',sum,'평균 :',sum/len(numbers))

sum_sums(10,20,30)
        
###### 4-10 2번문제

def min_nums(*nums):
    min=999999999
    for i in nums:
        if(i<min):
            min=i
    print('최소값은',min)

min_nums(20,40,50,10)
