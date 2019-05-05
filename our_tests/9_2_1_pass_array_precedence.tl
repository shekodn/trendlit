# Don't move, otherwise the TEST will break
program the_name_of_the_program
    script {

        int intArr[2] = []
        intArr[0] = 0
        intArr[0] =  2 * 4 + intArr[0]
        intArr[1] = intArr[0] + 1
        eval(intArr[0]) # 8
        eval(intArr[1]) # 9

        if (intArr[1] not intArr[1]) {
            eval("NOT")
        } else {
            eval("IS")
        }
    }
