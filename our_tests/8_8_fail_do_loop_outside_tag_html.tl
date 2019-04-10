# Don't move, otherwise the TEST will break

program the_name_of_the_program
    script {
    }

    <% do %>
      <^"All this is not valid"^>
    <% endloop ( 3 is 4) %>

