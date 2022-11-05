from debugutility import monitor_function

class testcase1:
    @monitor_function(ignore_self=True)
    def displaystring(self, a):
        print(a)
    @monitor_function()
    def run(self):
        print('this is a test case to print in console')
        self.displaystring('a string to be printed')

__all__ = {'testcase1'}