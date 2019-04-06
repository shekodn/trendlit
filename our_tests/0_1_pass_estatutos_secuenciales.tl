program the_name_of_the_program

    script {
      # =, 0, _, main_one

      int main_one = 0
      # =, 0, _, A
      int A
      # =, 0, _, B
      int B
      # int C
      # int D
      # int E
      # int F
      # int H

      # +, 1, 2, t1
      # =, t1, _, main_one
      main_one = 1 + 2
      # +, A, B, t2
      # =, t2, _, main_one
      main_one = A + B

      # main_one = 1 * 2
      # main_one = A * B
      #
      # main_one = 1 + 2 * 3
      # main_one = A + B * C
      #
      # main_one = 1 + 2 * 3 / 2
      # main_one = A + B * C / B

      # main_one = A * (B + C * D / E - F) / H
    }
