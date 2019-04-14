# Don't move, otherwise the TEST will break

program the_name_of_the_program
    script {

        def sum (int a, int b) {
            eval(a + b)
        }
    }

    div {
      <^sum(1,2)^>
    }

    # 0. +, a, b, 10001
    # 1. eval, -1, -1, 10001
    # 2. ENDPROC, -1, -1, -1
    # 3. eval, -1, -1, 604
    # 4. ..........................
    # ...MORE QUADS HEERE WHEN WE ADD CALL NERUAL POINTS............
    # 5. eval -1 -1 605
