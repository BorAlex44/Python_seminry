
with open('seminar4.txt', 'r') as file_1:
    count1 = sum(1 for _ in file_1)

with open('seminar4_5.txt', 'r') as file_2:
    count2 = sum(1 for _ in file_2)

if count1 != count2:
    print("The contents of the files do not match!")
else:
    with open('seminar4.txt', 'r') as file_1:
        with open('seminar4_5.txt', 'r') as file_2:
            with open('sum_file.txt', 'a') as file_3:
                while True:
                    line_1 = file_1.readline()
                    line_2 = file_2.readline()
                    new_line = line_1.replace("= 0\n", " + ") + line_2
                    file_3.write(f'{new_line}\n')
                    if not line_1:
                        break
