while True:
    a = int(input("첫 번째 숫자  : "))
    b = input("연산기호 (+ - * /) :")
    c = int(input("두 번째 숫자  : "))

    if b == '+':
      result = a + c
    elif b == '-':
      result = a - c
    elif b == '*':
      result = a * c
    elif b == '/':
      if c != 0:
        result = a / c
      else:
        print("0으로 나눌 수 없습니다.")
        continue
    else:
      print("올바른 연산 기호를 입력하세요.")
      continue
    print(f"계산결과 : {a} {b} {c} = {result}")

    sel = input("종료하시겠습니까? (Y / N) : ")
    if sel.lower() == 'y':
      print('프로그램 종료')
      break
    elif sel.lower() == 'n':
      print('프로그램 재실행')
    else:
      print('정확한 입력이 아닙니다')