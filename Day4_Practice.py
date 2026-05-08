num_list = [1, 2, 5]
for r in range(1, num_list[-1]+1):
    if r != num_list[r-1]:
        print(r)
        num_list.insert(r-1, r)


word = "hello"
splitword = [*word]
splitword = "".join([chr(ord(i) + 3) for i in splitword])

num_list1 = [1, 3, 5]
num_list2 = [2, 4, 6]
new_list = sorted(num_list1 + num_list2)

sentence = ("the cat and the dog".lower()).split()
sentence_dict = {}
for i in sentence:
    if i in sentence_dict:
        sentence_dict[i] += 1
    else:
        sentence_dict[i] = 1
print(sentence_dict)

number = 37
prime = "True"
for i in range(2, (number +1)//2):
    if number%i == 0:
        print("Not a prime number")
        prime = "False"
        break
    else:
        pass
if prime == "True":
    print("Prime number")