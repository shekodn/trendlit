program the_name_of_the_program

    script {
        int A
        int B
        bool D = True
        # bool isGreater # TODO: this breaks bc of the is
        D = 10 >= 20
        D = 10 <= 20
        D = 10 is 20
        D = 10 not 20
        D = 10 > 20
        D = 10 < 20
        # C = A + B # TODO: this is NOT failing (propperly aka nice error message) and 'C' is not declared!
        D = A > B
    }
