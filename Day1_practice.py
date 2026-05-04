num = 3
alphabet = "abcdefghijklmnopqrstuvwxyz"
for j in range(num-1, -1, -1):
    left = [alphabet[i] for i in range(num-1, j-1, -1)]
    right = [alphabet[i] for i in range(j+1, num)]
    sequence = left + right
    print("-".join(sequence))
for k in range(1, num):
    left = [alphabet[i] for i in range(num-1, k-1, -1)]
    right = [alphabet[i] for i in range(k+1, num)]
    sequence = left + right
    print("-".join(sequence))