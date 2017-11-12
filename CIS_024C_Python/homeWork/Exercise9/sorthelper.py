
def sortList(num_List):      
    int_Converted = []
    sorted_List = []
    
    for i in range(1, len(num_List)):
        int_Converted.append(int(num_List[i]))
        
    original_Len = len(int_Converted) 
        
    while len(sorted_List) < original_Len:  
        sorted_List.append(int_Converted.pop(int_Converted.index(min(int_Converted)))) 
        
    return sorted_List