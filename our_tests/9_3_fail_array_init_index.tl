# Don't move, otherwise the TEST will break
# Error code: 305 -> Slice's CTEI index not valid. Slice index value (0) should be a CTEI greater than 0
# Error code: 305 -> Slice's CTEI index not valid. Slice index value (-1) should be a CTEI greater than 0

program the_name_of_the_program
    script {
      int arrA [1] = []
      int arrB[0] = []
      int arrC[-1] = []
    }
#
