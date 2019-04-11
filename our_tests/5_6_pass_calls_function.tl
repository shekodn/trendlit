# Don't move, otherwise the TEST will break


program the_name_of_the_program
    script {

        int my_int
        double my_double
        bool my_bool
        str my_str

        def param_func (int my_int, double my_double, bool my_bool, str my_str) {
          eval("hi")
        }

        def another_func (str my_str) {
          eval("hi")
        }

        def no_param_func () {
          eval("hi")
        }

        another_func(my_str)


    }
