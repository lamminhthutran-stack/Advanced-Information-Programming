from player import Player
from map import campus_map, get_current_location, player_move, get_neighbors
from data_loader import load_events
from quest import Quest
from place import Place
from utils import use_item, save_game, load_game

player = Player()
events_data = load_events('events.pkl')
event_info = events_data["events"]
event_answers = events_data["answers"]
 
input_log = []

print("송도 생활을 마치고 신촌에 처음 도착했다. 연대앞 버스정류장이다.")
print("임무완료를 보고할 장소는 이윤재관 511호다.")
print("배가 고프다")


while True:
    cmd = input(">> ").strip()
    input_log.append(cmd)
    
    if cmd == "상태":
        player.print_status()
    
    
    elif cmd in ["동", "서", "남", "북"]:
        result = player.move(cmd)
        if result == "moved":
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
        result = Quest.interact(player, event_answers)
        if result == "end":
            break
        
    elif cmd == "구매":
        place = Place.get_place(player.location)
        if place.buy_items:
            Place.interact_buy(place, player)
        else:
            print("이 장소에서는 구매할 수 없습니다.")
            
    elif cmd == "판매":
        place = Place.get_place(player.location)
        if place.sell_items:
            Place.interact_sell(place, player)
        else:
            print("이 장소에서는 판매할 수 없습니다.")
        
    elif cmd == "임무":
        result = Quest.interact(player, event_answers)
        if result == "end":
            break
    
    elif cmd == "임무목록":
        Quest.show_quests(player)
        
    elif cmd == "저장":
        save_game(player, input_log)
        
    elif cmd == "불러오기":
        player, input_log = load_game(player)
    
    elif cmd == "난이도":
        print(f" 현재 난이도: {player.difficulty}")
        choice = input("난이도를 선택하세요 (보통, 어려움): ").strip()
        if choice in ["보통", "어려움"]:
            player.difficulty = choice
            print(f"난이도가 {choice}로 변경되었습니다.")
        else:
            print("잘못된 난이도입니다.")

    elif cmd == "종료":
        print("게임을 종료합니다.")
        break
     
    else:
        print("알 수 없는 명령어입니다.")