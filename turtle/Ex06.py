import turtle

turtle.title('거북아 놀자!!') # 윈도우 제목
turtle.shape('turtle') #모양을 거북이로
turtle.color('black','red') # 색상변경
turtle.pu(); #펜들어
turtle.write("거북아 놀자!!") # 문자열 출력
turtle.fd(80) #앞으로 80만큼 이동
turtle.pd(); # 펜 내려
turtle.bk(100) #뒤로 100만큼 이동
turtle.left(90);turtle.fd(18) #왼쪽으로 90도 회전 앞으로 18이동
turtle.right(90);turtle.fd(110) # 오른쪽으로 90도 회전 앞으로 110 이동
turtle.right(90);turtle.fd(18) # 오른쪽으로 90도 회전 앞으로 18이동
turtle.right(90);turtle.fd(110); #오른쪽으로 90도 회전 앞으로 110 이동
turtle.left(180); #180도 회전
turtle.exitonclick() # 마우스로 클릭시 윈도우 종료