# Don't move, otherwise the TEST will break

program the_name_of_the_program
    script {
    }

    div {
      <% if (1 > 5) %>
        <^"hi"^>
        <% if (1 > 2) %>
        p{}
        p { <^"nested if is executed"^> }
        <%/ endif %>
      <%/ endif %>
    }


    # 0. eval -1 -1 604
    # 1. > 1 5 1001
    # 2. GOTOF 1001 -1 11
    # 3. eval -1 -1 "hi"
    # 4. > 1 2 1002
    # 5. GOTOF 1002 -1 11
    # 6. eval -1 -1 606
    # 7. eval -1 -1 607
    # 8. eval -1 -1 606
    # 9. eval -1 -1 "nested if ...."
    # 10. eval -1 -1 607
    # 11. eval -1 -1 605
