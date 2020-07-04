from itertools import chain, combinations

def powerset(s):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def disjointsets(iterable1, iterable2):
    total=0
    for a in iterable1:
        for b in iterable2:
            if set(a).isdisjoint(set(b)):
                print(a,b)
                total+=1
    print("Number of ordered pairs with disjointsets=",total)

def subset1(iterable1, iterable2):
    total=0
    for a in iterable1:
        for b in iterable2:
            if set(a).intersection(set(b))=={1}:
                print(a,b)
                total+=1
    print("Number of ordered pairs with A intsersection B {1}=",total)

superset ={1,2,3,4,5}
data = powerset(superset)

subsets = set(data)
print("Number of subsets=",len(subsets))
disjointsets(subsets,subsets)
subset1(subsets,subsets)

