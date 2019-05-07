#!/usr/bin/python3

def mayus(word):
    if word.isupper():
        return True

def read(file_name):
    with open(file_name,'r') as f:
        for line in f:
            for word in line.split():
                if word.isupper():
                    new_upper = f"'{word}'"
                    print(new_upper)
                else:
                    print(word)



def main():
    read("a.txt")
if __name__ == "__main__":
    main()
