import ccrypt

def findPass(passhash, dictfile):	
	salt = passhash[3:5]                           # passhash의 3,4 번째 문자가 salt 이다.
	with open(dictfile, 'r') as dfile:             # dictionary.txt 파일을 연다. 이것을 dfile에 저장
		for word in dfile.readlines():             # dfile 의 내용을 한 줄씩(한 단어) 읽는다.
			word = word.strip('\n')                # word 에 있을지도 모르는 '\n' 을 제거한다.
			cryptwd = ccrypt.crypt(word, salt)     # ccrypt 모듈의 crypt() 함수로 해시를 계산
			if cryptwd == passhash[3:]:            # 일치하는지 검사하고 일치하면 그 word를 리턴한다.
				return word
	return ''
	
def main():	
	dictfile = 'dictionary.txt'                    # dictionary.txt 파일을 dictfile 로 명명
	with open('passwords.txt', 'r') as passFile:   # passwords.txt 파일을 연다. 이것을 passFile에 저장
		for line in passFile.readlines():          # passFile 의 내용을 한 줄씩 읽는다.
			data = line.split(':')                 # 해당 줄을 ':' 를 기준으로 나눠서 data 에 배열 형태로 저장
			user = data[0].strip()                 # data[0] 에 있을지도 모르는 공백을 제거한 후 순수 이름만 저장
			passwd = data[1].strip()               # 패스워드도 마찬가지
			word = findPass(passwd, dictfile)
			if word:
				print('FOUND Password: ID [%s] Password [%s]' %(user, word))
			else:
				print('Password Not Found!')
		
if __name__ == '__main__':
	main()
    
