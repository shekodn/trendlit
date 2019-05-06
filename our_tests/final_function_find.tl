# Don't move, otherwise the TEST will break
program the_name_of_the_program
    script {

        int arr_size = 10
        int arr[10] = []

        arr[0] = 5
        arr[1] = 1
        arr[2] = 4
        arr[3] = 2
        arr[4] = 8
        arr[5] = 100
        arr[6] = -2
        arr[7] = 3
        arr[8] = 44
        arr[9] = 0

        def my_find(int num) : bool {
            int i
            bool result

            loop(i < arr_size)  {
                if(arr[i] is num){
                    result = True
                    spit result
                }
                i = i + 1
            }

            spit result
        }

        eval(my_find(1234)) # False
        eval(my_find(100)) # True
        eval(my_find(-2)) # True
    }
