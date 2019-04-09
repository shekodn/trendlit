program the_name_of_the_program

    script {
      str final_sentence
      str name = "Byte"
      str another_string = ""

      another_string = "is cute"

      final_sentence = name + another_string

      eval(final_sentence+"!!!")

    }


# 1. = "" -1 final_sentence
# 2. = "Byte" -1 name
# 3. = "" -1 another_string
# 4. = "is cute" -1 another_string
# 5. + name another_string 10001
# 6. = 10001 -1 final_sentence
# 7. + final_sentence "!!!" 10002
# 8. eval -1 -1 10002
