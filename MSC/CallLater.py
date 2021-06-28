from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.aid import AID

class HelloAgent(Agent):
    def __init__(self, aid):
        super().__init__(aid=aid)

    def on_start(self):
        super().on_start()
        self.call_later(2.0, self.print_message)

    def print_message(self):
        display_message(self.aid.localname, 'Sample Message')

if __name__ == '__main__':
    agents = list()
    agents.append(HelloAgent(AID('Agent_20000@localhost:20000')))
    start_loop(agents)