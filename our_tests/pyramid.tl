program the_name_of_the_program
    script {
        # Function to print an array

            int rows = 5
            int i = 1
            int j=1

            loop(i <= rows)
            {
                loop(j <= i)
                {
                    eval(i)
                    eval(j)
                    j = j + 1
                }
                j = 0
                eval(" ")
                i = i + 1
            }
    }
