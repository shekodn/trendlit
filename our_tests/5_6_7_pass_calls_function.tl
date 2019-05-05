# Don't move, otherwise the TEST will break

program the_name_of_the_program
    script {
    str s
        def another_func () : str {
        spit "hi friends!"
          eval(1+1+2)
          spit "hello world!"
        }
        eval("I will call a func")
        s = another_func()
        eval(s)
        eval(1+1)

    }
