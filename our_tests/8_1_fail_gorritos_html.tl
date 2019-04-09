# Don't move, otherwise the TEST will break

# should fail because variable a is not declared !

program the_name_of_the_program
    script {
    }

    div {
     <^ 1+1 ^>
     <^ "hello" ^>
     <^ a + 1 ^>
    }
