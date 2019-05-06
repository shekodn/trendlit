program the_name_of_the_program
    script {

        def fib(int n) : int {

            if (n <= 1){
                spit n
            }

            spit (fib(n - 1)) + (fib(n - 2))
        }

        eval(fib(5))
    }
