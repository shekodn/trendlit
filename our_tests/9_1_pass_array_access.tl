# Don't move, otherwise the TEST will break

program the_name_of_the_program
    script {
        int a

        int intArr[3] = []

        a = intArr[1+1]
        # eval (a)
        # intArr[0] = 6
    }
#
