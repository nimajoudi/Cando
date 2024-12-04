
from gooey import Gooey, GooeyParser
from random import randint
import math

@Gooey(program_name = 'Multi Tab Program')

def main(): 
    parser = GooeyParser()
    
    sp = parser.add_subparsers(dest = 'for_test')
    ap = sp.add_parser('Introduction')
    ag = ap.add_argument_group('Statement')
    ag.add_argument('Description', widget = 'Textarea', gooey_options = {'initial_value':
    'Hello dear User\n\nRandom Number : In this tab, you can play a game with pc.\n\nOdd_Even : With this tab when you enter a number you can find that the number is odd or even.\n\nRegistration : Here you must enter your full name and password to sign up.\n\nChecking Registration : After you signed up your information will save in uor data base.\nSo in this thab you can check your information exists or not.\n\nCalculator : You can enter 2 numbers then calculate.'
    , 'height':500, 'readonly':True})
    
    ap1 = sp.add_parser('Random_Number')
    ap1.add_argument('Number', help = 'Please enter a Number')
    
    ap2 = sp.add_parser('Odd_Even')
    ap2.add_argument('Number1', help = 'Please enter a Number')
    
    ap3 = sp.add_parser('Registration')
    ap3.add_argument('User_Name', help = 'Please enter your full name')
    ap3.add_argument('Password', help = 'Please enter your Password')
    
    ap4 = sp.add_parser('Checking_Registration')
    ap4.add_argument('user_name', help = 'Please enter your full name')
    ap4.add_argument('password', help = 'Please enter your Password ')
    
    ap5 = sp.add_parser('Calculator')
    ap5.add_argument('number1', help = 'Please enter a Number')
    ap5.add_argument('number2', help = 'Please enter a Number')
    ap5.add_argument('Operation', choices = ['add', 'sub', 'div', 'mul', 'sqrt'], help = 'Please select your operation')
    
    
    
    args = parser.parse_args()
    
    return args 

def Random_Number(Number) :
    
    pc_input = randint(1,10)
    
    if int(Number) < pc_input : 
        print(f'Wrong guess {Number} < Adad e morede nazar')
        
    elif int(Number) > pc_input :
        print(f'Wrong guess {Number} > Adad e morede nazar')
                            
    else:
        print(f'Wll done Your guess : {Number} and PC number : {pc_input}' , sep='\n')


def Odd_Even(Number1) :
    
    if int(Number1) % 2 == 0 :
        print(f'{Number1} is Even')
    
    else :
        print(f'{Number1} is Odd')
        
        
def Registration(User_name, Password) :
    
    with open('Registration.txt', 'a') as file :

        file.write(f'{User_name},{Password}')
        file.write('\n')
    
    print('Registration done')


def Checking_Registration(user_name, password) :
    with open('Registration.txt', 'r') as file :
    
        var = file.read()
        
        if user_name in var and password in var :
            print('information exists')
            
        else :
            print('This Information does not exist')    
            

def Calculator(number1, number2, Operation) :
    
        if Operation == 'add' :
            var_result_add = int(number1) + int(number2)
            print('result is {}'.format(var_result_add)) 
        
        elif Operation == 'sub' :
            var_result_add = int(number1) - int(number2)
            print('result is {}'.format(var_result_add))  
        
        elif Operation == 'div' :
            var_result_add = int(number1) * int(number2)
            print('result is {}'.format(var_result_add)) 
        
        elif Operation == 'mul' :
            var_result_add = int(number1) + int(number2)
            print('result is {}'.format(var_result_add))
            
        else :
            print(f'{number1} : {math.sqrt(number1)} and {number2} : {math.sqrt(number2)}')  
    
complexity = main()

if complexity.for_test == 'Random_Number' :
    Random_Number(complexity.Number)
    
elif complexity.for_test == 'Odd_Even' :
    Odd_Even(complexity.Number1)

elif complexity.for_test == 'Registration' :
    Registration(complexity.User_Name, complexity.Password)

elif complexity.for_test == 'Checking_Registration' :
    Checking_Registration(complexity.user_name, complexity.password)

else :
    Calculator(complexity.number1, complexity.number2, complexity.Operation)