# Don't move, otherwise the TEST will break

program find
    script {

        int i = 0
        int arr_size = 10
        int arr[10] = []
        int which_number = 100
        bool in_array = False

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

        loop(i < arr_size) {

            if(arr[i] is which_number){
                in_array = True
            }

            i = i + 1
        }

        eval(in_array)

        # Resets vars
        i = 0
        which_number = 1234
        in_array = False

        loop(i < arr_size) {

            if(arr[i] is which_number){
                in_array = True
            }

            i = i + 1
        }


        eval(in_array)

    }
