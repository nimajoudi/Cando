from gooey import Gooey, GooeyParser

@Gooey(program_name = 'Calculator')

def calculator() :
    name = input('Please enter your name : ')
    family = input('Please enter your family : ')
    parser = GooeyParser(description = 'GUI Calculator Program')
    parser.add_argument('Name', help = 'please enter your Name : ')
    parser.add_argument('Family', help = 'please enter your Family : ')
    parser.add_argument('Number1', help = 'please enter the number : ')
    parser.add_argument('Number2', help = 'please enter the number : ')
    parser.add_argument('Operation', help = 'please enter the operation : ')
    args = parser.parse_args()

    if str(args.Name) != name and str(args.Family) != family :
        print('Error!!! : Name or Family is incorrect')

    elif int(args.Number1) and int(args.Number2) not in range (10, 99) :
        print('Error!!! : Invalid numbers')

    elif args.operation not in ('+', '-', '*', '/', '//', '**') :
        print('Error!!! : Invalid operation')
    
    elif args.operation == '+' :
        print(args.Number1, '+', args.Number2, '=', int(args.Number1) + int(args.Number2))
    
    elif args.operation == '-' : 
        print(args.Number1, '-', args.Number2, '=', int(args.Number1) - int(args.Number2))

    elif args.operation == '*' : 
        print(args.Number1, '*', args.Number2, '=', int(args.Number1) * int(args.Number2))

    elif args.operation == '**' : 
        print(args.Number1, '**', args.Number2, '=', int(args.Number1) ** int(args.Number2))

    elif args.operation == '/' : 
        print(args.Number1, '/', args.Number2, '=', int(args.Number1) / int(args.Number2))

    elif args.operation == '//' : 
        print(args.Number1, '//', args.Number2, '=', int(args.Number1) // int(args.Number2))

calculator()


    


