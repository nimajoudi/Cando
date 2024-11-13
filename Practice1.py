from gooey import Gooey, GooeyParser

@Gooey(program_name = 'Even and Odd Numbers')

def main() : 

    parser = GooeyParser(description = 'GUI Programing')
    
    parser.add_argument('Number1', help = 'please enter the number : ')
    parser.add_argument('Number2', help = 'please enter the number : ')
    parser.add_argument('Number3', help = 'please enter the number : ')
    parser.add_argument('Number4', help = 'please enter the number : ')
    args = parser.parse_args()
    if args == '' :
        print('Error!!! : Number is empty')

    if int(args.Number1) % 2 == 0 :
        print(args.Number1, ' : is Even')
    else :
        print(args.Number1, ': is Odd')
    if int(args.Number2) % 2 == 0 :
        print(args.Number2, ' : is Even')
    else :
        print(args.Number2, ' : is Odd')
    if int(args.Number3) % 2 == 0 :
        print(args.Number3, ' : is Even')
    else :
        print(args.Number3, ' : is Odd')
    
    if int(args.Number4) % 2 == 0 :
        print(args.Number4, ' : is Even')
    else :
        print(args.Number4, ' : is Odd')
    
    
main()


