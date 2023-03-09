a_list = [" маленький ", "принц"]
textfile = open("text.txt", "a")
for element in a_list:
    textfile.write(element + "\n")
textfile.close()