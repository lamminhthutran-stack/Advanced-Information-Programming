import pickle
import os
import glob
from datetime import datetime

def use_item(player, choice):
    if not player.inventory:
        print("가방이 비어있습니다.")
        return

    if choice in player.inventory:
        item_name = choice

   
    elif choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(player.inventory):
            item_name = player.inventory[idx]
        else:
            print("올바른 번호를 입력하세요.")
            return
    else:
        print("올바른 물건 이름 또는 번호를 입력하세요.")
        return

    
    item_effects = {
        "두쫀쿠":   10,
        "카페라떼":  5,
    }

    if item_name in item_effects:
        hp_gain = item_effects[item_name]
        player.HP += hp_gain
        player.inventory.remove(item_name)
        print(f"{item_name}를 먹었습니다. HP={player.HP}")
    else:
        print("사용할 수 없는 물건입니다.")
        
def save_game(player, input_log):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"save_{timestamp}.pkl"

    save_data = {
        "HP":         player.HP,
        "money":      player.money,
        "location":   player.location,
        "row":        player.row,
        "col":        player.col,
        "inventory":  player.inventory,
        "quests":     player.quests,
        "difficulty": player.difficulty,
        "input_log":  input_log,
        "saved_at":   timestamp,
    }

    with open(filename, "wb") as f:
        pickle.dump(save_data, f)

    print(f"게임이 '{filename}'에 저장되었습니다.")

def load_game(player):
    save_files = glob.glob("save_*.pkl")

    if not save_files:
        print("저장된 파일이 없습니다.")
        return player, []

    print("저장된 파일 목록:")
    for i, f in enumerate(save_files, 1):
        print(f"  {i}) {f}")
    print(f"  {len(save_files)+1}) 직접 경로 입력")

    choice = input(">> ").strip()

    if choice.isdigit() and 1 <= int(choice) <= len(save_files):
        filepath = save_files[int(choice) - 1]

    elif choice == str(len(save_files) + 1) or not choice.isdigit():
        filepath = input("파일 경로를 입력하세요 (상대경로 또는 절대경로): ").strip()
        filepath = os.path.normpath(filepath)
    else:
        print("올바른 번호를 입력하세요.")
        return player, []

    if not os.path.exists(filepath):
        print(f"'{filepath}' 파일을 찾을 수 없습니다.")
        return player, []

    with open(filepath, "rb") as f:
        data = pickle.load(f)

    player.HP         = data["HP"]
    player.money      = data["money"]
    player.location   = data["location"]
    player.row        = data["row"]
    player.col        = data["col"]
    player.inventory  = data["inventory"]
    player.quests     = data["quests"]
    player.difficulty = data["difficulty"]
    input_log         = data["input_log"]

    print(f"'{filepath}'에서 불러왔습니다.")
    print(f"  위치: {player.location} | HP: {player.HP} | 잔액: {player.money}원")
    return player, input_log