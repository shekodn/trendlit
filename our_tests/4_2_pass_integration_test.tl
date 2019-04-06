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
        int J
        int K
        int fake

      A = B + C * (D-E/F)*H
      B=E-F

      loop (A*B-C >= D*E/(G+H))
      {
        H = J*K+B
        if (B<H)
        {
            B = H+J
            loop(B>A+C){
                eval(A+B*C)
                eval(D-E)
                B = B-J
            }
        }
        else
        {
            do {
                A = A+B
                eval(B-D)
            } loop(A-D < C+B)

        }
      }
      F = A+B

    } # closes script
