# Don't move, otherwise the TEST will break


program the_name_of_the_program
    script {
        str my_name = "Sergio"
        
        def greetings (str name) {
            eval(name)
        }

        my_function(my_name)

    }
