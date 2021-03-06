
# the yield statement defines a generator function, calling that function creates a generator instance
# besides returnning a value, yield can receive a value as well
# a yield expression receiving a value defines a coroutine function

# a generator can be a routine at the same with yield used in both statement and expression

# gene-routine

def generoutine():
    item = yield
    print('received item:', item)
    print('returning item:', item)
    yield item

gr = generoutine()
next(gr)  # activates first yield, so that data can be sent to it
itm = gr.send('two yields')

# with a loop

def gr_loop():
    while True:
        try:
            item = yield
            print('echoing item:', item)
            yield item
        except GeneratorExit:   # => on .close() call
            print('generator closed')
            break

gl = gr_loop()
next(gl)  # activates the yield statement (coroutine behavior), waiting for input (send() call)
r = gl.send('round one')
print('generator return:', r)
next(gl)  # advances to a new iteration after yield item return (generator behavior)
r = gl.send('round two')
print('generator return:', r)
gl.close() # raises GeneratorExit at the yield, if not caught, the generator exists quietly


# this bidirectional communication between caller and generator can be achieved by 
# one 'yield' statement

def gr2():
    di = 0
    while True:
        try:
            dr = yield di
            print(f'echoing value times 10: {dr*10}')    
            di += 1
        except StopIteration:
            print('got StopIteration signal, stop')
            break

g2 = gr2()
print('first msg from gr2:', next(g2))  # sends back 0, waiting for input (send() call)
print('second msg from gr2:', g2.send(11)) # sends back 1, receiving 11
print('third msg from gr2:', g2.send(22))  # sends back 2, receiving 22
g2.close() # received stop signal, no sending back

# Comparing above two functions gr_loop and gr2, the difference is that in gr2 the yield has 
# a return value (generator output) besides receiving value from caller
# In fact, yield statement is always bidirectional, only sometimes only one direction is in use 
# between generator and caller




