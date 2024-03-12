# 답지를 봄
def explore_dungeons(k, dungeons):
    # 종료 조건: 던전이 더 이상 없을 때
    if not dungeons:
        return 0

    max_dungeons = 0
    for i, dungeon in enumerate(dungeons):
        min_required_fatigue, fatigue_consumption = dungeon

        # 현재 피로도가 던전 진입에 충분하다면
        if k >= min_required_fatigue:
            # 던전 진입 후 소모되는 피로도를 계산하여 재귀적으로 호출
            remaining_fatigue = k - fatigue_consumption
            remaining_dungeons = dungeons[:i] + dungeons[i+1:]
            max_dungeons = max(max_dungeons, 1 + explore_dungeons(remaining_fatigue, remaining_dungeons))

    return max_dungeons

def solution(k, dungeons):
    return explore_dungeons(k, dungeons)
