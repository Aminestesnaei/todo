try :
    with open("data.txt", "r") as f:
        data = f.read()
        f.close()
except:
    with open("data.txt" , "w") as a:
        a.write("To Do List by nucman")
        a.close()
        


def start():
    print("Hi there !, wanna add some undone things or you just do it ?")
    try :
        print("list (1)\nadd (2)\nremove (3) \nexit (4)")
        x = int(input())
        if x == 1 :
            show_lsit()
        elif x == 2 :
            add_list()
        elif x == 3 :
            del_list()
        elif x == 4 :
            kill()
        else:
            print("you got no power here ! just choose only option i told you")
            start()
        
    except:
        print("don't bother your-self and just call the number !")
        start()
        
       

        
def show_lsit():
    for list in date():
        print(list())
def add_list():
    pass
def del_list():
    pass
def kill():
    print("be well")

main()