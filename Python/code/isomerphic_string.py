# check if two strings are isomerphic.

def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    i, j = 0, 0
    my_dict = dict()
    for a, b in zip(s, t):
        f = my_dict.get(a)
        if f and f != b:
            return False
        else:
            if b in my_dict.values():
                return False
            my_dict[a] = b

    return True


if __name__ == "__main__":
    print(isIsomorphic("aaeaa", "uuxyy"))