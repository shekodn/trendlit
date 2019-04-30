# Trendlit - Cloud-based Programming Language

## Setup
Make sure to install python3.7 and Docker. Also, don't forget to install trendlit's requirements:

`pip3 install -r requirements.txt `

## How To Run
It is almost as easy as pie. Just build the docker image by doing `make build`

Then simply do `make run`

If `http://localhost`  is up and running, we are golden.

## Main Semantic Characteristics 
- There is only one script section.
- If script section is present, then it is defined at the top of the program. (before any html tag)
- Any variable defined in a script will be treated as a global variable.
- There can be n number of defined functions by the user.
- Any variable inside function in the script or embedded-script will be treated as a local variable.
- All variable names must be unique within a scope.
- There must be consistency between the defined type of a variable and the values it is assigned later on.

## Compilation Process
- In VERY general terms this is what happens after you finish writing your code in Trendlit.
- Lexer and Parser analyze your code !
- A semantic evaluation is done !
- Internal code is generated (Gimme those Quadz!)
- All your logic is sent to a virtual machine for processing!
- The results of your code are back from the virtual machine!
- You get a beautiful and usable HTML file to showcase in any browser !

We do a bunch of magic in the background, but the cool part is you don’t need to worry about any of that just focus on doing some fun stuff with Trendlit.

## Cool.. but how do I program in trendlit?
### Sample Code 

```
program the_name_of_the_program script {}
h1 {
<^ "Trendlit - Cloud Based Programming Language" ^>
}
h2 {
<^ "Hello World!" ^>
}
p {
<^ "I don't want to show off, but did you know that" ^>
<^ "2 + 2" ^>
<^ "is"^>
<^ 2+ 2^>
<^ "?"^>
}
        
```
