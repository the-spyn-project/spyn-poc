from multiprocessing.dummy import Pool as ThreadPool


def add(a, b):
    return a+b


def sub(a,b):
    return a-b

def mul(a,b):
    return a*b


def one_to_one_app(pool, ops, data):

    res = []
    for i in range(len(ops)):
        res.append(pool.starmap(ops[i], data[i]))

    return res


pool = ThreadPool(4)
results = pool.starmap(add, zip([1, 2], [3, 4]))

ops = [add, sub,  mul, mul]
data = [zip([1], [2]), zip([2], [3]), zip([3], [4]), zip([4], [5])]

print(one_to_one_app(pool, ops, data))


pool.close()
pool.join()
