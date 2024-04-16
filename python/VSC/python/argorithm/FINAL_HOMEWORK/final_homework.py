from tkinter import *
import random
import math
import heapq

# 다익스트라 함수
def dijkstra(graph, start, arrive):
    distance = {node:[float('inf'), start] for node in graph}
    distance[start] = [0, start]
    queue = []

    heapq.heappush(queue, [distance[start][0], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distance[current_node][0] < current_distance:
            continue
        for next_node, weight in graph[current_node].items():
            total_distance = current_distance + weight
            if total_distance < distance[next_node][0]:
                distance[next_node] = [total_distance, current_node]
                heapq.heappush(queue, [total_distance, next_node])
                
    path = arrive

    path_output = arrive

    reserve = []
    reserve.append(path_output)
    while distance[path][1] != start:
        path_output += distance[path][1]
        path = distance[path][1] 
        reserve.append(path)
    path_output += start
    reserve.append(start)
    return reserve


n = random.randint(2,20)                      # 점 개수 저장
list_X_Spot = []            # X좌표를 저장할 리스트 선언
list_Y_Spot = []            # Y좌표를 저장할 리스트 선언
list_Node_Con = {}          # 기준 노드에서 연결된 모든 노드를 저장할 딕셔너리 선언
start = 0                  # 최단거리 출발점
arrive = 1                # 최단거리 도착점

# tkinter창 실행과 창 크기 선언
width_width = 800
window = Tk()
w = Canvas(window, width = width_width, height = width_width)
w.pack()

# x좌표 범위 0~800 10칸으로 나눠 1칸마다 랜덤위치 저장, tkinter에 표시
# y좌표 범위 0~800 10칸으로 나눠 1칸마다 랜덤위치 저장, tkinter에 표시
for i in range(n) :
    a = (i%10)
    b = (i%10)+1
    for j in range(n) :
        c = (j%10)
        d = (j%10)+1
        x = random.randint(a*80,b*80)                   
        y = random.randint(c*80,d*80)                   
        list_X_Spot.append(x)
        list_Y_Spot.append(y)
        w.create_oval(x-5,y-5,x+5,y+5,fill = 'purple')

# 기준노드에서 모든 이웃노드 연결, 간선을 tkinter에 표시
for i in range(0,n**2) :
    cur = {}
    for j in range(0,n**2) :
        if i == j :
            continue
        pita_line = (list_X_Spot[i]-list_X_Spot[j])**2+(list_Y_Spot[i]-list_Y_Spot[j])**2
        if math.sqrt(pita_line) <= math.sqrt(32000) :
            cur[j]=math.sqrt(pita_line)
            w.create_line(list_X_Spot[i],list_Y_Spot[i],list_X_Spot[j],list_Y_Spot[j],fill = 'thistle3')
        
    list_Node_Con[i] = cur   

# 출발점은 빨간색, 도착점은 파란색
w.create_oval(list_X_Spot[start]-5,list_Y_Spot[start]-5,list_X_Spot[start]+5,list_Y_Spot[start]+5,fill = 'red')
w.create_oval(list_X_Spot[arrive]-5,list_Y_Spot[arrive]-5,list_X_Spot[arrive]+5,list_Y_Spot[arrive]+5,fill = 'blue')

#다익스트라 실행
a = dijkstra(list_Node_Con,start,arrive)

#다익스트라 간선 tkinter에 표시
for i in range(len(a)-1) :
    w.create_line(list_X_Spot[a[i]],list_Y_Spot[a[i]],list_X_Spot[a[i+1]],list_Y_Spot[a[i+1]],fill = 'SteelBlue2', width=3)

window.mainloop()