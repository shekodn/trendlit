# Don't move, otherwise the TEST will break


program the_name_of_the_program
    script {
        int number = 1

        def my_function (double number) {
            eval(number)
        }

        my_function(number + 2 * 3 / (1+2))

    }
