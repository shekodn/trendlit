program the_name_of_the_program
    script {
        int mat1[4][4] = [[]]
        int mat2[4][4] = [[]]
        int res[4][4] = [[]]

        int i=0, j=0, k=0, N = 4, count = 1

        # FILL MATRIX VALUES
        def fill_mat(){
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
        }

        # MUTIPLY MATRIX
        def multiply_matrix() {
            i=0
            loop (i < N)
            {
                j = 0
                loop (j < N)
                {
                    k = 0
                    loop (k < N) {
                        res[i][j] = res[i][j] + mat1[i][k] * mat2[k][j]
                        k = k+1
                    }
                    j = j+1
                }
                i = i+1
            }
        }

        # PRINT MATRIX A
        def print_mat1() {
            i=0
            loop (i < N)
            {
                j = 0
                loop (j < N) {
                    eval(mat1[i][j])
                    j = j+1
                }
                i = i + 1
            }
        }

        # PRINT MATRIX B
        def print_mat2() {
            i=0
            loop (i < N)
            {
                j = 0
                loop (j < N) {
                    eval(mat2[i][j])
                    j = j+1
                }
                i = i + 1
            }
        }

        # PRINT MATRIX red
        def print_mat_res() {
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

        fill_mat()
    }

    h1{
        <^"Mat 1:"^>
    }
    h2{
        <% print_mat1() %>
    }

    h1{
        <^"Mat 2:"^>
    }
    h2{
        <% print_mat2() %>
    }

    h1{
        <^"Result matrix: AxB"^>
    }
    h2{
        <%multiply_matrix()%>
        <% print_mat_res() %>
    }
