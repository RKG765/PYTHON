# strip function is used to clean the extra spaces
def remove_and_split(string, word):
    newstr = string.replace(word, "")
    return newstr.strip()

this = "    Raj is a good boy     "
n = remove_and_split(this, "Raj")
print(n)