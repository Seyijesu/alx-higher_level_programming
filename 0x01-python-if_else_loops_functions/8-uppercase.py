#!/usr/bin/python3
def uppercase(str):
    for i in str:
        setoffs = 0
        if ord(i) > 96 and ord(i) < 123:
            setoffs = -32
        print("{}".format(chr(ord(i) + setoffs)), end="")
    else:
        print()
