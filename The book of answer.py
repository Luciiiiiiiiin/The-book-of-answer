import time, random
print('Welcome, stranger. This is THE BOOK OF ANSWER!')
while True:
    print('what is your question?')
    answer = input()
    print('Very good. Your question will be answered in a few seconds')
    dot = '.'
    for i in range(5):
        print(dot)
        dot += '.'
        time.sleep(1)
    messages = ['It is certain',
        'It is decidedly so',
        'Yes definitely',
        'Reply hazy try again',
        'Ask again later',
        'Concentrate and ask again',
        'My reply is no',
        'Outlook not so good',
        'Very doubtful']
    print(messages[random.randint(0, len(messages) - 1)])
    print('Would you like to raise an another question? ()')
    n = input()
    if n == 'Y':
        continue
    else:
        break
print('Good bye!')



