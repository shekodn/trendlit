# Don't move, otherwise the TEST will break

program the_name_of_the_program
    script {

        str my_str = "some cool global var"

        def param_func (int my_int, double my_double, bool my_bool, str my_str) {
         eval(my_int)
          eval(my_str)
          eval(my_double)
          eval(my_bool)
          eval("Hello "+my_str)
        }

        param_func(1, 2.0, True, "Ana Karen")

        def another_func (str my_str, int one, int two) {
            eval("Hello I am another_func: ")
          eval(my_str)
          eval(one)
          eval(two)
        }
        another_func("byte!", 2, 2)
        eval("Now I am back to global!")

        def no_param_func () {
          eval("I am a func with no params")
          eval(my_str)
        }

        no_param_func()
    }
