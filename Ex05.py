import turtle

turtle.title('거북아 놀자!!') # 윈도우 제목
turtle.shape('turtle') # 모양을 거북이로
turtle.color('black','red') # 색상변경
turtle.penup(); # 펜 들어
turtle.write("거북아 놀자!!") # 문자열 출력
turtle.forward(80) # 앞으로 80만큼 이동
turtle.pendown(); # 팬 내려
turtle.backward(100) # 뒤로 100만큼이동
turtle.exitonclick() # 마우스로 클릭시 윈도우 종료