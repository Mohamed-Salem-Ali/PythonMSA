if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    final=[]
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                a1=[i,j,k]
                if i+j+k != n:
                    final.append(a1)
    final = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]


    print(final)
                    
