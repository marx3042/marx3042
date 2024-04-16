def fibonachi(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else :
        return fibonachi(num-1) + fibonachi(num-2)

num = int(input())
print(fibonachi(num))