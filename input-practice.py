# input 기능에 대한 연습(로그인 예제)

id = 'souljit1'
password = '비밀번호'

input_1 = input('아이디를 입력하세요: ')
input_2 = input('비밀번호를 입력하세요: ')

if id == input_1 and password == input_2:
    print('로그인 성공')

if id != input_1 or password != input_2:
    print('로그인 실패')