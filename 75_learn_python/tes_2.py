matrix = [
    [1,2,-1,-4,-20],
    [-8,-3,4,2],
    [3,8,10,1,3],
    [-4,-1,1,7,-6],
    ]

constraint = 29

def bruteForce(m, c):
    if len(m[0]) == 1 and len(m) == 1:
        return m[0][0]
    