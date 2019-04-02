def makeDisk(key):                        
    dec_disk = {}                       # dec_disk 라는 공간을 만듬 (딕셔너리) decoding = 복호화
    for i in range(26) :                # For i in range(26) 은 for (int i=0; i<26; i++) 와 같음, A ~ Z 까지 맵핑해주기 위함
        alp = (i+key) % 26 + 65         # ASCII 코드 65는 알파벳 A 를 의미, 66은 B, 67 은 C,… 
        dec_disk[chr(alp)] = chr(i+65)  # ex) {(C,A),(D,B),(E,C)...(B,Z)}
    return dec_disk                     # 복호화 하는 dec_disk 를 반환

def caesar(msg, key):                   
    ret = ''                # 복호화된 문장 저장하는 곳                  
    msg = msg.upper()       # 대문자로 바꿈
    disk = makeDisk(key)    # dec_disk 한 줄을 받음
    for c in msg:           # msg 를 쭉 돈다
        if c in disk:       # msg 를 돌다가 해당 부분이 disk에 있으면
            ret += disk[c]  # 그 key 값의 value 값을 ret에 추가 (복호화된 문장 만들어 가기)
        else:
            ret += c        # 알파벳이 아니라면 ret에 그냥 추가
    return ret

def attack(msg):
    for key in range(1, 26):        # 위의 과정을 알파벳 만큼 26번 반복하여 모든 경우의 수를 출력
        decmsg = caesar(msg, key)
        print('SHIFT[%d]: %s' %(key, decmsg))
        
if __name__=='__main__':
    msg = 'UGAMKZMBSMGQAVCUJMZBPZMMNQDMWVMBPZMM'    # 암호문
    attack(msg)
    
