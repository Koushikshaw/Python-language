dict={"hello":"greet or way to start the communication \n\tsynonym is hii\n\tlink to read more : https://www.dictionary.com/browse/hello","hii":"form of greet to start a talk \n\tsynonym is hello"}

choice = input("What do you want to do (search/add) : ")

if choice == "search" :
    word = input("Enter the word to search : ")
    value = dict[word]
    print(f"Word : {word}\nDefination : {value}")
else : 
    word = input("Enter the word you want to add : ")
    value = input("Enter the defination of the word you entered ")
    dict[word]=value
    print(dict)
