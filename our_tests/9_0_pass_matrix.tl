
program the_name_of_the_program
    script {
        # int i
        # bool b
        # double d
        # str s

        # bool arr[2] = []
        # bool b
        # bool mat[2] = [[]] # this should break
        int mat[2][2] = [[]]
        int i
        # a = intArr[1+20]
        # eval (a)
        eval(mat[1][1]) # 0
        mat[1][1] = 20
        eval(mat[1][1]) # 20
        i = mat[1][1]
        eval(i) # 20
        # mat[0][0] = 20
        # intArr[0] = 6
    }
#
