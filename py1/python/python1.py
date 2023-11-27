while True:
    별 = '입력해주세요'
    print(별)

    word = input("원하는 단어를 입력하세요: ")

    answer = f'당신이 입력한 단어는: [{word}]'
    print(answer)

    a = input("종료하시겠습니까? 'Y' / 'N': ")

    if a.lower() == 'y':
      print('프로그램 종료')
      break
    elif a.lower() == 'n':
      print('프로그램 재실행')
    else:
      print('올바른 입력이 아닙니다')


