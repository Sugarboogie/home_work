def task_1():   
    my_int = 42                
    my_float = 3.14            
    my_str = "Hello, World !"  
    my_list = [1, 2, 3, 4, 5]  
    my_bool = True            

    print("Тип my_int:", type(my_int))
    print("Тип my_float:", type(my_float))
    print("Тип my_str:", type(my_str))
    print("Тип my_list:", type(my_list))
    print("Тип my_bool:", type(my_bool))


task_1()

def task_2():  
    a = [1, 2, 3, 5, 8, 13, 21]
    
  
    print("Первые 3 значения:", a[0], a[1], a[2])


task_2()



def task_3(number: int) -> int:   
    return number ** 2            


print(task_3(5))
