from .time_util import sleep
from selenium.webdriver import ActionChains

class Actions(ActionChains):
    def wait(self, time_s):
        self._actions.append(lambda: sleep(time_s))
        return self

    def print_it(self, text):
        self._actions.append(lambda: print(text))
        return self