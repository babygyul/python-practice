# 거북이를 사용하자
import turtle
turtle.title('거북아놀자') # 윈도우의 제목을 변경해보자
turtle.color('black','red') #거북이 색사을 변경해보자
# turtle.shape('turtle')    # 거북이를 나타나게하자
#함수정의
def move(legth):
    turtle.penup()
    turtle.forward(legth)
    turtle.pendown()

move(-300)
for i in range(3,15):
    turtle.begin_fill()
    turtle.circle(20,steps=i)
    move(50)
    turtle.end_fill()

#클릭시 종료되게 하자
turtle.exitonclick()