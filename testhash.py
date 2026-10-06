from my_hash import MyHashMap

m = MyHashMap()

m.put("mokshitha", 100)
m.put("Tejaswi", 200)

print("Tejaswi:", m.get("Tejaswi"))
m.put("Tejaswi",300)
print("Tejaswi:", m.get("Tejaswi"))
print("Size:", m.size)
print("Capacity:", m.capacity)
print(m.get("mokshitha"))


# remove
m.put("a", 100)
m.put("i", 200)
print("a:", m.get("a"))
print("i:", m.get("i"))
print("Size:", m.size)
m.remove("a")
print("After removing a:", m.get("a"))
print("Size:", m.size)

# resizing
m.put("a", 100)
m.put("b", 200)
m.put("c", 300)
m.put("d", 400)
m.put("e", 500)

print("Before resize:")
print("Size:", m.size)
print("Capacity:", m.capacity)

m.put("f", 600)

print("After resize:")
print("Size:", m.size)
print("Capacity:", m.capacity)

print("a:", m.get("a"))
print("b:", m.get("b"))
print("c:", m.get("c"))
print("d:", m.get("d"))
print("e:", m.get("e"))
print("f:", m.get("f"))

# findnode
node = m.find_node("a")

print(node)