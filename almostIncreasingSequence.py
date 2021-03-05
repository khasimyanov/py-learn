# https://app.codesignal.com/arcade/intro/level-2/2mxbGwLzvkTCKAJMG
def almostIncreasingSequence(sequence):
    flag = True 
    for i in range(len(sequence)):
        count = 1
        d = sequence[0:i] + sequence[i+1:]
        print(d)
        for j in range(1,len(d)):
            if d[j] <= d[j-1]:
                count += 1
                flag = False
                break
        if count == 1:
            flag = True
            break
    return flag     