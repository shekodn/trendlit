program dogs

script {
  int number_of_dogs = 1000
  int counter = 0
}

div class : "pretty" {}

div class : "container" {
  div class : "row" {
    <% loop(counter < number_of_dogs) %>
      img src : "https://picsum.photos/id/237/200/300" {}
      <% counter = counter + 1 %>
    <% end %>
  }
}
