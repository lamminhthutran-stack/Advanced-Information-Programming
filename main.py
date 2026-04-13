from player import Player
from map import campus_map, get_current_location, player_move, get_neighbors

player = Player()

while True:
    cmd = input(">> ").strip()
    
    if cmd == "상태":
        current_location = get_current_location(player, campus_map)
        neighbors = get_neighbors(player, campus_map)
        
        print(f"HP: {player.HP}")
        print(f"계좌의 잔액: {player.money}")
        print(f"현재위치: {player.location}")
        print(f"동서남북 이웃 칸의 위치 이름: {player.location}") # 나중에 수정해야할 부분입니다.
        print(f"동: {neighbors['동']}, 서: {neighbors['서']}, 남: {neighbors['남']}, 북: {neighbors['북']}")
        
    elif cmd == "종료":
        print("게임을 종료합니다.")
        break
    
    else:
        print("알 수 없는 명령어입니다.")