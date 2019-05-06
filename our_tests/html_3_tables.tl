program the_name_of_the_program
    script {}

    div class : "container" {
      <^ "I'm a div in a class named container" ^>

      h1 class : "header" {
        <^ "Heading h1" ^>
      }

      table {
        thead {
          tr {
            th {
              <^ "Name" ^>
            }
            th {
              <^ "Item Name" ^>
            }

            th {
              <^ "Item Price" ^>
            }
          }
        }

        tbody {
          tr {
            td {
              <^ "Alvin"^>
            }
            td {
              <^ "Eclair"^>
            }
            td {
              <^ "$0.87"^>
            }
          }
          tr {
            td {
              <^ "Alan"^>
            }
            td {
              <^ "Jellybean"^>
            }
            td {
              <^ "$3.76"^>
            }
          }
          tr {
            td {
              <^ "Jonathan"^>
            }
            td {
              <^ "Lollipop"^>
            }
            td {
              <^ "$7.0"^>
            }
          }
        }
      }
    }
