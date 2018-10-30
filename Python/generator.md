> 生成器运行在堆内存中

+ 函数执行 栈帧过程

```python
import inspect

frame = None
def foo():
    bar()
def bar():
    global frame
    frame = inspect.currentframe()

foo()

print(frame.f_code.co_name)
caller_frame = frame.f_back
print(caller_frame.f_code.co_name)
caller_frame = caller_frame.f_back
print(caller_frame.f_code.co_name)

```

+ 生成器执行过程 栈帧 执行过程
```python
import dis
def genFun():

    yield 1
    name = "zero"
    yield 2
    age = 15
    tu  = 'tt'
    yield 'wind'
    return 'go'


gen = genFun()
print(dis.dis(gen))
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)

x = next(gen)
print(x)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)

x = next(gen)
print(x)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)

x = next(gen)
print(x)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)

```


