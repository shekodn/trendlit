program the_name_of_the_program

    script {
      int main_one = 3
      int main_two
      # str string_one = ""
      # str string_two = " "
      # str string_three = "hi"
      # str str_four
      # bool bool_one = True
      # bool bool_two = False
      # bool bool_three
      # double doub_one = 2.2
      # double doub_two
      # main_one = 11 + 22
      # main_one = 20 - 3
      main_one = 2 * 10
      # main_one = 20 / 4
      # main_one = main_one / main_one

      # bool_three = 1 > 2
      # bool_three = 3 <= 3
      # bool_three = 1 is 2
      if (False){
        eval("hello world")
      } else {
        eval("hi world!")
      }
      # eval(doub_one)
    }
    br{}
    h1{
        <%if (1+100 is 1001)%>
            <^ "Header 1 - if" ^>
        <% else %>
            <^ "Header 1 - else" ^>
        <% end%>
    }
    div{
        <^ "I am a DIV!" ^>
        <^ "I am in the same line." ^>
        br{}
        <^ "I am in another line." ^>
    }
    p{
        <^ "I am a paragraph." ^>
        <^ "Did you know that 2+2 is" ^>
        <^ 2+2 ^>
        br{}
        <^ "The value of var main_one:"^>
        <^ main_one ^>
        br{}
        <^ "main_one / 3 =" ^>
        <^ main_one / 3 ^>
    }

    h2 {
        <% loop (main_two < 3) %>
            <^ "Loop in h2!" ^>
            br{}
            <% main_two = main_two + 1 %>
        <% end %>
    }

    # TODO: duplicates en memoria constante! (False, y default intiial values)   bool bool_two = False y  bool bool_three
