def frequency_analysis(msg):
    fa = {}     #키는 문자, 값은 빈도수를 의미
    for c in msg:
        if c in fa:     # fa를 돌면서
            fa[c] += 1  # 값이 이미 있다면 거기에 1을 더해주고
        else:
            fa[c] = 1   # 없다면 1을 넣어준다. (첫번째 등장 이므로)
    # sorted(정렬할것, 정렬 기준, 정렬 방향)
    print(sorted(fa.items(), key=lambda x:x[1], reverse=True))

def change_test(msg):
    for c in msg:
        if c == '8':
            msg = msg.replace('8', 'e')
        if c == ';':
            msg = msg.replace(';', 't')
        if c == '4':
            msg = msg.replace('4', 'h')
        if c == '%':
            msg = msg.replace('%', 'o')
        if c == ')':
            msg = msg.replace(')', 's')
        if c == '*':
            msg = msg.replace('*', 'n')
        if c == '5':
            msg = msg.replace('5', 'a')
        if c == '6':
            msg = msg.replace('6', 'i')
        if c == '(':
            msg = msg.replace('(', 'r')
        if c == '#':
            msg = msg.replace('#', 'd')
        if c == '1':
            msg = msg.replace('1', 'f')

    print(msg)

if __name__ == '__main__':
    msg = """53%%#305))6*;4826)4%=')4%);806;48#8@60'))85;1%(;;-%*8#83(88)5*#;46(;88*96*?;8)*%(;485); 5*#2:*%(;4956*2(5*c4)8@8*;4069285);)6#8)4%%;1(%9;48081;8:8%1;48#85;4')-485#528806*81(%9;48;(88;4(%?34;484%;161;:188;%?;"""
    frequency_analysis(msg)
    print(msg)
    change_test(msg)
    
    