program the_name_of_the_program
    script {

        def print_recursive(int n) {
            eval(n);
            if (n < 10) {
                print_recursive(n+1);
            }
        }

        def fib(int n) : int {

            if (n <= 1){
                spit n
            }

            spit fib(n - 1) + fib(n - 2);
        }

        # print_recursive(0)
        fib(10)
    }
