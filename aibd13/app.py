def bubblesort(I):
    nb = 0
    Ip = list(I)
    n = len(Ip)
    while n > 1:
        i = 1
        for i  in range(1,n):
            if Ip[i - 1] > Ip[i]:
                Ip[i - 1], Ip[i] =  Ip[i], Ip[i - 1]
            nb += 1
        n = n - 1
    return Ip