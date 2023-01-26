def fatorial(k):
    fat = 1
    while k > 1:
        fat *= k
        k -= 1
    return fat

def combinacao(m,n):
    return fatorial(m) / (fatorial(m-n) * fatorial(n))

def soma(a,b):
    return a + b

def divisao(l,g):
    return l / g
