# Don't move, otherwise the TEST will break
# + a b 9000
# eval -1 -1 9000
# ENDPROC -1 -1 -1
# + a b 9000
# eval -1 -1 9000
# ENDPROC -1 -1 -1

program the_name_of_the_program
    script {
        # MODULES
        def my_function (int a, int b) {
            eval(a + b)
        }
        def my_function55 (int a, int b) {
            eval(a + b)
        }

    }
