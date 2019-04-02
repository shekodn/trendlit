# Example in Non-linear statements (Intermediate representation)
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

    # TODO - ELDAs example
      # if (A + B > D) {
        # if (A < B) {
        #    B = B + D
        # }
        # else {
        #    C = A + B
        #  }
      #   eval(2 + 4)
      #
      #   # A = B + C
      #
      #  }
      # # else {
      # #       A = B + C
      # #   }
      #  D = B + A


    } # closes script
