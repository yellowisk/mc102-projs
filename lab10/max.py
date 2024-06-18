def find_max(list, size):        
    if size == 1:                                 
        return list[size-1]                                                          
    else:                                                                      
        previous = find_max(list, size-1)                        
        current = list[size-1]                                                     
        if previous > current:                                                 
            return previous                                                    
        else:                                                                  
            return current 
to_be_ran = list(map(int, input().split()))
print(find_max(to_be_ran, len(to_be_ran)))
