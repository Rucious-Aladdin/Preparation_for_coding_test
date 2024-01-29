#recursive

def fibo(n):
    global n_call
    
    print(n_call)
    n_call += 1
    if n == 0 or n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
    
n_call = 1
print(fibo(25))