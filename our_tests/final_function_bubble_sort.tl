# Don't move, otherwise the TEST will break

program bubble_sort
    script {

        int size_array = 10
        int arr[10] = []

        def init_array(int size_array){

            int counter = size_array
            int aux = 0

            counter = size_array - 1

            loop (counter > 0) {
                arr[aux] = counter
                counter = counter - 1
                aux = aux + 1
            }
        }

        def print_array (int size_array) {
            int i = 0, j=0
            loop(i < size_array) {
                eval(arr[i])
                i = i + 1
              }
             i = 0
        }

        def bubble_sort() {
            int i = 0, j=0, temp = 0

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
        }

        init_array(size_array)
        print_array(size_array)
        eval("-----")
        bubble_sort()
        print_array(size_array)
    }
