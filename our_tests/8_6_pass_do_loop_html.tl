# Don't move, otherwise the TEST will break

program the_name_of_the_program
    script {
    }

    div {
      <% do %>
        <^"hi"^>
        p{}
      <% endloop ( 3 is 4) %>
    }

    # 0. eval -1 -1 604
    # 1. eval -1 -1 "hi"
    # 2. eval -1 -1 606
    # 3. eval -1 -1 607
    # 4. is 3 4 10001
    # 4. GOTOT 10001 -1 1
    # 5. eval -1 -1 605
