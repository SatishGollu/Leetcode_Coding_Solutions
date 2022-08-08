#Process_tasks_Using_servers
import heapq
def assigntasks(servers,tasks):
    #Time - O(mlogn)
    # 2 minheaps one for available server, one for unavailable
    # available = (weight,index)
    # unavailable = (timeServerBecomesFree,weight,index)

    res = [0]*len(tasks)
    available = [(servers[i],i) for i in ragne(len(servers))]
    heapq.heapify(available)
    unavail = []

    t = 0
    for i in range(len(tasks)):
        t = max(t,i)
        if len(available) == 0:
            t = unavail[0][0]
        while unavail and t >= unavail[0][0]:
            timefree,weight,index = heapq.heappop(unavail)
            heapq.heappush(available,(weight,index))
        weight,index = heapq.heappop(available)
        res[i] = index
        heapq.heappush(unavail, (t+tasks[i],weight,index))
    return res
