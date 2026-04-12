player = {
    "HP":  10,
    "money": 50000,
    "location": "연대앞 버스정류장",
    "inventory": ["체크카드"],
    "quests": []
}

while True:
    cmd = input(">> ")
    
    if cmd == "상태":
        print("HP:", player["HP"])
        print("Money:", player["money"])
        print("Location:", player["location"])
        print("Inventory:", player["inventory"])
        print("Quests:", player["quests"])
        
    elif cmd == "종료":
        print("게임을 종료합니다.")
        break
    
    else:
        print("알 수 없는 명령어입니다.")