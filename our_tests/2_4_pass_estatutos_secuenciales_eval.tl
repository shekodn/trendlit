# Don't move, otherwise the TEST will break

# expected quadruples after declarations

# / C D 10000
# * 10000 E 10001
# + B 10001 10002
# * F H 9000
# - 10002 9000 10003
# * A 10003 10004
# / D E 10005
# + B 10005 10006
# * C 10006 10007
# > 10004 10007 11000
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
