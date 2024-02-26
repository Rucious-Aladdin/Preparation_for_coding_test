N = int(input())
dict = {}
dict[0] = 0
dict[1] = 1
dict[2] = 1

def fibonacci(n):
    if n % 2 == 0:
        try:
            if dict[n]:
                return dict[n]
        except:
            fn = fibonacci(n // 2)
            fn_1 = fibonacci(n // 2 - 1)
            dict[n] = (fn * (fn + 2 * fn_1)) % 1_000_000_007
    else:
        try:
            if dict[n]:
                return dict[n]
        except:
            fn = fibonacci(n // 2)
            fn_1 = fibonacci(n // 2 + 1)
            dict[n] = (fn ** 2 + fn_1 ** 2) % 1_000_000_007
    
    return dict[n]    

print(fibonacci(N))
for i, e in dict.items():
    print(i, e)