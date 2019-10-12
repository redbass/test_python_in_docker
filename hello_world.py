from faker import Faker


class World:

    def __init__(self):
        self.faker = Faker()

    def hello(self, greeting=None):
        the_greeting = "Hello world " + self.faker.name() or greeting
        return the_greeting


if __name__ == '__main__':
    world = World()
    print(world.hello())
