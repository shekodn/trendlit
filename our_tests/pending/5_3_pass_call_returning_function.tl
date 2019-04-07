# Don't move, otherwise the TEST will break


program the_name_of_the_program
    script {
        int a = 4
        int b = 6
        bool result
        # MODULES
        def compare (int a, int b) : bool {
            spit a < b
        }

        result = compare(a, b)

    }
