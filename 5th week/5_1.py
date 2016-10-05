#초식남 테스트 프로그램
question=["격투기가 왜 재밌는지 모르겠다",
          "회식에 건배할 때도 음료수도 OK",
          "고백을 받으면, 일단 누군가에게 상담한다.",
          "소녀취향의 만화가 싫지 않다.",
          "여자친구들과 잘 어울리지만, 연애로 발전하는 경우가 거의 없다.",
          "편의점 신제품에 항상 관심을 가진다.",
          "일할 때, 간식(특히 과자)를 옆에 둔다.",
          "외출보다 집에 있는 것을 더 좋아한다.",
          "이성을 위해 돈을 쓰는 것보다 다양한 취미생활을 즐기는 인생을 산다."]
cnt = 0
chosik_rating = 0

for i in question:
    a = input("%s (Y/N)" % i)
    if a=='Y' or a=='y':
        cnt=cnt+1

if cnt>=6:
    chosik_rating = 90
elif cnt>=3 and cnt<=5:
    chosik_rating = 60
elif cnt<=2:
    chosik_rating = 20

print("당신의 초식도는 %d퍼센트 입니다" % chosik_rating)