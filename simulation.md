Organism:
    Set of random features (bit strings, i-memes) with fixed length.
    each incoming e-meme is evaluated: if it matches an existing one, over a certain threshold of matching bits, it's added to the set.

Process:
    - generate N sets of length p of random w words of length k
    - generate a random graph of communication
        - TODO define rules for a dynamic evolution of the communication
    - for each arc in the graph between n1 and n2: 
        - either n1 sends an ememe to n2, or n1 sends an ememe to n1
        - given a matching function for memes M(m1, m2)
        - given word w as an ememe for node n, mutate it according to function C(w), yielding ememe m  
        - add ememe m to node n2 according to some function f       
        - evict an imeme from n according to some function g

Track:
    epoch | mind_id | single imeme 

    TODO: edges ???

Proposed f,g and C
    - f: if at least one m' with m' in n imemes M(m, m') > threshold t, add m to n imemes
    - g: remove randomly until you get length of set p
    - C: randomly mutate each character with probability q 

    - f: add normally
    - g: remove the least fit meme until you get length of set p, calculating fitness as similarity to the whole set (Levensthein distance)
    - C: randomly mutate each character with probability q 

