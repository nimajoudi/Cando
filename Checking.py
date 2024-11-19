from gooey import Gooey, GooeyParser

@Gooey(program_name = 'Registration')

def check() :
    parser = GooeyParser(description = 'GUI Programing')
    
    parser.add_argument('Name', help = 'Please enter your Name :')
    parser.add_argument('Password', help = 'Please enter your password :')
    parser.add_argument('ID', help = 'Please enter your ID : ')
    args = parser.parse_args()
    
    with open('newfile.txt', 'r') as file3 :
        var = file3.read()
        
        if args.Name in var and args.Password in var and args.ID in var :
            print('information exists')
            
check()