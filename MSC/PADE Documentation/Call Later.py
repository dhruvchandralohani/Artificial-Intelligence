from pade.misc.utility import display_message, start_loop, call_later
from pade.core.agent import Agent
from pade.acl.aid import AID
'''
With PADE, it is possible to postpone the execution of a given piece of code in a very simple way! Just use the call_later () method available in the Agent () class .
To use the call_later () , the following parameters should be given: time delay, callback method and its args.
'''
class HelloAgent(Agent):
    def __init__(self, aid):
        super(HelloAgent, self).__init__(aid=aid, debug=False)

    def on_start(self):
        super().on_start()
        self.call_later(5.0, self.say_hello)

    def say_hello(self):
        display_message(self.aid.localname, "Hello, I\'m an agent!")


if __name__ == '__main__':
    agents = list()
    hello_agent = HelloAgent(AID(name='hello_agent'))
    agents.append(hello_agent)
    start_loop(agents)
