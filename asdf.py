def calc(a, b):
    try:
        res = a/b
    except:
        return -1
    return res

ans = calc(10, 0)
if ans == -1:
    print('Errrrrooooorrrr')
else:
    print('Result = %f' %ans)

