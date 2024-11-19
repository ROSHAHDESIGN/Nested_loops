start_num = int(input())
end_num = int(input())
magic_num = int(input())
combination_counter = 0 #promenliva za da otbroyava

is_found = False #boolean za BREAK,akoe FALSE PREKYSVA loop-a(v koyto e)

for i in range(start_num, end_num +1):
    for j in range(start_num, end_num + 1):
        combination_counter +=1
        if i + j == magic_num:
            is_found = True
            print(f"Combination N:{combination_counter} ({i} + {j} = {magic_num})")
            break
    if is_found:
        break

if not is_found:
    print(f"{combination_counter} combinations - neither equals {magic_num}")
