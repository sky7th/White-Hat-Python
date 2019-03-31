def makePattern(p):  #문장 p의 패턴을 표준화한 결과를 리턴함
    tmp = {}         #문자에 부여한 범호를 임시로 저장하기 위한 사전 자료
    res = []         #패턴 결과를 담을 리스트 자료
    index = 0        #문자에 부여할 번호
    for c in p:
        if c in tmp:            # tmp 사전에 이미 있다면 그 값을 사용
            res.append(tmp[c])
        else:                   # tmp 사전에 없다면 index 번호로 새로 추가
            tmp[c] = str(index)
            res.append(str(index))
            index += 1          # 유일성을 위해 1 더해줌
    return ';'.join(res)        # 1012131414 (엉망)   10;12;13;14;14 (구분)

def findPattern(msg, p):             # msg에서 1자씩 움직여가며 p와 동일한 패턴을 스캔하고 p와 동일한 부분을 찾으면
    pattern = makePattern(p)         #더이상 스캔하지 않고 해당 부분을 리턴한다
    blocksize = len(p)
    pos = 0
    while True:
        data = msg[pos:pos+blocksize]   # msg 를 p의 패턴길이 만큼씩 처음부터 쭉 돈다. 0 ~ 패턴길이, 1 ~ 1+패턴길이, ....
        if len(data) < blocksize:       # 돌다가 패턴길이 만큼 설정할 수 없을 때 탈출, (마지막 즈음에 탈출)
            break

        ptrn = makePattern(data)        # msg 의 패턴길이 만큼을 패턴화 한다.
        if ptrn == pattern:             # msg 의 부분 패턴과 p패턴이 같으면
            return data                 # msg 의 그 부분을 리턴
            break
        pos += 1

if __name__ == '__main__':
    msg = "53%%#305))6*;4826)4%=')4%);806;48#8@60'))85;1%(;;-%*8#83(88)5*#;46(;88*96*?;8)*%(;485); 5*#2:*%(;4956*2(5*c4)8@8*;4069285);)6#8)4%%;1(%9;48081;8:8%1;48#85;4')-485#528806*81(%9;48;(88;4(%?34;484%;161;:188;%?;"
    known_plaintext = ['goodglass', 'mainbranch']
    for p in known_plaintext:
        ret = findPattern(msg, p)
        print('[%s] = [%s]' %(p, ret))
        
        