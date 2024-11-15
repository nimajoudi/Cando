from colorama import init, Style, Fore , Back

def function1 () : 
    
    var_input = int(input('Please enter the Number1 (6-10) : '))
    var_input2 = int(input('Please enter the Number2 (6-10) : '))
    
    if 6 <= var_input <= 10 and 6 <= var_input2 <= 10 :
        var_list = []
        
        for i in range (1, var_input + 1) :
            if i == 2 :
                continue
            
            else :            
                for j in range (1, var_input2 + 1) :
                    if j == 2 :
                        continue
                    
                    elif j == 4 :
                        print(Fore.RED + str(i*j), end = '  ' + Style.RESET_ALL)
                        
                        var_list.append(i*j)    
                        
                        
                    else : 
                        print(Fore.YELLOW + str(i*j), end = '  ')
                        
                        var_list.append(i*j)    
                    
            
            print()
            
        return var_list
        
    else : 
        print('Invalid input')
        
var_result_func1 = function1()   

print(var_result_func1)   


def even (var_result_func1) :
    list_function2 = []
    
    for z in range(len(var_result_func1)) :
        # print(z)
        if var_result_func1[z] % 2 == 0 :
            list_function2.append(z)
            
    print(list_function2)        
        
even(var_result_func1) 
