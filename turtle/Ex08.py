from concurrent.futures.process import _threads_wakeups
import turtle

turtle.title('거북아놀자') # 윈도우의 제목을 변경해보자
turtle.shape('turtle') # 거북이를 나타나게하자

turtle.color('black','red') 
turtle.forward(100)
turtle.stamp() #도장을 찍어보자
turtle.left(120)
turtle.color('black','green') #거북이 색상을 변경해보자
turtle.forward(100)
turtle.stamp()
turtle.left(120)
turtle.color('black','blue')
turtle.forward(100)
turtle.stamp()
# 클릭시 종료되게 하자
turtle.exitonclick()