# Don't move, otherwise the TEST will break

program the_name_of_the_program
    script {
        int a

        int intArr[1] = []

        # a = intArr[1+20]
        # eval (a)
        intArr[0] = 7
        a = intArr[0]
        eval(a)
        # eval(intArr[0])
    }
#
