names = ['jenn', 'Nancy', 'larry', 'scary Larry', 'mark e mark', 'david', 'josephiNe', 'betina', 'inglebert']


print(names)


def get_nnames(listy):
    for i in range(len(listy)):
        if(len(listy[i]) > 5):
            if('n' in listy[i] or 'N' in listy[i]):
                print(listy[i])


get_nnames(names)

measured = len(names)

while(measured > 0):
    names.pop()
    print(names)
    measured = len(names)

