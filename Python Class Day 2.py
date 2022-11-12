#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("Hello World!")


# In[5]:


money = True

if money == True:
    print("택시를 타자")
else:
    print("걸어가자")


# In[8]:


money = 8000

if money >= 5000: 
    print("택시를 타자")
elif money >=1000: 
    print("버스를 타자")
else:
    print("걸어가자")


# In[11]:


# Q. 학생의 성적을 입력 받아서
#점수가 90 이상이면 "A학점입니다."
#점수가 80 이상이면 "B학점입니다."
#점수가 70 이상이면 "C학점입니다."
#점수가 60 이상이면 "D학점입니다."
#나머지는 모두 "F학점입니다."

score = input("점수를 입력하시오: ")
score_int = int(score)

#input함수를 int로 씌워줘도 된다!

if score_int >= 90:
    print("A학점입니다.")
elif score_int >= 80:
    print("B학점입니다.")
elif score_int >= 70:
    print("C학점입니다.")
elif score_int >= 60:
    print("D학점입니다.")
else:
    print("F학점입니다.")


# In[12]:


score = int(input("점수를 입력하시오: "))

if score >= 90:
    print("A학점입니다.")
elif score >= 80:
    print("B학점입니다.")
elif score >= 70:
    print("C학점입니다.")
elif score >= 60:
    print("D학점입니다.")
else:
    print("F학점입니다.")


# In[14]:


#새로운 셀: shift enter

#while

num = 10

while num >= 0:  # num이 0보다 크거나 같을 때만 10을 찍어라.
    print(num)
    num = num - 1  # num에서 1뺀 것을 다시 넣고 조건에 맞으면 반복해라.


# In[20]:


prompt = "1. 덧셈 / 2. 뺄셈 / 3. 곱셈 / 4. 나눗셈 / 5. 종료"
num = 0

while num <= 4:
    print(prompt)  #4이하면 계속 반복해서 물어보다가 5가 나오면 종료.
    num = int(input())
    

#몇 번 반복할지 모르는 게임. while 문이 더 어울린다!


# In[22]:


#while 문의 경우 반복 횟수가 정확하지 않을 경우가 많기 때문에 조건에서 뿐만이 아니라 while문 중간에 반복을 종료 시키는 방법도 필요하다.

num = 0

while num <= 10:  #while에 조건을 걸어서 무한반복을 못하게 하는 경우
    print(num)
    num = num + 1


# In[23]:


num = 0

while True:   #무한반복. 아래에 탈출 지점이 필요하다.
    print(num)
    num = num + 1
    
    if num > 10: 
        break   #무한반복하다가 중간에 반복을 종료하는'break'로 빠져나간다. 위의 코드와 비교해보자!
        


# In[76]:


# Q. while문을 사용하여 1부터 100까지의 수 중 3의 배수만의 합을 구하시오.

num = 1
sum = 0  #초기화

#햄버거 시작: while 쓰자

while num <= 100:
    if num % 3 == 0:  
        sum = sum + num  #3의 배수면 True ok!
#만약 3의 배수가 아니라면
    num = num + 1   # num += 1

# 햄버거 끝

print(sum)


# In[80]:


#for 문
#보통 변수명은 i를 많이쓴다.

for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)


# In[86]:


#90점 이상이 합격

math = [80,90,70,70,100]

j = 1  # if와 else에 둘다 걸리기 위해 밖에서

for i in math:   #math리스트에서 가져와
    if i >= 90:
        print(j, "번째 학생은 합격입니다.")
    else:
        print(j, "번째 학생은 불합격입니다.")
    j += 1


# In[89]:


# 짝수만 찍고 싶다

for i in [1,2,3,4,5,6,7,8,9,10]:
    if i%2 ==0 :
        print(i)
    


# In[90]:


# 짝수만 찍고 싶다 => 홀수는 안 찍고 싶다.

for i in [1,2,3,4,5,6,7,8,9,10]:
    if i%2 != 0 :   #0이 아니다 !=
        continue   #컨티뉴면 안 내려가고 다시 위로 올라감.
    
    print(i)


# In[92]:


# range 함수 (for문과 궁합이 잘맞음)

for i in range(1,11):
    print(i)


# In[95]:


# for문으로 구구단 출력하기

for i in range(2,10):  # 2단부터 9단까지. i = 단
    for j in range(1,10):   # j = 곱해지는 수
        print(i, "*", j, "=", i*j)


# In[97]:


# for문으로 구구단 출력하기: 세련ver 

for i in range(2,10): 
    for j in range(1,10):
        print(i*j, end = "\t")  # 줄 바꾸지 말고 탭해라.
    print()  #n단 다 돌때 줄바꿈!


# In[100]:


# for문으로 구구단 출력하기: 세련ver2

for i in range(1,10): 
    for j in range(2,10):
        print(i*j, end = "\t")
    print()


# In[111]:


# range를 사용하여 100 이하의 수 중 짝수들만의 합계를 구하세요.

sum = 0

for i in range(1,101):
    if i % 2 == 0:
        sum += i 
    
print(sum)


# In[112]:


sum = 0

for i in range(0,101,2):
    sum += i 
    
print(sum)


# In[116]:


#List Comprehension

list1 = [1,2,3,4]
print(list1)


list2 = [num           for num in list1]  # 리스트1에서 항목을 하나씩 가져와 num에 넣는다.
print(list2)


list3 = [num*2           for num in list1]  # 리스트를 만들기 전에 하나씩 곱해 만든다.
print(list3)


list4 = [num          for num in list1          if num % 2 == 0]  #리스트에서 꺼내서 조건에 해당하는 것만 num에 넣는다.
print(list4)


# In[121]:


#if 고급형: if를 표현하는 또 다른 방법

num = 70

if num >= 70:
    print("합격입니다.")
else:
    print("불합격입니다.")
    
    
print("합격입니다."    if num >= 80    else "불합격입니다.") 
#앞이 T 케이스, 뒤가 F 케이스


# In[ ]:




