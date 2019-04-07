# Don't move, otherwise the TEST will break
# + a b 10001
# eval -1 -1 10001
# ENDPROC -1 -1 -1
# + a b 10002
# eval -1 -1 10002
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
