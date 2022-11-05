

class PlayGround:
    def __init__(self):
        pass
    def run(self):
        from testcases.testcase1 import testcase1
        testcase1().run()
        pass

playground = PlayGround()

__all__ = {'playground'}