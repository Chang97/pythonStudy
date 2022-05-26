# 1.정수형으로 두개의 변수 입력받음.
n, k = map(int, input().split())

# 2.변수 범위 조건.
if 1 <= k and k <= n and n <= 1000 :
    # 3. 1 ~ n + 1 배열 생성
    arr = [i for i in range(1, n + 1)]
    # 4. 제거 인덱스용 변수
    pt = 0
    # 5. 결과값용 변수
    ans = []

    # 6. n이 0이 될때 까지 삭제 반복
    for _ in range(n) :
        # 7. k 번째 사람제거 (k -1) --배열은 0부터 
        # 빈 공간도 세기 때문에 반복할때마다 2씩 추가.
        pt += k - 1
        # 8. %=을 이용하면 배열에 length를 지나쳐 앞에 인덱스를 찾을 수 있음.
        pt %= len(arr)
        # 9. 결과값 배열에 append
        ans.append(arr.pop(pt))
    # 10. f-string을 이용하여 출력.
    print(f"<{', '.join(map(str, ans))}>")
