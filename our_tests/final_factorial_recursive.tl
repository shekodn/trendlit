program factorial_recursive
    script {

        def factorial(int n) : int {
            if (n is 0) {
                spit 1;
            }

            spit n * (factorial(n - 1))
        }

        eval(factorial(10)) # savior
    }
