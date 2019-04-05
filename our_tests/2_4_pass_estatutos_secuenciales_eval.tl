# expected quadruples after declarations

# / C D 1001
# * 1001 E 1002
# + B 1002 1003
# * F H 1004
# - 1003 1004 1005
# * A 1005 1006
# / D E 1007
# + B 1007 1008
# * C 1008 1009
# > 1006 1009 1010
program the_name_of_the_program

      script {
      int A
      int B
      int C
      int D
      int E
      int F
      int G
      int H

      eval(A * ( B + C / D * E - F * H) > C * (B + D / E))



      } # closes script
