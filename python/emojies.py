emojies = {
    ':)' : '😀',
    ':(' : '😔'
    }



words = input('Enter u r emotions: ')
word = words.split()
print(word)

result = ''
for i in range(len(word)):
    if i == emojies[i]:
        print('')
    



