import random, string
import uuid
import argparse 
from datetime import datetime as dt

from Levenshtein import distance as lev

alphabet = string.ascii_letters

def randword(k):
    return ''.join([random.choice(alphabet) for i in range(0,k)])

def get_random_edges(minds, edge_prob):
    edges = []
    for i in range(0, len(minds)):
        for j in range(0, len(minds)):
            if i != j and random.random() > (1-edge_prob):
                edges.append((minds[i], minds[j]))
    return edges

def select_meme(mind):
    return random.choice(mind.imemes)

def mutate(meme):
    mut_prob = 0.5
    mutated = []
    for c in meme:
        if random.random() > (1-mut_prob):
            mutation = random.choice(alphabet)
            mutated.append(mutation)
        else:
            mutated.append(c)
    return ''.join(mutated)

def similarity(ememe, imeme):
    return lev(ememe, imeme) / len(imeme) 

class Mind():
    def __init__(self, p, k):
        self.p = p
        self.id = uuid.uuid1()
        self.imemes = [ randword(k) for i in range(0, p) ]

    def receive(self, ememe):
        min_distance = 0.5
        for imeme in self.imemes:
            distance = similarity(ememe, imeme)
            if distance > min_distance:
                self.imemes.append(ememe) 
                break

    def forget(self):
        if len(self.imemes) > self.p:
            self.imemes.remove(random.choice(self.imemes))

def get_less_similar(memes):
    last_dist = 0
    less_similar = None
    for candidate in memes:
        dist = 0
        for m in memes:
            dist += similarity(candidate, m)
        if less_similar == None or last_dist == 0 or dist < last_dist:
            less_similar = candidate
            last_dist = dist
    return less_similar

class MindFit(Mind):
    def receive(self, ememe):
        self.imemes.append(ememe)

    def forget(self):
        while len(self.imemes) > self.p:
            toforget = get_less_similar(self.imemes) 
            self.imemes.remove(toforget)
            
class Graph():
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

def main():
    parser = argparse.ArgumentParser(description='Memetic simulation')
    parser.add_argument('-e', '--epochs', dest='epochs', action='store', default='1000', type=int)
    args = parser.parse_args()

    N = 1000;
    k = 10;
    p = 10;
    edge_prob = 0.5

    #minds = [ Mind(p, k) for i in range(0, N) ]
    minds = [ MindFit(p, k) for i in range(0, N) ]
    [ print(m.imemes) for m in minds ]
    
    timestamp = str(dt.now()).replace(' ', '_')
    epoch = 0
    with open(f'memesim_{N}_{k}_{p}_{edge_prob}_{timestamp}.csv', 'w') as file:
        file.write('epoch;id;imeme\n')
        while epoch <= args.epochs:
            epoch += 1
            graph = Graph(minds, get_random_edges(minds, edge_prob)) 
            for edge in graph.edges:
                sender = edge[0]
                receiver = edge[1]
                ememe = mutate(select_meme(sender))
                #ememe = select_meme(sender)
                receiver.receive(ememe)
                receiver.forget()      
            for m in minds:
                for imeme in m.imemes:
                    data = f'{epoch};{m.id};{imeme}\n'
                    file.write(data)

if __name__=='__main__':
    main()
        
