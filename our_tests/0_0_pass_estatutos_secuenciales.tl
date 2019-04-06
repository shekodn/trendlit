program the_name_of_the_program

    script {
      # =, 1, _, main_one
      int main_one = 1

      # =, 2, _, main_two
      int main_two = 2

      # =, 0, _, main_three
      int main_three

      # =, 0, _, main_four
      int main_four

      main_three = main_one + main_two
      # +, main_one, main_two, t1
      # =, t1, _, main_three

      main_four = main_two * main_two
      # *, main_two, main_two, t2
      # =, t2, _, main_four

      main_three = 1 + 2
      # +, 1, 2, t3
      # =, t3, _, main_three

    }
