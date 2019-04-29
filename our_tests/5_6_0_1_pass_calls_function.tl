# Don't move, otherwise the TEST will break
# =, 13000, -1, 1000

program the_name_of_the_program
    script {

        int my_str

        def function2 (int b) : int {
          b = b * 1+3
          spit b*2
        }

        eval(1+function2(1+3))


    }
