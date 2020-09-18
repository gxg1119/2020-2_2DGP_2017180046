import turtle
import random
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.penup()

turtle.forward(300)

turtle.pendown()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

turtle.exitonclick()
#Filename: py_03_03_2017182020_1.py

random
a=random.randint(1,6)
print(a)
b=random.uniform(2.3,4.0)
print(b)


v=input("Hello")
print(v)
v*10 #input이라는 함수가 리턴한 v의타입이 문제
print(v)
print(type(v))
vv=int(v)#int클래스를 통과하여 정수 48 이다.
print(vv)
print(v)#v는 문자열 48이다.

vv*10
print(vv)
#int('hello') 정수가 아닌 문자열을 입력하여 오류가난다.

if vv>10: print('large')

vv=5
if vv>10: print('large')
vv=100
if vv>10:
    print('hello')
    print('world')
    print('stop')
#elif와else를 사용할수있다.
#들여쓰기 중요**


turtle.reset()
count=1
while count<100:
    turtle.forward(200)
    turtle.left(179)
    count+=1


