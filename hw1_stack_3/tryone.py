class Stackfor:

  def __init__(self):
        self.items = []

  def is_empty(self):
        return self.items == []

  def pop(self):
        return self.items.pop()

  def push(self, item):
        self.items.append(item)

  def peek(self):
        return self.items[len(self.items)-1]

  def size(self):
        return len(self.items)

troto = "satchelisthebest"
wo = Stackfor()
len(troto)
wo.push(troto)
print(wo.peek())
wo.pop()
wo.push("tsebehtsilehctas")
print(wo.peek())
