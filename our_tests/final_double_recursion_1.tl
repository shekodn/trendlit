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

        def multiplyNumbers(int n) : int {
            if (n >= 1){
                spit (n * multiplyNumbers(n - 1))
            }
            else {
                spit 1
            }
        }

        def factorial(int n) : int {
            if (n is 0) {
                spit 1;
            }

            spit n * (factorial(n - 1))
        }



        # print_recursive(0)
        # eval("---")
        # eval(fib(10))
        # eval("---")
        # multiplyNumbers(10)
        # eval("---")
        eval(factorial(10)) # savior
    }
