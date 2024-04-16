from tarfile import LENGTH_LINK
from tkinter import *
import random
import math
import sys
import heapq

# n = random.randint(2,20)
n = 10
list_X_Spot = []
list_Y_Spot = []
list_Node_Line_Count = []
list_Node_Con = []
INF = int(1e9)
all_count = 0
start = 10
arrive = 89
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

width_width = 800
window = Tk()
w = Canvas(window, width = width_width, height = width_width)
w.pack()

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
        w.create_oval(x-5,y-5,x+5,y+5,fill = 'red')


for i in range(0,n**2) :
    count = 0
    for j in range(0,n**2) :
        pita_line = (list_X_Spot[i]-list_X_Spot[j])**2+(list_Y_Spot[i]-list_Y_Spot[j])**2
        if math.sqrt(pita_line) <= math.sqrt(12800) :
            all_count+=1
            count+=1
            cur = (i,(j,math.sqrt(pita_line)))
            list_Node_Con.append(cur)
            w.create_line(list_X_Spot[i],list_Y_Spot[i],list_X_Spot[j],list_Y_Spot[j],fill = 'gray')
    list_Node_Line_Count.append(count)    


# # 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
# def get_smallest_node() :
#     min_value = INF
#     index = 0 
#     for i in range(1, n + 1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#     return index

# def dijkstra(start):
#     distance[start] = 0
#     visited[start] = True
#     for i in list_Node_Line_Count[start]:
#         distance[[i][0]] = list_Node_Con[i][1]

#     for i in range(n - 1):
#         now = get_smallest_node()
#         visited[now] = True
#         # 현재 노드와 연결된 다른 노드를 확인
#         for j in list_Node_Line_Count[now]:
#             cost = distance[now] +list_Node_Con[j][1]
#             # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost



window.mainloop()