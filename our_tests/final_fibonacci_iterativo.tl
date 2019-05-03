# Don't move, otherwise the TEST will break
# https://dev.to/khalilsaboor/fibonacci-recursion-vs-iteration--474l

program the_name_of_the_program
    script {
        int previouspreviousNumber
        int previousNumber = 0
        int currentNumber = 1

        int i = 1

        int nthNumber = 7


        loop (i < nthNumber) {
            previouspreviousNumber = previousNumber

            previousNumber = currentNumber

            currentNumber = previouspreviousNumber + previousNumber

            i = i+1
        }
        eval (currentNumber)
    }
#
