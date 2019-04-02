program the_name_of_the_program

    #This is a comment

    script {
        # VARIABLE AND DECLARATION AND INITIALIZATION SECTION

        # You can declare global variables like this.
        str global_var_name = "I am a global variable"
        # We support different data types and you can define them like this
        str name = "Ana Karen"
        int age = 23
        str sex = "F"
        double height = 1.6

        int a = avg(average_slice1D) # TODO: do we want this?
        # int a,b,c # TODO: do we want this?
        int d = 1, e = 2, f = 3
        # int int_var = 1+0 # FAILURE EXAMPLE
        bool flag = True
        bool flag2 = False
        bool flag3 #declare with no value
        # int my_slice [2] = [1+2,30] # FAILURE EXAMPLE

        int i = 1
        int int_var_name

        bool legal # This is how you deine an uninitialized variable, trendlit by default will assign a false value
        # Slices and 2D Slices work as arrays and matrixes respectively
        str my_slice [2] = ["a","b"]
        int another_slice [2] = [1, 2]
        # int my_2D_slice [3][3] = [[]]
        # int another_2D_slice [3][3] = [[1,2,3][1,2,3][1,2,3]]

        # VARS FOR FUNCTIONS
        int test_slice [5] = [4,3,1,7,0]

        ### median
        int slice1D [5] = [20, 2, -1, 1, 34]
        # median_1Dslice(slice1D) - TODO
        int med = 1


        ### mode
        int mode_slice1D [9] = [5, 2, 2, 1, 1, 4, 1, 4, 4]
        # int mode = mode_1Dslice(mode_slice1D) - TODO

        ### avg
        int average_slice1D [5] = [4, 3, 1, 7, 0]
        # int avg = avg(average_slice1D) - TODO

        ### pow
        int pow_a = 2
        int pow_b = 3
        # int pow_ans = avg(pow_a,pow_b) - TODO

        ### multiply_1Dslice1
        int multiply_1Dslice1 [3] = [1, 2, 3]
        int multiply_1Dslice1_factor = 2

        # find
        int find_slice [8] = [10, 20, 30, 40, 50, 60, 70, 80]
        int find_filter_num = 40

        ### find_min
        # int slice_min = find_min(slice, filter_num) - TODO

        ### find_max
        # TODO - how to declare an array? with unkown size
        # int slice_max = find_max(slice, filter_num) - TODO

        ### zeros
        int slice_zeros[10]
         # = zeros(10) - TODO

        ### randoms
        int slice_randoms[10]
        # = randoms(10) - TODO

        # You can add and modify elements of your array/matrix
        another_slice[0] = 1+2
        my_slice[0] = "z" #this will result in the array being ["z", "b"]
        my_2D_slice[0][0] = 1

        # CONDITIONALS

        # You can create a simple condition like the following
        if (sex is "F") {
            int_var_name = 1
            eval("Female!")
        }

        if (sex not "F") {
            eval("Male!")
        }

        # You can add an else to your condition
        if (age <= 18) {
            legal = True
            eval("Legal! :)")
        } else {
            legal = False
            eval("Underage :(")
        }
        # Please don't declare any new variable  outside the declaring scope.
        # int hola = 1 # FAILURE EXAMPLE

        # LOOPS

        #You can loop through an array/matrix or a fixed number of times by using a loop
        # This is a while disguised as a loop
        loop (i not 10) {
            eval("Loop number" + i + "")
            # Please don't declare any new variable inside a loop.
            # int hola = 1 # FAILURE EXAMPLE
        }

        # MODULES

        # This is how you declare a function.
        # The group of parentheses is used for parametrization and whatever comes after the ':' the return type.
        # You can use the spit statement to return your values
        def sum (int a, int b) : int {
            int result = a #This is a local variable
            result = a + b
            # int result = a + b # FAILURE EXAMPLE
            spit result
        }

        # This is how you declare a non-spitting function (aka void)
        def greeting (str nickname) {
            eval("Hello " + nickname + "!")
        }

        ####
        # BASIC STATISTICS FUNCTIONS
        # Oh yes we are very cool and we support some basic statistical functions
        ###

        # You can even import a table from an excel sheet into a matrix!
        # suck_csv receives an argument with the path to your csv file
        # int my_table [2][3] = suck_csv("C:\\Documents\car.csv")

        ### sort_slice
        sort_slice(test_slice, max)
        eval(test_slice)

        sort_slice(test_slice, min)
        eval(test_slice)

        # ### median
        # int slice1D [5] = [20, 2, -1, 1, 34]
        median_1Dslice(slice1D)
        eval(med)

        # ### mode
        # int mode_slice1D [9] = [5, 2, 2, 1, 1, 4, 1, 4, 4]
        mode_1Dslice(mode_slice1D)
        eval(mode)

        ### avg
        average = avg(average_slice1D)
        # pow_ans = avg(pow_a,pow_b) # FAILURE EXAMPLE
        eval(average)
        eval(avg(average_slice1D))

        ### pow
        pow_a = 2
        pow_b = 3
        pow_ans = pow(pow_a,pow_b)
        eval(pow_ans)

        ### multiply_1Dslice
        # TODO - When you generate a slice, do you overwrite it or do you create
        # a new one (See GO's documentation)
        multiply_1Dslice1 = multiply_1Dslice1(multiply_1Dslice1, multiply_1Dslice1_factor)
        eval(multiply_1Dslice1)

        ### find_min
        slice_min = find_min(slice, filter_num)
        eval(slice_min)

        ### find_max
        slice_max = find_max(slice, filter_num)
        eval(slice_max)

        ### zeros
        slice_zeros = zeros(10)
        eval(slice_zeros)

        ### randoms
        slice_randoms[10] = randoms(10)
        eval(slice_randoms)

    }

    h1 { "This is a Title" }
    h2 {
        class: "header-2-class"
        "And this is the subtitle"
    }

    div {
        p { "What we want to do here is being able to let others write pythoninc
            code while being able to demonstrate their findings."
        }
        p {
            <^"Whatever goes inside this will be evaluated as code." ^>
            "The result of 1+1 is" <^ 1+1 ^>
        }
        p {
            "We noticed that a lot of researches and financial people are using python
            so we tought that we could do a language to help them publish their results
            faster and with a minimal learning curve. The idea is that,
            if you know python, you know how to write using trendlit."
        }
    }

    div {
        class: "example-class"

        table {
            tr {
                th {"Brand"}
                th {"Year"}
                th {"Model"}
            }
            embed my_embed_name {
                int i
                int j
                loop (i not len(my_table)) {
                    tr {}
                        loop (j not len(my_table[0])) {
                            th { eval(my_table[i][j]) } # prints brand, year, model
                            j = sum(j,1)
                        }
                    }
                    i = sum(i,1)
                }
            }
        }
    }
