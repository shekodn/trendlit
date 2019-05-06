program the_name_of_the_program
    script {}

    div class : "row" {
      div class : "col s12 m6" {
        div class : "card blue-grey darken-1" {
          div class : "card-content white-text" {
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
           link href : "#" {<^"This is a link"^>}
          }
        }
      }
    }
