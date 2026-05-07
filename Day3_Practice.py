#Vowel tracker
vowels = "aeiou"
word = "Race car".lower()
count = 0
vowel_dict = {}
for i in word:
    if i in vowels:
        count += 1
        if i not in vowel_dict:
            vowel_dict[i] = 1
        else:
            vowel_dict[i] += 1
print(count)
print(vowel_dict)

#Palindrome checker
word = "race car"
word = "".join(word.split()).lower()
if word[::-1] == word:
    print("Yes it a palindrome")
else:
    print("Nope it isnt a palindrome")

#Frequency counter
num_list = ["1", "1", "2", "3", "3"]
num_dict = {}
for i in num_list:
    if i in num_dict:
        num_dict[i] += 1
    else:
        num_dict[i] = 1
        
num_dict["max"] = max(num_dict, key=num_dict.get)
print(num_dict)