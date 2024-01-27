#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    text = dir(hidden_4)
    for name in text:
        if name[0] != "_" and name[1] != "_":
            print(name)
