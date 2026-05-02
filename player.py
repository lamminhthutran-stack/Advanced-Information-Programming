class Player:
    def __init__(self):
        self.HP = 10
        self.money = 10000
        self.location = "연대앞 버스정류장"
        self.inventory = []
        self.quests = {}
        self.row = 6   
        self.col = 0
        self.difficulty = "보통"

    def move(self, direction):
        from map import campus_map, player_move
        return player_move(self, direction, campus_map)

    def print_status(self):
        from map import campus_map, get_neighbors
        neighbors = get_neighbors(self, campus_map)
        print(f"계좌의 잔액: {self.money}원")
        print(f"HP: {self.HP}")
        print(f"현재위치: {self.location}")
        print(f"동: {neighbors['동']}, 서: {neighbors['서']}, 남: {neighbors['남']}, 북: {neighbors['북']}")