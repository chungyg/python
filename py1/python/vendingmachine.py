import random

while True:
    balance = 0 

    while True:
        a = int(input("돈을 넣어주세요: "))
        balance += a

        if balance >= 500:
            print(f"번호를 입력해 음료수를 골라주세요. 현재 잔액: {balance}")
            print("1. 콜라 : 500원")
            print("2. 사이다 : 700원")
            print("3. 닥터페퍼 : 1000원")
            print("4. 식혜 : 1200원")
            print("5. 랜덤 음료수 : 800원")

            result = input("음료를 선택하세요 (1, 2, 3, 4, 5): ")

            if result == '1':
                drink = '콜라'
                price = 500
            elif result == '2':
                drink = '사이다'
                price = 700
            elif result == '3':
                drink = '닥터페퍼'
                price = 1000
            elif result == '4':
                drink = '식혜'
                price = 1200
            elif result == '5':
                drinks = ['콜라', '사이다', '닥터페퍼', '식혜']
                drink = random.choice(drinks)
                price = 800
                print(f"랜덤 음료수가 선택되었습니다. 선택된 음료수: {drink}")
            else:
                print("올바른 선택이 아닙니다.")
                continue

            if balance >= price:
                balance -= price
                print(f"{drink}를 선택했습니다. 잔돈은 {balance}원 입니다.")
            else:
                print("돈이 부족합니다.")
                print(f"현재 잔액: {balance}")
                continue

            re1 = input(f"현재 잔액은 {balance}원 입니다. 다시 뽑으시겠습니까? (Y / N): ")
            if re1.lower() == 'y':
                continue
            elif re1.lower() == 'n':
                re_exit = input("거스름돈을 돌려드릴까요?. (Y / N): ")
                if re_exit.lower() == 'y':
                    print(f'거스름돈: {balance}, 현재 잔액 : 0')
                    break
                else:
                    print('프로그램 재실행')
                    
                    continue
            else:
                print('정확한 입력이 아닙니다.')
        else:
            print("돈이 부족합니다.")
            print(f"현재 잔액: {balance}")
            continue

    re2 = input("종료하시겠습니까? (Y / N): ")
    if re2.lower() == 'y':
        print('프로그램 종료')
        break
    elif re2.lower() == 'n':
        print('프로그램 재실행')
    else:
        print('정확한 입력이 아닙니다.')