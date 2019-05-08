# Don't move, otherwise the TEST will break

program the_name_of_the_program
    script {
        int a

        int intArr[3] = []
        eval(intArr[1+1]) #0
        intArr[1+1] = 2
        eval(intArr[1+1]) #2
        a = intArr[1+1]

        eval (a) #2
        intArr[0] = 6
        eval(intArr[0]) #6
        # #
        eval(intArr[1]) # 0
        intArr[1] = a
        eval(intArr[1]) # 2
    }
#
