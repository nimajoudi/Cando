# برنامه ای بنویسید: (به کمک توابع و گرافیکی نباشد)
# اگر کاربر عدد یک را تایپ کرد 5 مقدار دریافت و مقادیر دریافت شده در دیتاتایپ لیست نمایش داده شود. 
# اگر کاربر عدد دو را تایپ کرد 5 مقدار دریافت و مقادیر دریافت شده در دیتاتایپ دیکشنری نمایش داده شود. 
# اگر کاربر عدد سه را تایپ کرد 5 مقدار دریافت و مقادیر دریافت شده در دیتاتایپ Tuple نمایش داده شود. 
# اگر کاربر عدد چهار را تایپ کرد 5 مقدار دریافت و مقادیر دریافت شده در دیتاتایپ set نمایش داده شود.
from os import system

def get_value () :
    menu = input('\n\n1.List 2.Dictionary 3.Tuple 4.Set :')
    system('clear')
    
    match menu :
        case '1' :
            user_list = []
            for i in range (5) :
                user_input = input('Please enter something : ')
                system('clear')
                
                if user_input == '' :
                    print('Error!!! : input is empty')
                    
                user_list.append(user_input)
            print(user_list)
                    
        case '2' :
            data = {}
            for i in range (5) :
                key_input = input('Please enter some keys value : ')
                system('clear')
        
                value_input = input('Please enter some value : ')
                if key_input == '' and value_input == '' :
                    print('Error!!! : key input or value input is empty')
                
                data[key_input] = value_input
            
            print(data)        
        
        case '3' :
            user_list = []
            for i in range (5) :
                user_input = input('Please enter something : ')
                system('clear')
                
                if user_input == '' :
                    print('Error!!! : input is empty')
                    
                user_list.append(user_input)
            
            print(tuple(user_list))
            
        case '4' :
            data = set()
            
            for i in range (5) :
                user_input = input('Please enter something : ')
                if user_input == '' :
                    print('Error!!! : input is empty')
                    
                data.add(user_input)
                
            print(data)        
        
        case _ :
            print('Error!!! : Invalid menu number.')
            
            
get_value()
            

     