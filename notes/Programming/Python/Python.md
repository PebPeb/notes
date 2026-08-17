# Python

## Virtual Environments

A virtual environment acts as a workspace that you can install different packages to and set up for specific projects. This can be handy as some packages my interfere with each other or some projects require older or new versions of a package. To set up a simple virtual environment the following command can be used.

``` bash
python3 -m venv <env_name>
```

To use that virtual environment you must `source` the `active` in the environments `bin` directory.


``` bash
source ~/.venv/<env_name>/bin/active
```

This is an example in reality the virtual environment may be located in a different directory.

## Decorator

What is a decorator? It is a short hand to "wrap" another function to extend its behavior.

``` python
@test
def my_function()
  pass
```

Above is the exact same way of saying the following.

``` python
def my_function()
  pass

my_function = test(my_function)
```

Example of creating a custom decorator.

``` python
def test(func):
    def wrapper():
        print(f"Testing the function: {func.__name__}")
        func()
        print("Test complete!")
    return wrapper

@test
def say_hello():
    print("Hello World!")

say_hello()
```

```
Testing the function: say_hello
Hello World!
Test complete!
```




## [Asynchronous I/O (asyncio)](https://docs.python.org/3/library/asyncio-runner.html)

Asyncio is a library to write concurrent code using the async/await syntax.

``` python
import asyncio
```

### [Runners](https://docs.python.org/3/library/asyncio-runner.html)

This function runs the awaitable, taking care of managing the asyncio event loop, finalizing asynchronous generators, and closing the executor.

This function cannot be called when another asyncio event loop is running in the same thread.


``` python
asyncio.run(coro, *, debug=None, loop_factory=None)
```

Example:

``` python
async def main():
    await asyncio.sleep(1)
    print('hello')

asyncio.run(main())
```


### [Coroutines and tasks](https://docs.python.org/3/library/asyncio-task.html)

Coroutines declared with the async/await syntax is the preferred way of writing asyncio applications. 

Awaiting on a coroutine. The following snippet of code will print “hello” after waiting for 1 second, and then print “world” after waiting for another 2 seconds.

``` python
import asyncio
import time

async def say_after(delay, what):
  await asyncio.sleep(delay)
  print(what)

async def main():
  print(f"started at {time.strftime('%X')}")

  await say_after(1, 'hello')
  await say_after(2, 'world')

  print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
```

The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks. Rather than taking 3 seconds like the previous example with will only take 2 as they are run together.

``` python
async def main():
  task1 = asyncio.create_task(
    say_after(1, 'hello'))

  task2 = asyncio.create_task(
    say_after(2, 'world'))

  print(f"started at {time.strftime('%X')}")

  # Wait until both tasks are completed (should take
  # around 2 seconds.)
  await task1
  await task2

  print(f"finished at {time.strftime('%X')}")
```

