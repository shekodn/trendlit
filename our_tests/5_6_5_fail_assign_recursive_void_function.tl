# Don't move, otherwise the TEST will break


program the_name_of_the_program
    script {
        int a
        def uno (int a) {
            eval(a)
        }

        uno(uno(2))

        a = 1+1

    }
