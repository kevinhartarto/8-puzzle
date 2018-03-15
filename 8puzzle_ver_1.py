from _heapq import heappush, heappop
class priorityqueue:
    def __init__(self):
        self.pq = []
    def __add__(self, other):
        heappush(self.pq, other)
    def peek(self):
        return self.pq[0]
    def poll(self):
        return heappop(self.pq)
    def remove(self, item):
        value = self.pq.remove(item)
        heappop(self.pq)
        return value is not None
    def __len__(self):
        return len(self.pq)

#global variabel
start_state = ['2','8','3','1','6','4','7','0','5']
goal_state = ['1','2','3','8','0','4','7','6','5']
current_state = []
visited = []
step =0
closeset = []
openset = priorityqueue()
leftList = [1,2,4,5,7,8]
rightList = [0,1,3,4,6,7]
upList=[3,4,5,6,7,8]
downList=[0,1,2,3,4,5]

#read start state of the 8-puzzle
#f_start = open('start_state.txt','r')
#start_state = f_start.read()
#start_state = start_state.splitlines()
#f_start.close()

#read goal state of the 8-puzzle
#f_goal = open('goal_state.txt', 'r')
#goal_state = f_goal.read()
#goal_state = goal_state.splitlines()
#f_goal.close()

#methods
def searchSuccessor(currentState):
    temp = currentState[:]
    index = temp.index('0')
    #Move Up
    if index in upList:
        temp[index], temp[index-3] = temp[index-3], temp[index]
        if temp not in visited:
            temp_state = [total(temp), currentState, temp[:], 'up']
            openset.__add__(temp_state[:])

        temp = currentState[:]
    #Move Down
    if index in downList:
        temp[index], temp[index+3] = temp[index+3], temp[index]
        if temp not in visited:
            temp_state = [total(temp), currentState, temp[:], 'down']
            openset.__add__(temp_state[:])

        temp = currentState[:]
    #Move Right
    if index in rightList:
        temp[index], temp[index+1] = temp[index+1], temp[index]
        if temp not in visited:
            temp_state = [total(temp), currentState, temp[:], 'right']
            openset.__add__(temp_state[:])

        temp = currentState[:]
    #Move Left
    if index in leftList:
        temp[index], temp[index-1] = temp[index-1], temp[index]
        if temp not in visited:
            temp_state = [total(temp), currentState, temp[:], 'left']
            openset.__add__(temp_state[:])

        temp = currentState[:]

#Cara ke-2
def _h(state):
    count = 0
    for lines in state:
        n = state.index(lines)
        i = goal_state.index(lines)
        if n != i and lines is not '0':
            if n < 3 and (2 < i < 6):
                if (2 < i < 6):
                    n = n+3
                    count = count + 1
                elif i > 5:
                    n = n + 6
                    count = count + 1
            elif (2 < n < 6):
                if i < 3:
                    n = n - 3
                    count = count + 1
                elif i > 5:
                    n = n + 3
                    count = count + 1
            elif (n > 5):
                if (2 < i < 6):
                    n = n-3
                    count = count + 1
                elif i < 3:
                    n= n-6
                    count = count + 1
            while n != i:
                if n < i:
                    n=n+1
                else:
                    n=n-1
                count=count+1
    return count

#Cara ke-1
#alternatif 1
#def _h(state):
#    count = 0
#    for lines in state:
#        n = state.index(lines)
#        i = goal_state.index(lines)
#        if n != i and lines is not '0':
#            count = count+1
#    return count

#alternatif 2
#def _h(state):
#    return sum([1 if state.index(i) != goal_state.index(i) and i is not '0' else 0 for i in state])


def total(state):
    return _h(state)+step

#process
initial_state = [step, None, start_state, '']
openset.__add__(initial_state)
current_state = openset.poll()
closeset.append(current_state[:])

while current_state[2] != goal_state:
    if current_state not in closeset:
        closeset.append(current_state[:])
    if current_state[2] not in visited:
        visited.append(current_state[2][:])
        step = step + 1
        searchSuccessor(current_state[2][:])
        current_state = openset.poll()
    else:
        current_state = openset.poll()
        step = step-1
closeset.append(current_state[:])
for lines in closeset:
    print(lines)
move = ""
for lines in closeset:
    move = move+lines[3]+" "
print('Move      : '+str(move))
print('Total Move: '+str(step))