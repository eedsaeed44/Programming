file_name = input("Enter File Name: ")
if len(file_name) < 1:
    print("enter right name")
hand = open(file_name)

for line in hand:

    line = line.rstrip()
    # print(line)
    wds = line.split()
    # print(wds)
    # for w in wds:
    #     print(w)
    # print(wds)

    if len(wds) != 0:
        m = wds[0]
        if len(m) > 3:
            if type(m) == str:
                print(m)
    