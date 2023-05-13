import itertools as it

arr = [1,2,3]

print(list(it.combinations(arr,len(arr))))
print(list(it.permutations(arr,len(arr))))

