program fibonacci_recursive
    script {

        def fib(int n) : int {

            if (n <= 1){
                spit n
            }

            spit (fib(n - 1)) + (fib(n - 2))
        }

        eval(fib(13))
    }
