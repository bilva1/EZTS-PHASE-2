import queue
a=queue.Queue()
b=queue.Queue()
for x in range(5):
    b.put(x)
print(a.empty())
print(b.empty())

L=queue.Queue(maxsize=5)
L.put(1)
L.put(2)
L.put(3)
print(L.qsize())
print(type(L))
print(L.get())
print(L.get())
