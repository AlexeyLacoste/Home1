def can_break_chokolate(n, m, k):
    total_area = n * m
    if k > total_area or k == 0:
        return False

    return (k % n == 0) or (k % m == 0)


n = int(input("Вводим первую сторону n: "))
m = int(input("ВВодим вторую сторону m: "))
k = int(input("Вводим количество долек k: "))
if can_break_chokolate(n, m, k):
    print(" МОжно разломить шоколадку так, чтобы получить", k, " долек")
else:
    print("Невозможно разломить шоколадку так")
