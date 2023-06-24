from queue import LifoQueue
s=LifoQueue(maxsize=3)
print(s.qsize())
s.put('a')
s.put('b')
s.put('c')
print(f"stack full? {s.full()}")
print(f"size={s.qsize()}")
    
print(s.get())
print(s.get())
print(s.get())
print(f"stack empty? {empty()}")
