# Don't move, otherwise the TEST will break

program the_name_of_the_program

      script {
      bool A
      bool B
      bool C
      A = True
      B = True
      C = False

      eval(A and C) # FALSE
      eval(A or C) # TRUE
      eval((A and C) is (A and C)) # True
      eval(A and C is A and A) # False

      } # closes script
