'''
Q1.
사내 시스템에 들어가기 위해서는 
사원 아이디와, 사원 번호를 입력받아서

아이디가 최규리, 사원 번호가 20220701 인지 확인해야 합니다.
아이디와 사원 번호가 동일하면, '환영합니다'를,
아이디가 틀렸으면 '아이디가 없습니다'를,
사원번호가 틀렸으면 '사원번호가 없습니다'를 출력하도록 하세요.
사원번호박스이름:sawon
'''
id='최규리'
sawon='20220701'
id_input=input('아이디를입력하세요:')
sawon_input=input('사원번호를입력하세요:')
if id == id_input and sawon == sawon_input :
    print('환영합니다')
if id != id_input :
    print('사원번호가 없습니다')
if sawon != sawon_input :
    print('사원번호가 없습니다')