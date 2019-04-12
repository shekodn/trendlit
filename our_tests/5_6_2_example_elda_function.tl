# Don't move, otherwise the TEST will break


program the_name_of_the_program
    script {

        int a
        int b
        double f


        def uno (int a) {
            a = a + b * a
            eval(a)
           eval(b)
           eval(a+b)
        }

        def dos (int a, int b, double g) {
          int i
          i = b
          loop (i>0){
            a = a+b*i+b
            uno(i*2)
            eval(a)
            i = i - 8
          }
        }

        def main() {
          a = 3
          b = a + 1
          eval(a)
          eval(b)
          f = 3.14
          dos(a+b*2, b, f*3)
          eval(a)
          eval(b)
          eval(f*2+1)
        }


    }
