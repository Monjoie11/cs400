brainy_list = [1, 2, 3, 5, 7, 11]


def write_stuff(funk):
    print('{listy}'.format(listy = funk()))
    listy = funk
    for i in listy:
        print('this is some really great work, jeff. {yay:-^20.1f}'.format(yay=i))

write_stuff(list(map(lambda i: i * 3, brainy_list)))


