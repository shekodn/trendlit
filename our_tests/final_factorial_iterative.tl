program factorial_iterative
    script {

        int product = 1
        int j = 1
        int N = 11

        loop(j <= N) {
            product = product * j
            j = j + 1
        }

        eval(product)
    }
