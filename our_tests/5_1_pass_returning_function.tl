# Don't move, otherwise the TEST will break
# + a b 10001
# RET, 10001, -1, memory address

program the_name_of_the_program
    script {
        # MODULES
        def my_function55 (int a, int b) : int {
            spit a+b
        }
    }
