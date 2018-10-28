def gen():
    val = 111111
    print("aa")
    while True:
        print(val*1000)
        val = yield val
        print(f"--{val}")
        val = (yield val) * 111111
        print(val*10)
        

g = gen()
print(next(g))  # 111111
print(g.send(2))  # 222222
print(g.send(3))  # 333333
