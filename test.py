def solution(n):
    f0 =0
    f1 =1
    fn = fibo(n)
    print(fn)
    print("done")

def fibo(n):
    if n == 0:
        return 0
    elif n== 1:
        return 1
    elif (n>=3):
        fn = fibo(n-1)+fibo(n-2)
        return fn

solution(500)