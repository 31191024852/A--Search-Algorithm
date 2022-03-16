
from collections import defaultdict
from queue import PriorityQueue

data =  defaultdict(list)
data['A'] = ['B', 6, 'G', 18, 'D', 4, 18]
data['B'] = ['C', 5, 'E', 4, 'H', 6, 9]
data['C'] = ['D', 15, 'F', 8, 11]
data['D'] = [23]
data['E'] = ['F', 7, 'G', 5, 5]
data['F'] = ['G', 3, 3]
data['G'] = [0]
data['H'] = ['G', 6, 6]

class Node:
    def __init__(self, name, par = None, g = 0 , h = 0):
        self.name = name
        self.par = par
        self.g = g
        self.h = h
    
    def display(self):
        print(self.name, self.g, self.h)
        
    def __lt__(self, other):
        if other == None:
            return False
        return self.g + self.h < other.g + other.h
    
    def __eq__(self, other):
        if other == None:
            return False
        return self.name == other.name
    
def equals(O, G):
    if O.name == G.name:
        return True
    return False
    
def checkInPriority(tmp, c):
    if tmp == None:
        return False
    return (tmp in c.queue)
    
def getPath(O):
    print(O.name)
    if O.par != None:
        getPath(O.par)
    else:
        return
                
def AStar(S, G):
    Open = PriorityQueue()
    Closed = PriorityQueue()
    S.h = data[S.name][-1]
    Open.put(S)
        
    while True:
        if Open.empty() == True:
            print('Tìm kiếm thất bại')
            return
        O = Open.get()
        Closed.put(O)
        print('Duyệt : ', O.name, O.g, O.h)
            
        if equals(O, G)== True:
            print('Tìm kiếm thành công')
            getPath(O)
            print('Distance: ', (O.g + O.h))
            return
        i=0
        while i < len(data[O.name])-1:
            name = data[O.name][i]
            g = O.g + data[O.name][i+1]
            h = data[name][-1]
            tmp = Node(name=name, g=g, h=h)
            tmp.par = O
            ok1 = checkInPriority(tmp, Open)
            ok2 = checkInPriority(tmp, Closed) 
            
            if not ok1 or not ok2:
                Open.put(tmp)
            i+=2
                  
AStar(Node('A'),Node('G'))            
        