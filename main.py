vowels = ['a', 'e', 'i', 'o', 'u']


def get_rythm(line: str) -> str:
    last_word = line.split(' ')[-1].lower()
    for i in range(len(last_word) - 1, -1, -1):
        c = last_word[i]
        if c in vowels:
            if c == last_word[-1]:
                return c
            else:
                return last_word[i + 1:]
    return last_word


def get_poetry_type() -> str:
    rythms = [None]*4
    for i in range(4):
        line = input()
        rythm = get_rythm(line)
        rythms[i] = rythm
    if rythms[0] == rythms[1] == rythms[2] == rythms[3]:
        return 'perfect'
    if rythms[0] == rythms[1] and rythms[2] == rythms[3]:
        return 'even'
    if rythms[0] == rythms[2] and rythms[1] == rythms[3]:
        return 'cross'
    if rythms[0] == rythms[3] and rythms[1] == rythms[2]:
        return 'shell'
    return 'free'


n = int(input())
for i in range(n):
    print(get_poetry_type())
