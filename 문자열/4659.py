vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    pwd = input()
    if pwd == "end":
        break

    _pwd = list(pwd)
    v_flag = 0  # 모음이 존재하는지
    v_cnt = 0  # 모음 3개가 연속으로 존재하는지
    c_cnt = 0  # 자음 3개가 연속으로 존재하는지
    error = 0  # 같은 글자가 연속으로 존재하는지, 모음/자음의 3개 연속인지

    for i in range(len(_pwd)):
        if i > 0:
            if _pwd[i] == _pwd[i-1]:
                if _pwd[i] != 'e' and _pwd[i] != 'o':
                    error = 1
                    break

        if _pwd[i] in vowel:
            v_flag = 1
            v_cnt += 1
            c_cnt = 0
            if v_cnt == 3:
                error = 1
                break
        else:
            v_cnt = 0
            c_cnt += 1
            if c_cnt == 3:
                error = 1
                break

    if (error != 1) and (v_flag == 1):
        print("<" + pwd + "> is acceptable.")
    else:
        print("<" + pwd + "> is not acceptable.")