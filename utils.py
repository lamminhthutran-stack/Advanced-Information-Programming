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