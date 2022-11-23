while True:
    code = input()

    if code == "END":
        break
    else:
        code = code[::-1]
        print(code)