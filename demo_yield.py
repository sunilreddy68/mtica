def demo_yield():
    print('code segment1 execute')
    x=7
    yield x*x
    print('code segment2 execue')
    yield 2
    print('code segment1 execue')
    yield 3
    print('code segment4 execue')
