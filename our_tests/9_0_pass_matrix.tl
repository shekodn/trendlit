
program the_name_of_the_program
    script {
        int mat[2][2] = [[]]
        int i
        eval(mat[1][1]) # 0
        mat[1][1] = 20
        eval(mat[1][1]) # 20
        i = mat[1][1]
        eval(i) # 20
    }
#
