def spy_game(z):
    for i in range(0,len(z)):
        if z[i] == 0:

    
           for x in range(i+1,len(z)):
                if z[x] == 0:
                    for y in range(x+1,len(z)):
                        if z[y] == 7:
                            return True
                else:
                    return False
            
                                  
print (spy_game([1,2,4,0,0,7,5]))               