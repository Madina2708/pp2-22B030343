with open("text.txt") as fd:
    with open('copy.txt', "w") as cop:
        for line in fd:
            cop.write(line)