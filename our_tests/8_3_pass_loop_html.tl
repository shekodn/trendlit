# Don't move, otherwise the TEST will break

program the_name_of_the_program
    script {
    }

    div {
      <% loop (1 > 5) %>
        <^"hi"^>
      <%/ endloop %>
    }


    # 0. eval -1 -1 604
    # 1. > 1 5 10001
    # 2. GOTOF 10001 -1 5
    # 3. eval -1 -1 "hi"
    # 4. GOTO -1 -1 1
    # 5. eval -1 -1 605
