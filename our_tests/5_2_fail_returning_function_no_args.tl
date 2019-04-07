# Don't move, otherwise the TEST will break
program the_name_of_the_program
    script {
        def my_function3 (int a, int b, int c) : int {
            spit(a + b + c)
        }

        # MODULES
        def my_function () : int {
            spit "Hi"
        }

    }
