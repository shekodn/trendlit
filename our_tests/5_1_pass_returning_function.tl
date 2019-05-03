# Don't move, otherwise the TEST will break
# GOTO -1 -1 3
# + a b 9000
# RET, 9000, -1, memory address

program the_name_of_the_program
    script {
        # MODULES
        def my_function55 (int a, int b) : int {
            spit a+b
        }
    }
