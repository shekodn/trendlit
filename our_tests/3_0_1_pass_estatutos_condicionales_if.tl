# Don't move, otherwise the TEST will break

# expected quadruples
#0. =,0,-1,A
#1. <,A,1,11000
#2. GOTOF,11000,-1,4
#3. =,0,-1,A

program the_name_of_the_program

script {

    int A

    if (A < 1) {
        A = 0
    }

} # closes script
