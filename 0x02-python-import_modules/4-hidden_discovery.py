#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    names.sort()

    for n in names:
        if n[0:2] != "__":
            print(n)
