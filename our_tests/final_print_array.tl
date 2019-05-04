program the_name_of_the_program
    script {
        # Function to print an array

            int size_array = 10
            int arr [10] = []
            bool ascending = True
            int counter

            if (ascending is True) {
                counter = size_array
                eval("is ascending")
                eval(ascending)
                loop(counter > 0) {
                    eval(counter)
                    counter = counter - 1
                }
            } else {
                counter = 0
                eval("is NOT ascending")
                eval(ascending)
                loop(counter < size_array) {
                    eval(counter)
                    counter = counter + 1
                }
            }
    }
