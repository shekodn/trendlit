program the_name_of_the_program
    script {
      int card_counter = 9
      int arr_size = 9
      int aux_counter = 0
      int arr[9] = []

      arr[0] = 5
      arr[1] = -1
      arr[2] = 4
      arr[3] = 2
      arr[4] = -8
      arr[5] = 100
      arr[6] = -2
      arr[7] = 3
      arr[8] = 42

      def my_find(int num, int arr_size) : bool {
          int i
          bool result

          loop(i < arr_size)  {
              if(arr[i] is num){
                  result = True
                  spit result
              }
              i = i + 1
          }

          spit result
      }

      def init_array(int size_array){

          int counter = size_array
          int aux = 0

          counter = size_array - 1

          loop (counter > 0) {
              arr[aux] = counter
              counter = counter - 1
              aux = aux + 1
          }
      }

      def print_array (int array_size){
        int i
        loop (i < array_size) {
          eval(arr[i])
          i = i + 1
        }
      }

      def bubble_sort(int array_size) {
          int i = 0, j=0, temp = 0

          loop(i < array_size - 1) {
              loop(j < array_size - i - 1) {
                  if (arr[j] > arr[j+1]) {
                      temp = arr[j]
                      arr[j] = arr[j+1]
                      arr[j+1] = temp
                  }
                  j = j+1
              }
              j = 0
              i = i+1
          }
          i = 0
      }

      def fibo_it (int nth_number) : int {

        int previous_previous_number = 0
        int previous_number = 0
        int current_number = 1
        int i = 1
            loop (i < nth_number)  {
                previous_previous_number = previous_number
                previous_number = current_number
                current_number = previous_previous_number + previous_number

                i = i+1
            }
            spit (current_number)
        }

      def factorial_it(int N) : int {
            int product = 1
            int j = 1

            loop(j <= N) {
                product = product * j
                j = j + 1
            }

            spit (product)
      }



    }

    head class : "pretty" {}
    div class : "container" {


    h1 { <^ "Headers" ^> }
    p {
        <^ "We provide some basic styling on header tags. In the example, you can
        see the the 6 header tags' different sizes."^>
    }

    div class : "card-panel" {
        h1 { <^ "Header1" ^> }
        h2 { <^ "Header2" ^> }
        h3 { <^ "Header3" ^> }
        h4 { <^ "Header4" ^> }
        h5 { <^ "Header5" ^> }
        h6 { <^ "Header6" ^> }
    }

    h1 {<^ "Cards Are Out Of Order!" ^>}
    h2 {<^ "Why not apply a sort?" ^>}
      div class : "row" {
      <% loop (aux_counter < card_counter) %>
        div class : "col m4" {
          div class : "card " {
            div class : "card-image" {
              img src : "https://via.placeholder.com/150" {}
              span class : "card-title" {
                <^ arr[aux_counter] ^>
              }
            }
            div class : "card-content" {
              span class : "card-title" {
                <^ arr[aux_counter] ^>
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
      <% aux_counter = 0 %>
      <% bubble_sort(arr_size) %>
      h1 { <^ "Cards are sorted!" ^> }
      p { <^ "This is like magic , but real" ^> }
      div class : "row" {
      <% loop (aux_counter < card_counter) %>
        div class : "col m4" {
          div class : "card " {
            div class : "card-image" {
              img src : "https://via.placeholder.com/150" {}
              span class : "card-title" {
                <^ arr[aux_counter] ^>
              }
            }
            div class : "card-content" {
              span class : "card-title" {
                <^ arr[aux_counter] ^>
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

      h1 { <^ "Show me only the cards with a negative value!" ^> }
        div class : "row" {
        <% aux_counter = 0 %>
        <% loop (aux_counter < card_counter) %>
            <% if (arr[aux_counter] < 0) %>
              div class : "col m4" {
                div class : "card " {
                  div class : "card-image" {
                    img src : "https://via.placeholder.com/150" {}
                    span class : "card-title" {
                      <^ arr[aux_counter] ^>
                    }
                  }
                  div class : "card-content" {
                    span class : "card-title" {
                      <^ arr[aux_counter] ^>
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
          <% end %>
          <% aux_counter = aux_counter + 1 %>
          <% end %>
        }
    h1 { <^ "Is 1234 in the card list? "^> }
    h3 { <^ "Let's find out! "^> }
    <% if (my_find(1234, arr_size)) %>
        h4 { <^ "Yes! it is! "^> }
    <% else %>
        h4 { <^ "It is not :( "^> }
    <% end %>

    h1 { <^ "What about number 42? "^> }
    <% if (my_find(42, arr_size)) %>
        h4 { <^ "Yes! it is! "^> }
        h5 { <^ "Coincidence? I don't think so ;)" ^> }
    <% else %>
        h4 { <^ "It is not :( "^> }
    <% end %>

    h1 { <^ "Speaking about number 42 ..."^> }
    h2 { <^ "What's the 42th fibonacci number?"^> }
    h3 { <^ fibo_it(42 - 1) ^> }
    h2 { <^ "And the first 42 numbers?"^> }
    h3 { <^ "I Don't know, let's count!"^> }
    ol {
        <% aux_counter = 0 %>
        <% loop (aux_counter < 42) %>
            li { <^ fibo_it(aux_counter) ^> }
            <% aux_counter = aux_counter + 1 %>
        <% end %>
    }

    h2 { <^ "This is correct, but SUPER ugly."^> }
    h3 { <^"Let's make it prettier!"^> }

    table {
        thead {
            tr {
                th {
                    <^ "Fibonacci Sequence like a boss" ^>
                }
            }
        }

        <% aux_counter = 0 %>
        tbody {

            <% loop (aux_counter < 42) %>
                tr {
                    td { <^ fibo_it(aux_counter) ^>  }
                }
                <% aux_counter = aux_counter + 1 %>
            <% end %>
        }
    }

    }
