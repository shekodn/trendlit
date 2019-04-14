# Don't move, otherwise the TEST will break


program the_name_of_the_program
    script {
        int a
        def uno (int a): int{
            spit a+1
        }

        # uno(2)
        a = uno(2)

    }
