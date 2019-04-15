# Don't move, otherwise the TEST will break

program the_name_of_the_program
    script {
    }

    div {
      <% loop (1 > 5) %>
        <^"hi"^>
        <% loop (2 is 2) %>
        <% end %>
      <% end %>
    }



    # 0. eval -1 -1 604
    # 1. > 1 5 11000
    # 2. GOTOF 11000 -1 8
    # 3. eval -1 -1 "hi"
    # 4. is 2 2 11001
    # 5. GOTOF 11001 -1 7
    # 6. GOTO -1 -1 4
    # 7. GOTO -1 -1 1
    # 8. eval -1 -1 605
