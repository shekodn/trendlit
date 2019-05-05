# Don't move, otherwise the TEST will break


program the_name_of_the_program
    script {
    str s
        def another_func () : str {
            # str greeting = "hello i am local trendy"
          # eval("hiiiii")
          spit "hello world"
        }
        eval("I will call a func")
        s = another_func()
        eval(s)
        eval("I called it!")


    }
