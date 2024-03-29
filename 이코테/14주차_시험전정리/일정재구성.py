#일정 재구성 코드 테스트

import collections

tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
graph = collections.defaultdict(list)

def dfs(a):
    while graph[a]:
        dfs(graph[a].pop())
    route.append(a)

for a, b in sorted(tickets, reverse=True):
    graph[a].append(b)

route = []
dfs("JFK")
print(list(route[::-1]))