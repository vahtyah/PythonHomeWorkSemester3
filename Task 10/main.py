class MealyError(Exception):
    def __init__(self, method_name):
        self.method_name = method_name

    def __str__(self):
        return self.method_name


class MealyMachine:
    def __init__(self):
        self.state = 'A'

    def jog(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 4
        elif self.state == 'E':
            self.state = 'F'
            return 6
        else:
            raise MealyError("jog")

    def flip(self):
        if self.state == 'B':
            return 2
        elif self.state == 'E':
            self.state = 'B'
            return 7
        elif self.state == 'F':
            self.state = 'G'
            return 8
        elif self.state == 'G':
            self.state = 'D'
            return 9
        elif self.state == 'D':
            self.state = 'A'
            return 5
        else:
            raise MealyError("flip")


def test():
    machine = main()
    assert machine.jog() == 0
    assert machine.flip() == 2
    assert machine.flip() == 2
    assert machine.jog() == 1
    assert machine.jog() == 3
    assert machine.jog() == 4
    assert machine.jog() == 6
    assert machine.flip() == 8
    try:
        machine.jog()
    except MealyError as e:
        assert str(e) == "jog"
        assert e.method_name == "jog"
    assert machine.flip() == 9
    assert machine.jog() == 4
    assert machine.flip() == 7
    assert machine.jog() == 1
    try:
        machine.flip()
    except MealyError as e:
        assert str(e) == "flip"
        assert e.method_name == "flip"
    assert machine.jog() == 3
    assert machine.flip() == 5


def main():
    return MealyMachine()