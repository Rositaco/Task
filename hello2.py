print("좀보이드 서버를 위한 후원 부탁드립니다.\n(목표 후원금:100) \n서버 후원금을 입력해주세요 :")
donation = ""

money = 0

while money < 100:
    money += int(input(donation))
    result = 100 - money
    print("후원금이 입금 되었습니다. 목표 모금액에 달성하면 후원창은 종료됩니다.")
    print("- 현재 후원금: %d원" % money)
    print("- 최종 모금까지 남은 금액: %d원" % result)
    if money == 100:
        print("후원 감사합니다. 당신의 돈을 들고 튀겠습니다.")
        break

#돈이 입금되면 prompt문구 출력이 멈추는것 (o)
#현재 후원금이 얼마나 입금되었는지 출력하기 (o)
#목표 후원금에 달성하면 후원 입금완료 문구 출력 멈추기
#목표 후원금까지 얼마나 더 필요한지 계산하여 출력하기