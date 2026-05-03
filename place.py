from collections import Counter

class Place:
    def __init__(self, name, buy_items=None, sell_items=None):
        self.name = name
        self.buy_items = buy_items or {}
        self.sell_items = sell_items or {}


    def get_place(location):
        return Place.place_db.get(location, Place(location))
    
    def interact_buy(place, player):
        if not place.buy_items:
            print("구매할 수 있는 물건이 없습니다.")
            return
        while True:
            print("무엇을 구매하시겠습니까?")
            items = list(place.buy_items.items())
            for i, (name, (price, hp)) in enumerate(items, 1):
                print(f"  {i}) {name}: {price}원, HP가 {hp}만큼 증가한다.")
            print(f"  {len(items)+1}) 종료")

            choice = input(">> ").strip()

            if choice == str(len(items) + 1) or choice == "종료":
                print("구매를 종료합니다.")
                break
            elif choice.isdigit() and 1 <= int(choice) <= len(items):
                item_name, (price, hp) = items[int(choice) - 1]
                if player.money < price:
                    print(f"{item_name} 구매를 실패했다. 계좌 잔액이 부족하다.")
                else:
                    player.money -= price
                    player.inventory.append(item_name)
                    print(f"{item_name}를 구매해서 가방에 넣었다. 계좌 잔액 = {player.money}원")
            else:
                print("올바른 번호를 입력하세요.")


    def interact_sell(place, player):
        if not place.sell_items:
            print("판매할 수 있는 장소가 아닙니다.")
            return

        sellable = [item for item in player.inventory if item in place.sell_items]
        if not sellable:
            print("판매할 수 있는 물건이 없습니다.")
            return

        while True:
            sellable = [item for item in player.inventory if item in place.sell_items]
            if not sellable:
                print("팔 것이 없어서 종료합니다.")
                break

            count = Counter(sellable)
            unique_items = list(count.keys())

            print("무엇을 판매하시겠습니까?")
            for i, item in enumerate(unique_items, 1):
                price, hp = place.sell_items[item]
                print(f"  {i}) {item} x{count[item]}: {price}원")
            print(f"  {len(unique_items)+1}) 종료")

            choice = input(">> ").strip()

            if choice == str(len(unique_items) + 1) or choice == "종료":
                print("판매를 종료합니다.")
                break
            elif choice.isdigit() and 1 <= int(choice) <= len(unique_items):
                item_name = unique_items[int(choice) - 1]
                price, hp = place.sell_items[item_name]
                player.inventory.remove(item_name)
                player.money += price
                print(f"{item_name}를 판매해서 {price}원을 벌었다. 계좌 잔액 = {player.money}원")
            else:
                print("올바른 번호를 입력하세요.")


BUY_ITEMS_SCHOOL = {"두쫀쿠": (5000, 10), "카페라떼": (3000, 5)}
BUY_ITEMS_CAFE   = {"두쫀쿠": (4000, 10), "카페라떼": (2000, 5)}
SELL_ITEMS_HIGH  = {"두쫀쿠": (7000, 10), "카페라떼": (4000, 5)}
SELL_ITEMS_MID   = {"두쫀쿠": (6000, 10), "카페라떼": (3000, 5)}

Place.place_db = {
    "학생회관":    Place("학생회관",   buy_items=BUY_ITEMS_SCHOOL),
    "스타벅스":    Place("스타벅스",   buy_items=BUY_ITEMS_CAFE),
    "ABMRC":       Place("ABMRC",      buy_items=BUY_ITEMS_CAFE),
    "체육관":      Place("체육관",     sell_items=SELL_ITEMS_HIGH),
    "공학관":      Place("공학관",     sell_items=SELL_ITEMS_HIGH),
    "공학원":      Place("공학원",     sell_items=SELL_ITEMS_HIGH),
    "재활병원":    Place("재활병원",   sell_items=SELL_ITEMS_HIGH),
    "어린이병원":  Place("어린이병원", sell_items=SELL_ITEMS_HIGH),
    "노천극장":    Place("노천극장",   sell_items=SELL_ITEMS_HIGH),
    "중앙도서관":  Place("중앙도서관", sell_items=SELL_ITEMS_MID),
    "백양관":      Place("백양관",     sell_items=SELL_ITEMS_MID),
    "대강당":      Place("대강당",     sell_items=SELL_ITEMS_MID),
    "백주년기념관":Place("백주년기념관",sell_items=SELL_ITEMS_MID),
    "안과병원":    Place("안과병원",   sell_items=SELL_ITEMS_MID),
    "암병원":      Place("암병원",     sell_items=SELL_ITEMS_MID),
    "새천년관":    Place("새천년관",   sell_items=SELL_ITEMS_MID),
    "알렌관":      Place("알렌관",     sell_items=SELL_ITEMS_MID),
    "제중관":      Place("제중관",     sell_items=SELL_ITEMS_MID),
    "의과대학":    Place("의과대학",   sell_items=SELL_ITEMS_MID),
    "치과대학":    Place("치과대학",   sell_items=SELL_ITEMS_MID),
    "세브란스병원":Place("세브란스병원",sell_items=SELL_ITEMS_MID),
    "본관":        Place("본관",       sell_items=SELL_ITEMS_MID),
    "경영관":      Place("경영관",     sell_items=SELL_ITEMS_MID),
}