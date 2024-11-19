from gooey import Gooey, GooeyParser

@Gooey(program_name = 'Registration')

def registration() :
    parser = GooeyParser(description = 'GUI Programing')
    
    parser.add_argument('Name', help = 'Please enter your Name :')
    parser.add_argument('Password', help = 'Please enter your password :')
    parser.add_argument('ID', help = 'Please enter your ID : ')
    args = parser.parse_args()
                
    with open('newfile.txt', 'a') as file3 :
        
        name = args.Name
        password = args.Password
        id_ = args.ID
        
        file3.write('{},{},{}'.format(name, password, id_))
        file3.write('\n')
        
        print('Registration done')
            
registration()            
            
 