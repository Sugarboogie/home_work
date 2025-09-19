def task_1() -> None:   
    my_int = 42                # int
    my_float = 3.14            # float
    my_str = "Hello, World !"  # str
    my_list = [1, 2, 3, 4, 5]  # list
    my_bool = True             # bool

    print("Тип my_int:", type(my_int))
    print("Тип my_float:", type(my_float))
    print("Тип my_str:", type(my_str))
    print("Тип my_list:", type(my_list))
    print("Тип my_bool:", type(my_bool))


task_1()

def task_2() -> None:  
    a = [1, 2, 3, 5, 8, 13, 21]
    
  
    print("Первые 3 значения:", a[0], a[1], a[2])


task_2()



def task_3(number: int) -> int:   
    return number ** 2            


print(task_3(5))
