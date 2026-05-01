from player import Player
from map import campus_map, get_current_location, player_move, get_neighbors
from data_loader import load_events
from quest import Quest
from place import get_place
from utils import use_item
from utils import use_item, save_game, load_game

player = Player()
events_data = load_events('events.pkl')
event_info = events_data["events"]
event_answers = events_data["answers"]

input_log = []

print("송도 생활을 마치고 신촌에 처음 도착했다. 연대앞 버스정류장이다.")
print("현재 시간은 11시.")
print("1시 수업은 이윤재관 511호다.")
print("배가 고프다")


while True:
    cmd = input(">> ").strip()
    input_log.append(cmd)
    
    if cmd == "상태":
        neighbors = get_neighbors(player, campus_map)
        neighbors = get_neighbors(player, campus_map)
        print(f"계좌의 잔액: {player.money}원")
        print(f"HP: {player.HP}")
        print(f"현재위치: {player.location}")
        print(f"동: {neighbors['동']}, 서: {neighbors['서']}, 남: {neighbors['남']}, 북: {neighbors['북']}")
    
    
    elif cmd in ["동", "서", "남", "북"]:
        result = player_move(player, cmd, campus_map)
        if result != "blocked":
            if player.difficulty == "보통":
                player.HP -= 1
            if player.difficulty == "어려움":
                player.HP -= 2
            elif player.difficulty == "쉬움":
                player.HP -= 0.5
                
            if player.location in event_info:
                print(f"[사건]: {event_info[player.location]}") 
                
            Quest.on_arrive(player, event_answers)
            
    elif cmd == "가방":
        if not player.inventory:
            print("가방이 비어있습니다.")
        else:
            print("가방 목록:")
            for i, item in enumerate(player.inventory, 1):
                print(f"{i}. {item}")
            choice = input("사용 할 물선 이름 또는 번호 (취소: 엔터): ").strip()
            use_item(player, choice)
    
    elif cmd == "상호작용":
        Quest.interact(player, event_answers)
        
    elif cmd == "구매":
        place = get_place(player.location)
        if place.buy_items:
            place.interact_buy(player)
        else:
            print("이 장소에서는 구매할 수 없습니다.")
            
    elif cmd == "판매":
        place = get_place(player.location)
        if place.sell_items:
            place.interact_sell(player)
        else:
            print("이 장소에서는 판매할 수 없습니다.")
        
    elif cmd == "임무목록":
        Quest.show_quests(player)
        
    elif cmd == "저장":
        save_game(player, input_log)
        
    elif cmd == "불러오기":
        player, input_log = load_game(player)
    
    elif cmd == "난이도":
        print(f" 현재 난이도: {player.difficulty}")
        choice = input("난이도를 선택하세요 (쉬움, 보통, 어려움): ").strip()
        if choice in ["쉬움", "보통", "어려움"]:
            player.difficulty = choice
            print(f"난이도가 {choice}로 변경되었습니다.")
        else:
            print("잘못된 난이도입니다.")

    elif cmd == "종료":
        print("게임을 종료합니다.")
        break
     
    else:
        print("알 수 없는 명령어입니다.")