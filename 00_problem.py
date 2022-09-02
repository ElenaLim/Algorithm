# 백준 2570번 문제: 수 정렬하기
import sys
#엔터로 줄구분하여 정수 입력
#sys.stdin.readline()을 사용하면 input()을 사용할 때보다 시간초과 위험성 줄일 수 있음

n =int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for i in range(n)]

#수 정렬
data.sort()
for i in data:
    print(i)

