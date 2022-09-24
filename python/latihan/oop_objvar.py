class Robot:
    """represent a robot , with a name"""

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """initialize the data."""
        self.name = name
        print("(Initializing {})".format(self.name))

        # When this person is created,
        # the robot add the population
        Robot.population += 1

    def die(self):
        """I am dying."""
        print("{} is being destroyed".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("The last one standing is {}".format(self.name))
        else:
            print("There are still {:d} working.".format(Robot.population))
    
    def say_hi(self):
        """Greeting by the robot.

        Yeah, they can do that."""
        print("Greetings, my master call me {}".format(self.name))

    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} population".format(Robot.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()

'''How It Works

This is a long example but helps demonstrate the nature of class and object variables. Here, population belongs to the Robot class and hence is a class variable. The name variable belongs to the object (it is assigned using self) and hence is an object variable.

Thus, we refer to the population class variable as Robot.population and not as self.population. We refer to the object variable name using self.name notation in the methods of that object. Remember this simple difference between class and object variables. Also note that an object variable with the same name as a class variable will hide the class variable!

Instead of Robot.population, we could have also used self.__class__.population because every object refers to its class via the self.__class__ attribute.

The how_many is actually a method that belongs to the class and not to the object. This means we can define it as either a classmethod or a staticmethod depending on whether we need to know which class we are part of. Since we refer to a class variable, let's use classmethod.

We have marked the how_many method as a class method using a decorator.'''