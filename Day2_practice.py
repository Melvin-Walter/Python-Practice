target = 10
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
left = 0
right = len(num_list)-1
last_op = "left"
current_sum = num_list[left] + num_list[right]
while right > left:
    if current_sum < target:
        left += 1
        last_op = "left"
    elif current_sum > target:
        right -= 1
        last_op = "right"
    else:
        print(f"The indices are {left} and {right}")
        if last_op == "left":
            right-= 1
        else:
            left += 1
        current_sum = num_list[left] + num_list[right]
        continue
    current_sum = num_list[left] + num_list[right]