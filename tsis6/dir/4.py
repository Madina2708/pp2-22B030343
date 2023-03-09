fpath="./text.txt"
with open(fpath, 'r') as fp:
    lines = len(fp.readlines())
    print(' Number of lines:', lines)