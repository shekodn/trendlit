# Don't move, otherwise the TEST will break

program the_name_of_the_program

    script {

    int A
    int B
    int C
    int D

    if (A + B > D) {
      if (A < B) {
         A = 0
         B = B + D
      }
      else {
         C = A + B
       }
     }
     else {
          A = B + C
      }
     D = B + A * C

    } # closes script
