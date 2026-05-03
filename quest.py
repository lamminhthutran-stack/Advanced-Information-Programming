class Quest:
    def __init__(self, name, description, status='not started'):
        self.name = name
        self.description = description
        self.status = status


    def add_quest(player, name, description):
        if name not in player.quests:
            player.quests[name] = Quest(name, description)
            print(f"[임무목록]에 '{name}' 임무가 추가되었습니다.")
        
    def complete_quest(player, name):
        if name in player.quests:
            print(f"다음의 임무가 해결되었다! [{name}]")
            player.completed_quests.append(name)
            del player.quests[name]

    def remove_quest(player, name):
        if name in player.quests:
            del player.quests[name]

    def show_quests(player):
        if not player.quests:
            print("현재 진행 중인 임무가 없습니다.")
            return
        print("임무목록:")
        for quest in player.quests.values():
            print(f"  - {quest.name} - {quest.description}")

    def on_arrive(player, event_answers):
        location = player.location
        actions = []
        from place import Place
        place = Place.get_place(location)
        if place.buy_items:
            actions.append("구매")
        if place.sell_items:
            actions.append("판매")
        quest_locations = ["정문", "독수리상", "본관", "세브란스병원", "이윤재관"]
        if location in quest_locations:
            actions.append("임무")
        if actions:
            print(f"[{', '.join(actions)}]")
        if location in event_info:
            print(event_info[location])
        if location == "정문":
            Quest.interact_gate(player)

    def interact(player, event_answers):
        location = player.location
        if location == "정문":
            Quest.interact_gate(player)
        elif location == "독수리상":
            Quest.interact_eagle(player)
        elif location == "본관":
            Quest.interact_main_building(player, event_answers)
        elif location == "세브란스병원":
            Quest.interact_severance(player, event_answers)
        elif location == "이윤재관":
            return Quest.interact_classroom(player)
        else:
            print("이 장소에서는 상호작용할 수 없습니다.")

    def interact_gate(player):
        if "학교 소식 확인" not in player.quests:
            Quest.add_quest(
                player,
                "학교 소식 확인",
                "학교에서 어떤 일들이 일어나고있는지 소식들이 모이는 독수리상에서 알아보자.")

    def interact_eagle(player):
        if "학교 소식 확인" in player.quests:
            Quest.complete_quest(player, "학교 소식 확인")

        if "교내 부조리 수사" not in player.quests and "교내 부조리 수사" not in player.completed_quests:
            Quest.add_quest(
                player,
                "교내 부조리 수사",
                "교내 어딘가에서 부조리가 일어나고있다. 이동하고 상호작용을 해서 부조리를 찾아서 본관에 보고하라.")

        if "교내 위생사건 수사" not in player.quests and "교내 위생사건 수사" not in player.completed_quests:
            Quest.add_quest(
                player,
                "교내 위생사건 수사",
                "학생들이 단체로 식중독에 걸렸다. 이동하고 상호작용을 해서 위생사건의 원인을 찾아서 세브란스에 보고하라.")

    def interact_main_building(player, event_answers):
        if "교내 부조리 수사" not in player.quests:
            print("해결할 임무가 없습니다.")
            return
        answer = input("교내 어디에 부조리가 있나? ")
        if answer == event_answers["교내 부조리 수사"]:
            Quest.complete_quest(player, "교내 부조리 수사")
            print("수업들으러 이윤재관 가야지!")
        else:
            print("정답이 아닙니다. 다시 시도하세요.")

    def interact_severance(player, event_answers):
        if "교내 위생사건 수사" not in player.quests:
            print("해결할 임무가 없습니다.")
            return
        answer = input("교내 어디에 식중독 원인이 있나? ")
        if answer == event_answers["교내 위생사건 수사"]:
            Quest.complete_quest(player, "교내 위생사건 수사")
            print("수업들으러 이윤재관 가야지!")
        else:
            print("정답이 아닙니다. 다시 시도하세요.")

    def interact_classroom(player):
        corruption_done = "교내 부조리 수사" in player.completed_quests
        food_done = "교내 위생사건 수사" in player.completed_quests

        if not corruption_done and not food_done:
            print("독수리상에서 임무를 받고 오세요.")
            return
        
        if corruption_done and food_done:
            print("부조리와 식중독 수사를 완료했구나! 수업은 이걸로 끝입니다. 또 만나요~")
            return "end"
        elif corruption_done:
            print("부조리 수사를 완료했구나! 식중독 원인도 찾아주세요~")
        elif food_done:
            print("식중독 수사를 완료했구나! 부조리도 찾아주세요~")