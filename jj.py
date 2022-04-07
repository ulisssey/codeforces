from jinja2 import Template


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


me = Person('Erasyl', 18)
tm = Template("My name is {{ me.name }} and i am {{ me.age }} years old.")
msg = tm.render(me=me)
print(msg)