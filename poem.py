import random as random 


""" What Next BY FREDERICK SEIDE""" 

poem = """So the sun is shining blindingly but I can sort of see
It’s like looking at Mandela’s moral beauty
The dying leaves are sizzling on the trees
In a shirtsleeves summer breeze
But daylight saving is over
And gaveling the courtroom to order with a four-leaf clover
Is over. And it’s altogether November.
And the Pellegrino bubbles rise to the surface and dismember"""


string_list = poem.split("\n")


def lines_printed_backwards(string_list):
    """
    Takes in a list of strings containing the lines of the poem as arguments and 
    prints the poem lines out in reverse with the line numbers reversed
    """

    i = len(string_list)
    string_list.reverse()

    for string in string_list:
        print(f'{str(i)} {string}')
        i -= 1


def lines_printed_random(string_list):
    """
    Randomly selects lines from a list of strings and prints them out in random order
    """

    for _ in string_list:
        print(random.choice(string_list))
 

def list_rearrange(string_list):
    """
    Prints each line in reverse
    """

    for line in string_list:
        print(line[::-1])


def list_rearrange_words(string_list):
    """
        Rearranges the words on each line.
    """
    rand = random.randint(0, len(string_list))

    for index in range(len(string_list)):
        temp = string_list[index]
        string_list[index] = string_list[rand]
        string_list[rand] = temp
    print(string_list)    



lines_printed_backwards(string_list)

lines_printed_random(string_list)

list_rearrange(string_list)

list_rearrange_words(string_list)