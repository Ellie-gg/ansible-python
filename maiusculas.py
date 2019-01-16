def maiusculas(frase):
    p = 0
    done = ''
    while p < len(frase):
        if ord(frase[p]) >= 65 and ord(frase[p]) <=90:
            done += frase[p]
        p += 1
    return done