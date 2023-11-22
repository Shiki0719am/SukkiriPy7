file = open("diary.txt",'r',encoding="UTF-8")
for line in file:
    print(line)
    with open("copy.txt","a",encoding="UTF-8") as copy_file:
        copy_file.write(line + "\n")
file.close()