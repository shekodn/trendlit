program the_name_of_the_program

    #This is a comment

    script {
        # VARIABLE AND DECLARATION AND INITIALIZATION

        # You can declare global variables like this.
        str global_var_name = "I am a global variable"
        # We support different data types and you can define them like this
        str name = "Ana Karen"
        int age = 23
        str sex = "F"
        double height = 1.6

        bool legal # This is how you deine an uninitialized variable, trendlit by default will assign a false value
        # Slices and 2D Slices work as arrays and matrixes respectively
        str my_slice [2] = ["a","b"]
        # int my_2D_slice [3][3] = [[]]

        # You can add and modify elements of your array/matrix
        my_slice[0] = "z" #this will result in the array being ["z", "b"]
        my_2D_slice[0][0] = 1

        # CONDITIONALS

        # You can create a simple condition like the following
        if (sex is "F") {
            int int_var_name = 1
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

        # LOOPS

        #You can loop through an array/matrix or a fixed number of times by using a loop
        # This is a while disguised as a loop
        int i = 1
        loop (i not 10) {
            eval("Loop number" + i + "")
            # Please don't declare any new variable inside a loop.
            # int hola = 1
        }

        # MODULES

        # This is how you declare a function.
        # The group of parentheses is used for parametrization and whatever comes after the ':' the return type.
        # You can use the spit statement to return your values
        def sum (int a, int b) : int {
            int result = a + b #This is a local variable
            spit result
        }

        # This is how you declare a non-spitting function (aka void)
        def greeting (str nickname) {
            eval("Hello " + nickname + "!")
        }

        # BASIC STATISTICS FUNCTIONS
        #oh yes we are very cool and we support some basic statistical functions

        # You can even import a table from an excel sheet into a matrix!
        # suck_csv receives an argument with the path to your csv file
        # int my_table [2][3] = suck_csv("C:\\Documents\car.csv")

        # You can manipulate your slices by using some the default methods
        int test_slice [5] = [4,3,1,7,0]
        sort_slice(test_slice, criteria)
            #type = int, double, str, bool
            # criteria = min/max

        # Get valuable insight from your data
        median(test_slice) # will spit => 3
            #type = int, double.
        mode(test_slice) # would spit => 3
            #type = int, double, str, bool
        avg(test_slice) # would spit => 3.0
            #type = int, double

        #Supported math function
        # pow(type a, int b)
        pow(a, b)
            #type = int, double

        # You can manipulate your sort_2D_slice by using some the default methods
        sort_2D_slice(my_table, criteria, column_index)
            # criteria = min/max

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
            # embed my_embed_name {
            #     int i
            #     int j
            #     loop (i not len(my_table)) {
            #         tr {
            #             loop (j not len(my_table[0])) {
            #                 th { eval(my_table[i][j]) } # prints brand, year, model
            #                 j = sum(j,1)
            #             }
            #         }
            #         i = sum(i,1)
            #     }
            # }
        }
    }
