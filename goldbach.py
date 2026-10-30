from priem_getal import is_priem

def even_getallen(N: int) -> None:
    for i in range(4, N, 2):
        i_found = False
        for j in range(2, i):
            if i_found == True:
                    break
            for k in range(2, i):
                if j + k == i and is_priem(j) == True and is_priem(k) == True:
                    print(f"{i} = {j} + {k}")
                    i_found = True
                    break
                    
        
                
                
            
        
        

if __name__ == '__main__':
    even_getallen(20)