# produce all possible oligos of a primer sequence with degenerate nucleotides 

import itertools # computes cartesian product of input iterables
import os


choice = 'Y'
while choice == 'Y':
    degnuc = {'A':'A', 'T':'T', 'C':'C', 'G':'G', 'R':['A','G'], 'Y':['C','T'], 'S':['G','C'],
            'W':['A','T'], 'K':['G','T'], 'M':['A','C'],
            'B':['C','G','T'], 'N':['A','T','C','G']}
            
    seq = raw_input('Enter degenerate primer sequence: ').upper()
    
    seqchk = list(seq)
    for x in seqchk:
        if x not in degnuc.keys():
            print "Invalid Input"
            break
        else:
            continue


    def multi_replace(seq, degnuc):
        indexes, replacements = zip(*[(i, degnuc[c]) for i, c in enumerate(seq) if c in degnuc])
    
        l = list(seq) # turn input into mutable object 
       
        # iterate over cartesian product of all replacement tuples  
        
        for p in itertools.product(*replacements):
            for index, replacement in zip(indexes, p): 
                l[index] = replacement
            yield ''.join(l)

    for perm in multi_replace(seq, degnuc):
        print perm
            
    choice = raw_input('Enter another sequence? \n(Y/N): ').upper()
    if choice == 'N':
        os.system('exit')
