

from gooey import Gooey, GooeyParser

@Gooey(program_name = 'Calculator')

def calculator() :
    parser = GooeyParser(description = 'GUI Calculator Program')
    parser.add_argument('Name', help = 'please enter your Name : ')
    parser.add_argument('Family', help = 'please enter your Family : ')
    parser.add_argument('Number1', help = 'please enter the number : ')
    parser.add_argument('Number2', help = 'please enter the number : ')
    parser.add_argument('Operation', choices = ['add', 'sub', 'div', 'mul'], help = 'please select your operation : ')
    
    args = parser.parse_args()
    
    var_name = 'Nima'
    var_family = 'Joudi'
    
    if  var_name == args.Name and var_family == args.Family and 10 <= int(args.Number1) <= 99 and 10 <= int(args.Number2) <= 99 :
        if args.Operation == 'add' :
            var_result_add = int(args.Number1) + int(args.Number2)
            print('result is {}'.format(var_result_add)) 
        
        elif args.Operation == 'sub' :
            var_result_add = int(args.Number1) - int(args.Number2)
            print('result is {}'.format(var_result_add))  
        
        elif args.Operation == 'div' :
            var_result_add = int(args.Number1) * int(args.Number2)
            print('result is {}'.format(var_result_add)) 
        
        elif args.Operation == 'mul' :
            var_result_add = int(args.Number1) + int(args.Number2)
            print('result is {}'.format(var_result_add))
        
        else : 
            print('Invalid Input!!!!')                                                                 

calculator()





    


