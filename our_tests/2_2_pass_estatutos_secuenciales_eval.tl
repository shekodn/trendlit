# Don't move, otherwise the TEST will break

program the_name_of_the_program

      script {
        eval(4 + 2)
        eval(4 - 2)
        eval(4 * 2)
        eval(4 / 2)
        eval(4 < 2)
        eval(4 > 2)
        eval(4 >= 2)
        eval(4 <= 2)
        eval(4 is 2)
        eval(4 not 2)
      } # closes script
