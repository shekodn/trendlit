# https://dev.to/khalilsaboor/fibonacci-recursion-vs-iteration--474l
program fibonacci_iterative
    script {

        def fibo2 (int nth_number) : int {

            int previous_previous_number = 0
            int previous_number = 0
            int current_number = 1
            int i = 1

        loop (i < nth_number)  {
            previous_previous_number = previous_number

            previous_number = current_number

            current_number = previous_previous_number + previous_number

            i = i+1
        }
            spit (current_number)
        }

        eval(fibo2(50))
    }
