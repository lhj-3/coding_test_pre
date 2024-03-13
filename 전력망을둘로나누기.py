# dfs에 필요한 것 => 현재 위치, 전체 노드, 방문 확인
def dfs(cur, wires, ch):
    # global로 변수 받아서 방문 가능 노드 수 +1
    global tmp
    # 현재 위치에서 방문 안한 곳 전부다 방문하면서 처리하는 것이 dfs
    for i in range(len(ch)-1):
        # 조건, 방문 안한 곳일 때
        if ch[i] == 0:
            # 시작점, 끝점을 확인함
            for j in range(2):
                # 만약 현재 위치가, 시작점이나 끝점에 포함이 된다면
                if wires[i][j]==cur:
                    # 현재 노드 방문처리
                    ch[i]=1
                    # 방문을 할 수 있으니 방문 가능 노드 수 +1
                    tmp+=1
                    # 현재 위치를 변경 시킨 후 다시 dfs
                    dfs(wires[i][(j+1)%2], wires, ch)
                    # 방문 해제
                    ch[i]=0
                    
def solution(n, wires):
    ch = [0] * n
    res = []
    global tmp
    for i in range(n-1):
        tmp=1
        # 방문처리로 tree나눠버림
        ch[i]=1
        a, b = wires[i][0], wires[i][1]
        dfs(a, wires, ch)
        ch[i]=0
        # 아래 수식을 쓰면 차이가 나옴
        res.append(abs(2*tmp-n))
    return min(res)
