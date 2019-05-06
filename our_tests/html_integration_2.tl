program the_name_of_the_program
    script {
      int card_counter = 9
      int aux_counter = 0
    }

    head class : "pretty" {}

    div class : "container" {

      div class : "row" {
      <% loop (aux_counter < card_counter) %>
        div class : "col m4" {
          div class : "card " {
            div class : "card-image" {
              img src : "https://via.placeholder.com/150" {}
              span class : "card-title" {
                <^"Card Title"^>
              }
            }
            div class : "card-content" {
              span class : "card-title" {
                <^"Card Title"^>
              }
              p {
                <^ "I am a very simple card. I am good at containing small bits of information." ^>
                <^ "I am convenient because I require little markup to use effectively." ^>
              }
            }
            div class : "card-action" {
             link href : "#" {<^"This is a link"^>}
            }
          }
        }
        <% aux_counter = aux_counter + 1 %>
        <% end %>
      }
    }
