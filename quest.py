class Quest:
    def __init__(self,name, description, status = 'not started'):
        self.name = name
        self.description = description
        self.status = status
        
    def add_quest(player, name, description):
        if name not in player.quests:
            player.quests[name] = Quest(name, "in_progress")
            print(f"임무목록에'{name}' 임무가 추가되었습니다.")
            
    def complete_quest(player, name):
        if name in player.quests:
            player.quests[name].status = "completed"
            print(f"'{name}' 임무가 완료되었습니다.")
    
    def remove_quest(player, name):
        if name in player.quests:
            del player.add_quest[name]
    
    def show_quests(player):
        if not player.quests:
            print("현재 진행 중인 임무가 없습니다.")
            return
        print("임무목록:")
        for quest in player.quests.values():
            print(f"- {quest.name} (상태: {quest.status})")
            
    def interact(player, places, event_answers):
        location = player.location
        
        if location == "정문":
            interact_gate(player)
            
        elif location == "독수리상":
            interact_eagle(player)
        
        elif location == "본관":
            interact_main_building(player, event_answers)
            
        elif location == "세브란스병원":
            interact_severance(player, event_answers)
            
        elif location == "이윤재관":
            interact_classroom(player)
            
    def interact_gate(player):
        if "학교 소식 획인" not in player.quests:
            Quest.add_quest(
                player, 
                "학교 소식 획인",
                "학교에서 어떤 일들이 일어나고있는지 소식들이 모이는 독수리상에서 알아보자.")
        else:
            print("이미 정문에서 받은 임무가 있습니다.")
            
    def interact_eagle(player):
        if "학교 소식 획인" in player.quests and player.quests["학교 소식 획인"].status != "completed":
            Quest.complete_quest(player, "학교 소식 획인")
        
        if "교내 부조리 조사" not in player.quests:
            Quest.add_quest(
                player,
                "교내 부조리 조사",
                "교내 어딘게에서 부조리가 일어자고있다. 이동하고 상호작용을 해서 부조리를 찾아서 본관에 보고하라.")
        
        if "교내 위생사건 수사" not in player.quests:
            Quest.add_quest(
                player,
                "교내 위생사건 수사",
                "학생들이 단체로 식중독에 걸렸다. 이동하고 상호작용을 해서 위생사건의 원인을 찾아서 세브란스에 보고하라.")
    
    def interact_main_building(player, event_answers):
        if "교내 부조리 조사" in player.quests and player.quests["교내 부조리 조사"].status != "completed":
            print("해결할 임무가 없습니다.")
            return
        
        if player.quests["교내 부조리 조사"].status == "completed":
            print("이미 해결한 임무입니다.")
            return
        
        answer = input("교내 어디에 부조리가 있나? ")
        if answer == event_answers["교내 부조리 수사"]:
            Quest.complete_quest(player, "교내 부조리 조사")
            print("수업들으러 이윤재관 가야지!")
            
        else:
            print("정답이 아닙니다. 다시 시도하세요.")
            
    def interact_severance(player, event_answers):
        if "고내 위생사건 수사" not in player.quests:
            print("해결할 임무가 없습니다.")
            return
        
        if player.quests["교내 위생사건 수사"].status == "completed":
            print("이미 해결한 임무입니다.")
            return
        
        
        answer = input("교내 어디에 식중독 원인이 있나?")
        if answer == event_answers["교내 위생사건 수사"]:
            Quest.complete_quest(player, "교내 위생사건 수사")
            print("수업들으러 이윤재관 가야지!")
            
        else:
            print("정답이 아닙니다. 다시 시도하세요.")
            
    def interact_classroom(player):
        corruption_done = (
            "교내 부조리 수사" in player.quests and
            player.quests["교내 부조리 수사"].status == "completed"
        )
        
    food_done = (
        "교내 위생사건 수사" in player.quests and
        player.quests["교내 위생사건 수사"].status == "completed"
    )
    
    if corruption_done and food_done:
        print("모든 임무를 완료했습니다! 축하합니다!")
        return "end"
    
    elif corruption_done:
        print("부조리 수사를 완룔했습니다! 식중독 원인도 찾아주세요.")
        
    elif food_done:
        print("식중독 원인 수사를 완료했습니다! 부조리도 찾아주세요.")
    
    else:
        print("독수리상에서 임무를 받고 오세요")
        
    