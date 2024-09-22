import sys
n = int(sys.stdin.readline())
input_str = sys.stdin.readline().rstrip()

dct={'000000': 'A', 
    '001111': 'B', 
    '010011': 'C', 
    '011100': 'D', 
    '100110': 'E', 
    '101001': 'F', 
    '110101': 'G', 
    '111010': 'H' }

result=''
now=0
check=True
for idx in range(0, 6*n, 6):
    # print(input_str[idx:idx+6])
    if input_str[idx:idx+6] in dct.keys():
        result += dct[input_str[idx:idx+6]]
    else:
        # 1개만 다른 숫자 있는지 체크
        # 없으면 결과 출력
        for i in dct.keys():
            cnt=0
            for j in range(6):
                if i[j] != input_str[idx:idx+6][j]:
                    cnt+=1
            if cnt < 2:
                result += dct[i]
                check=True
                break
            else:
                check=False
        
        if not check:
            break
    if check:
        now+=1
    else:
        break

if check:
    print(result)
else:
    print(now+1)