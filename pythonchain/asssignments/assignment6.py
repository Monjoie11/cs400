import pickle
import json

repeat = True
choice = ''


def load_history():
    with open('blockchain.txt', mode='rb') as f:
        global file_content
        file_content = pickle.loads(f.read())
        return file_content

prose = load_history()

while repeat:
    print('want to write stuff?: 1')
    print('want to see what you\'ve written?: 2')
    print('want to go be sad and lonely without me in your life?: 3')
    choice = input('make a decision already!')
    if choice == '1':
        words = input('stroke that keyboard')
        print('yeah, that\'s the good stuff')
        prose.append(words)
        with open('blockchain.txt', mode='wb') as f:
            f.write(pickle.dumps(prose))
        
    elif choice == '2':
        # with open('blockchain.txt', mode='rb') as f:
        #     file_content = pickle.loads(f.read())
        i = 0
        for entry in prose:
            i += 1
            print(f'entry {i}: ', entry)

             

    elif choice == '3':
        print('farewell, cruel cruel world')
        repeat = False
        

    