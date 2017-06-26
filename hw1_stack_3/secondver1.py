class Marquise:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


rotomau = "yeahtheschoolisstarted"

d = Marquise()

d.push("Lalaisthebigmoney")
print(d.peek())
d.pop()
d.push("yenomgibehtsialal")
print(d.peek())

print "------Now with the different code!!-------"

e = Marquise()
len(rotomau)
e.push(rotomau)
print(e.peek())
print "checking the value!"
print "----reversing the string value-------"
e.pop()
e.push("detratssiloohcsehthaey")
print(e.peek())
print "see the differences?"
