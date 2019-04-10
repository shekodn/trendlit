# Don't move, otherwise the TEST will break

program the_name_of_the_program
    script {
    }


    <% loop (1 > 5) %>
        <^"All this is not valid"^>
    <% end %>

