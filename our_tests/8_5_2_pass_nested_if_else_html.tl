# Don't move, otherwise the TEST will break

program the_name_of_the_program
    script {
    }

    div {

        <% if (1 > 2) %>
            p { <^" if is executed"^> }
        <% else %>
            p { <^" else is executed"^> }
            <% if (1 > 2) %>
                p { <^" 2nd if is executed"^> }
            <% else %>
                p { <^" 2nd else is executed"^> }
            <%end %>
        <%end %>
    }

    # 0. eval -1 -1 604
    # 1. > 1 2 11000
    # 2. GOTOF 11000 -1 7
    # 3. eval -1 -1 606
    # 4. eval -1 -1 " if is executed"
    # 5. eval -1 -1 607
    # 6. GOTO -1 -1 19
    # 7. eval -1 -1 606
    # 8. eval -1 -1 " else is executed"
    # 9. eval -1 -1 607
    # 10. >  1 2 11001
    # 11. GOTOF 11001 -1 16
    # 12. eval -1 -1 606
    # 13. eval -1 -1 " 2nd if is executed"
    # 14. eval -1 -1 607
    # 15. GOTO -1 -1 19
    # 16  eval -1 -1 606
    # 17. eval -1 -1 " 2nd else is executed"
    # 18. eval -1 -1 607
    # 19. eval -1 -1 605








    # 7. eval -1 -1 606
    # 8. eval -1 -1 " else is executed"
    # 9. eval -1 -1 607
    # 10. eval -1 -1 605
