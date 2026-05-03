
campus_map = [
    ["종합관", "본관", "경영관", "노천극장", "새천년관", "이윤재관"],
    ["백양관", "백양로5", "대강당", "음악관", "알렌관", "ABMRC"],
    ["중앙도서관", "독수리상", "학생회관", "루스채플", "재활병원", "치과대학"],  
    ["체육관", "백양로3", "공터2", "광혜원", "어린이병원", "세브란스병원"],
    ["공학관", "백양로2", "백주년기념관", "안과병원", "제중관", None],
    ["공학원", "백양로1", "공터1", "암병원", "의과대학", None],               
    ["연대앞 버스정류장", "정문", "스타벅스", "세브란스병원 버스정류장", None, None]
]

def get_current_location(player, campus_map):
    return campus_map[player.row][player.col]

def player_move(player, direction, campus_map):
    dr, dc = 0, 0
    if direction == "북":
        dr = -1
    elif direction == "남":
        dr = 1
    elif direction == "동":
        dc = 1
    elif direction == "서":
        dc = -1
    
    new_row = player.row + dr
    new_col = player.col + dc
    
    if new_row < 0 or new_row >= len(campus_map) or new_col < 0 or new_col >= len(campus_map[0]):
        print("그 방향은 막혔어.")
        return "blocked"
    
    if campus_map[new_row][new_col] is None:
        print("그 방향은 막혔어.")
        return "blocked"
    
    player.row = new_row
    player.col = new_col
    player.location = campus_map[new_row][new_col]
    print(f"{player.location}으로 이동했어.")
    hp_loss = {"보통": 1, "어려움": 2}
    player.HP -= hp_loss.get(player.difficulty, 1)
    return "moved"

def get_place_name(row, col, campus_map):
    if row < 0 or row >= len(campus_map) or col < 0 or col >= len(campus_map[0]):
        return None
    return campus_map[row][col]

def get_neighbors(player, campus_map):
    return {
        "북": get_place_name(player.row - 1, player.col, campus_map),
        "남": get_place_name(player.row + 1, player.col, campus_map),
        "동": get_place_name(player.row, player.col + 1, campus_map),
        "서": get_place_name(player.row, player.col - 1, campus_map),
    }
