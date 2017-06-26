class Relet:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
#declaring string variable
namever = "mynameisokky"
#initialize relet
s = Relet()
#scan the length of the string value
len(namever)
#push the value of string to Relet
s.push(namever)
#print out the last value
print(s.peek())

print "------now popping out and reverse the value using the stack-----"
#take out the original string value
s.pop()
#push the reverse string
s.push('ykkosiemanym')

print "--------this is the result------"
#print out the string
print(s.peek())
