# Don't move, otherwise the TEST will break
# 0 =, 13000, -1, 1000
# 1 =, 13000, -1, 1001
# 2 =, 13000, -1, 1002
# 3 VER, 13000, 13001, 13000
# 4 +, 13000, 13002, 9000
# 5 *, 13001, 13003, 9001
# 6 VER, 13000, 13001, 13000
# 7 +, 13000, 13002, 9002
# 8 +, 9001, 1009002, 9003
# 9 =, 9003, -1, 1009000

program the_name_of_the_program
    script {
        int a

        int intArr[2] = []
        intArr[0] =  2 * 4 + intArr[0]


        # if (intArr[0] > intArr[1]) {
        #   eval(intArr[0] > intArr[1])
        # }

    }
#
