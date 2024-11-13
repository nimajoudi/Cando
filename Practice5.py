from os import system
from random import randint

def register_user():
    users = {}
    for i in range(2):
        username = input(f"Please enter the username {i+1}: ")
        password = input(f"Please enter the password (just Number) {i+1} : ")
        
        if not password.isdigit():
            print("Error!!! : Invalid Password.")
            return
        
        users[username] = password
    
    print("Registration is done.")
    for username, password in users.items():
        print(f"Username: {username}, Password: {password}")
        


    user_score = 0
    pc_score = 0
    game_count = 0
    guess_count = 0

    while user_score < 5 and pc_score < 5:

        # region pc input
        
        pc_input = randint(1, 100)

        # endregion

        # region guess number
       
        while True :    
            user_guess = int(input('Please enter your guess number : '))
            system('clear')
            guess_count += 1
        
            if user_guess < pc_input : 
                print('Wrong guess', user_guess , '< Adad e morede nazar')
                pc_score += 1
                        
            elif user_guess > pc_input :
                print('Wrong guess', user_guess , '> Adad e morede nazar')
                pc_score += 1
                        
            else:
                print('Wll done','Your guess : ', user_guess, 'PC number : ', pc_input, sep='\n')
                user_score+= 1 
                break
                        
        #endregion
        
register_user()        
          