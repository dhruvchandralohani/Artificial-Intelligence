from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent, AID
from pade.behaviours.protocols import TimedBehaviour

class MyTimedBehaviour(TimedBehaviour):
    def on_time(self):
        super().on_time()
        display_message(self.agent.aid.localname, 'Hello World!')

class MyAgent(Agent):
    def __init__(self, aid):
        super().__init__(aid=aid)
        behaviour = MyTimedBehaviour(self, 1.0)
        self.behaviours.append(behaviour)

if __name__ == '__main__':
    agents = list()
    agent_name = 'agent_hello_20000@localhost:20000'
    timed_agent = MyAgent(AID(name=agent_name))
    agents.append(timed_agent)
    start_loop(agents)