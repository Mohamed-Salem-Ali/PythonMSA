if __name__ == '__main__':
    raw_input()
    nPut = map(int, raw_input().strip().split(" "))
    print hash(tuple(nPut))