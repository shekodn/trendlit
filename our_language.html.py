%str hello = "Hello I am a global variable"
%eval(hello)


%console
    def friends_function(list friends): # RECIEVE PARAMETERS
      int max = 40
      str hello2 = "I am a local variable"
      if friends.length > max:
          friends.push("byte") #REMOVE ELM FROM LIST
        else if friends.length < max: #ADD ELM TO LIST
            friends.pop()
        return friends

    list[str] my_friends_list = ["ana karen", "sergio", "laura"] #LIST
    my_friends_list = friends_function(friends) # SEND PARAMS
    eval("I have" + my_friends_list.length() + "friends !!!") #W RITE

-h1 "class: none"
    This is a Title

-h2 "class: header-2-class"
    And this is the subtitle

-div
    -p
    What we want to do here is being able to let others write pythoninc code while being able to
    demonstrate their findings.

    -p
    We noticed that a lot of researches and financial people are using python
    so we tought that we could do a language to help them publish their results
    faster and with a minimal learning curve. The idea is that,
    if you know python, you know how to write using our language.

%sort_list(list[type], criteria) #does not include dict or list[list]
# criteria = min/max
# type = int, double, str, char, bool

%sort_mat([i][j], criteria, i)

%median(list[type]) #type = int, double
%mode(list[type]) #type = int, double, str, char, bool
%avg(list[type]) #type = int, double
%pow(type a, int b) #type = int, double


# list = array