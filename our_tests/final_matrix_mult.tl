program the_name_of_the_program
    script {
        # Function to print an array

        int mat1[4][4] = [[]]
        int mat2[4][4] = [[]]
        int res[4][4] = [[]]

        int i=0, j=0, k=0, N = 4, count = 1

# FILL MATRIX VALUES
        i=0
        loop (i < N)
        {
            j = 0
            loop (j < N) {
                mat1[i][j] = count
                mat2[i][j] = count
                j = j+1
            }
            count = count +1
            i = i + 1
        }

# MUTIPLY MATRIX
        i=0
        loop (i < N)
        {
            j = 0
            loop (j < N)
            {
                k = 0
                loop (k < N) {
                    # aux1 = mat1[i][k]
                    # aux2 = mat2[k][j]
                    # res[i][j] = res[i][j] + aux1 * aux2
                    res[i][j] = res[i][j] + mat1[i][k] * mat2[k][j]
                    k = k+1
                }
                j = j+1
            }
             i = i+1
        }

            eval("Result matrix is:")
# PRINT MATRIX
        i=0
        loop (i < N)
        {
            j = 0
            loop (j < N) {
                eval(res[i][j])
                j = j+1
            }

            i = i + 1
        }
    }
