# Don't move, otherwise the TEST will break


program the_name_of_the_program
    script {

        def my_function (int number) {
            eval(number)
        }

        my_function("not an int")

    }
