if __name__ == '__main__':
    n = int(raw_input())
    t = map(int, raw_input().split())
    t=tuple((t))

    print(hash(t))
