from random import choice
import string

def preparation_list(generator_keys):
    def wraper(*args):
        mass_elements = list(range(101))
        for i in string.ascii_letters:
            mass_elements.append(i)   
        return generator_keys(mass_elements)  
    return wraper

@preparation_list
def generator_keys(mass_elements,key = str(None)):
    for i in range(15):
        key = key + str(choice(mass_elements))
    key = key[3:]
    return key

mass_elements=[]
key = generator_keys(mass_elements)
