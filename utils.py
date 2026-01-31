
def readFasta(fileName):
    with open(fileName) as file:
        textContent = file.read()
        begin = textContent.find("\n")
        head = textContent[0 : begin]
        genome = textContent[begin+1:].replace("\n", "")
        return head, genome

def reverseComplement(s):
    ans = ""
    d = {"A" : "T", "T" : "A", "G" : "C", "C" : "G"}
    for letter in s:
        ans += d[letter]
    return ans

# head, genome = readFasta("Salmonella_enterica")
# print(head)
# print(genome[:30])