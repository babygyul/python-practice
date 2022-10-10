id = '최규리'
password = '몰라'

id_input = input('id를 입력하세요: ')
password_input = input('비밀번호를 입력하세요: ')

if id == id_input and password == password_input:
    print('로그인 성공')

if id != id_input:
    print('아이디가 없습니다.')

if password != password_input:
    print('패스워드가 틀렸습니다.')