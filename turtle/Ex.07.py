from datetime import datetime
import turtle
import datetime
now = datetime.datetime.now()
print(now)
turtle.title(now) # 윈도우 제목
turtle.shape('turtle') # 모양을 거북이로
turtle.color('black','red') # 거북이 색상을 변경해보자
turtle.stamp() # 도장을 찍어보자
turtle.forward(30)
turtle.color('black','green') # 거북이 색상을 변경해보자
turtle.stamp() # 도장을 찍어보자
turtle.forward(30)
turtle.color('black','yellow')
turtle.stamp()
turtle.color('black','blue')
turtle.forward(30)
turtle.stamp()
# 클릭시 종료되게 하자
turtle.exitonclick()
