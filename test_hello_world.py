from unittest import TestCase

from HelloWorld import World


class HelloWorldTestCase(TestCase):

    def test_base_case(self):
        world = World()
        self.assertIn("Hello world", world.hello())

    def test_custom_case(self):
        world = World()
        custom = "Ciao ciao"
        self.assertIn("Hello world", world.hello(greeting=custom))
