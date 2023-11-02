bo_tak = []

for i in range(4):

    if i % 2 != 0:
        
        list_i = []
        
        for j in range(4):
            
            if j % 2 == 0:
                list_i.append(j + 1)
                
        bo_tak.append(list_i)
        

print(bo_tak)
