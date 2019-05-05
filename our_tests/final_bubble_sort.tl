# Don't move, otherwise the TEST will break
# https://www.geeksforgeeks.org/bubble-sort/

program the_name_of_the_program
    script {

        int i=0
        int j=0
        int n=0
        int temp
        int arr[10] = []
        int size_array = 10

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


        loop(i < size_array - 1) {
            loop(j < size_array - i - 1) {
                if (arr[j] > arr[j+1]) {
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
                }
                j = j+1
            }
            j = 0
            i = i+1
        }

        i = 0

        eval("AFTER SORT")
        loop(i < size_array) {
            eval(arr[i])
            i = i + 1
        }


    }
