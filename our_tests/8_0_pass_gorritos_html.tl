# Don't move, otherwise the TEST will break

program the_name_of_the_program
    script {
        int a
    }

    div {
     <^ 1+1 ^>
     <^ "hello" ^>
     <^ a + 1 ^>
    }
