# Don't move, otherwise the TEST will break
# https://www.geeksforgeeks.org/bubble-sort/

program the_name_of_the_program
    script {

        int i=0, j=0, n=0
        int temp
        int arr[5] = []

        arr[0] = 2
        arr[1] = 1
        arr[2] = 9
        arr[3] = 7
        arr[4] = 3

        loop(i < n-1) {
            loop(j < n-i-1) {
                if (arr[j] > arr[j+1]) {
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
                }
                j = j+1
            }
            i = i+1
        }
    }
