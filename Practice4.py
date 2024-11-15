from random import randint

def guess_number() :
    
    pc_input = randint(1, 10)
    
    while True :
        user_guess = int(input('Please enter your guess number : '))
        system('clear')
                
        if user_guess < pc_input : 
            print('Wrong guess', user_guess , '< Adad e morede nazar')
                                        
        elif user_guess > pc_input :
            print('Wrong guess', user_guess , '> Adad e morede nazar')
                            
        else:
            print('Wll done','Your guess : ', user_guess, 'PC number : ', pc_input, sep='\n')
            break

guess_number()            
