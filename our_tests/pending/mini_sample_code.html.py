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

        # int a,b,c # TODO: do we want this?
        int d = 1, e = 2, f = 3
        # int int_var = 1+0 # FAILURE EXAMPLE
        bool flag = True
        bool flag2 = False
        bool flag3 #declare with no value
        # int my_slice [2] = [1+2,30] # FAILURE EXAMPLE

        int i = 1
        int int_var_name

        bool legal


        ### mode
        # int avg = avg(average_slice1D) - TODO

        ### pow
        int pow_a = 2
        int pow_b = 3
        # int pow_ans = avg(pow_a,pow_b) - TODO

        ### multiply_1Dslice1

        ### find_min
        # int slice_min = find_min(slice, filter_num) - TODO

        ### find_max
        # TODO - how to declare an array? with unkown size
        # int slice_max = find_max(slice, filter_num) - TODO



        # CONDITIONALS

        # You can create a simple condition like the following
        if(1>2){
            eval(10+20)
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
