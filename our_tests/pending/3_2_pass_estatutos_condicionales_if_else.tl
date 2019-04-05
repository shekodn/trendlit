# Example in Non-linear statements (Intermediate representation)
# + 1  2 1001
# > 1001  4 1002
# + 2 3 1003
# > 1 2 1004
# GOTOF
program the_name_of_the_program

    script {

    if (1 + 2 > 4) {
        eval(2 + 4)
      if (1 > 2) {
         eval(2 + 4)
      }
      else {
         eval(1 + 2)
       }
     }
     else {
          eval(2 + 3)
      }
     eval(2 + 1)

    } # closes script
