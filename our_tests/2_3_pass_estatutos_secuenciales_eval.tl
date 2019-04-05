# Don't move, otherwise the TEST will break
# expected quadruples after declarations
#1. /,C,D,1001
#2. *,1001,E,1002
#3. +,B,1002,1003
#4. *,F,H,1004
#5. -,1003,1004,1005
#6. *,A,1005,1006


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
      # eval(A*(B+C))

      eval(A*(B+C/D*E-F*H))



      } # closes script
