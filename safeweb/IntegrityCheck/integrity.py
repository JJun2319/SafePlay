def checksum():
    from Crypto.Hash import SHA256 as SHA
    SIZE = 1024*256
    def getFileHash(filename):  #입력된 파일을 256KB씩 읽어 해시 값을 만들어 연속적으로 갱신하고 최종 해시 값을 리턴
        hash = SHA.new()
        h = open(filename, 'rb')
        content = h.read(SIZE)
        while content:
            hash.update(content)
            hashval = hash.digest()
            content = h.read(SIZE)
        h.close()
        return hashval

    def hashCheck(file1, file2):  #file1, file2 에 대해 각각 getFileHash를 호출하여 파일에 대한 해시값을 계산하고 비교함
        hashval1 = getFileHash(file1)
        hashval2 = getFileHash(file2)
        if hashval1 == hashval2:
            print('Two Files are Same')
        else:
            print('파일이 손상되었을수도 있습니다.')
            
    def main():
        file1 = 'IntegrityCheck\plain.txt'
        file2 = 'IntegrityCheck\plain.pre'
        hashCheck(file1, file2)
        
        
    if __name__ == '__main__':
        main()
