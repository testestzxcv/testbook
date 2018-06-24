def yell(text):
    return text.upper() + '!'

print(yell('hello'))

bark = yell

print(bark('woof'))

# del yell

print(bark('hey'))

print(bark.__name__)

funcs = [bark, str.lower, str.capitalize]
print(funcs)

for f in funcs:
    print(f, f('hey there'))

print(funcs[0]('heyho'))

def greet(func):
    greeting = func('Hi, I am a Python program')
    print(greeting)

print(greet(yell))

def whisper(text):
    return text.lower() + '...'

print(greet(whisper))

print(list(map(yell, ['hello','hey','hi'])))

def speak(text):
    def whisper(t):
        return t.lower() + '...'
    return whisper(text)

print(speak('Hello World'))

def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'
    def yell(text):
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return whisper

print(get_speak_func(0.3))
print(get_speak_func(0.7))

speak_func = get_speak_func(0.7)
print(speak_func('Hello'))

def get_speak_func(text, volume):
    def whisper():
        return text.lower() + '...'
    def yell():
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return whisper

print(get_speak_func('Hello, World', 0.7)())


def make_adder(n):
    def add(x):
        return x + n
    return add

plus_3=make_adder(3)
plus_5 = make_adder(5)

print(plus_3(4))
print(plus_5(4))

class Adder:
    def __init__(self, n):
        self.n = n
    def __call__(self, x):
        return self.n + x

plus_3 = Adder(3)
print(plus_3(4))

d = 3
c = '3'

print(callable(plus_3))
print(callable(d))
print(callable(c))