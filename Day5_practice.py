sentence = "Gojo Satoru is the strongest man alive"
sentence = sentence.split()
longest_word = [sentence[0]]
for i in sentence:
    if len(i) > len(longest_word[0]):
        longest_word.clear()
        longest_word.append(i)
    elif len(i) == len(longest_word[0]):
        longest_word.append(i)
    else:
        pass


list1 = list(range(1, 10))
even = [i for i in list1 if i % 2 == 0]
odd = [i for i in list1 if i % 2 != 0]
list1 = even + odd

list1 = [1, 2, 3, 4, 5]
k = 2
list2 = []
for i in range(len(list1)):
    list2.append(list1[i-k])

list1 = [1, 3, 5, 7, 9]
num = 7
found = False
check = len(list1)//2
while found == False:
    check = len(list1)//2
    if num > list1[check]:
        del list1[0:check+1]
    elif num == list1[check]:
        print(check)
        found = True
    else:
        del list1[check:]
    