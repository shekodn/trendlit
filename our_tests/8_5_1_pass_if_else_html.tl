# Don't move, otherwise the TEST will break

program the_name_of_the_program
    script {
    }

    div {

        <% if (1 > 2) %>
            p { <^" if is executed"^> }
        <% else %>
            p { <^" else is executed"^> }
        <%/ endif %>
    }

    # 0. eval -1 -1 604
    # 1. > 1 2 10001
    # 2. GOTOF 10001 -1 7
    # 3. eval -1 -1 606
    # 4. eval -1 -1 " if is executed"
    # 5. eval -1 -1 607
    # 6. GOTO -1 -1 10
    # 7. eval -1 -1 606
    # 8. eval -1 -1 " else is executed"
    # 9. eval -1 -1 607
    # 10. eval -1 -1 605
