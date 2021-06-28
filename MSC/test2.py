from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.aid import AID
from pade.acl.messages import ACLMessage
import sys

class User_2(Agent):
    def __init__(self, aid):
        super().__init__(aid)
    
    def react(self, message):
        try:
            super().react(message)
            display_message(self.aid.localname, 'USER_1 -> {}'.format(message.content))
            msg = message.content
            if msg == 'BYE':
                sys.exit()
            self.send_message(message.sender.name)
        except:
            print('Conversation Over!')
    
    def send_message(self, receiver_agent):
        try:
            message = ACLMessage(ACLMessage.INFORM)
            message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
            message.add_receiver(receiver_agent)
            self.add_all_agents(message.receivers)
            msg = input('user 2:')
            message.set_content(msg)
            self.send(message)
            if msg == 'BYE':
                sys.exit()
        except:
            print('Conversation Over!')
    
    def add_all_agents(self, receivers):
        for receiver in receivers:
            self.agentInstance.table[receiver.localname] = receiver
    
if __name__ == '__main__':
    agents = list()
    receiver_agent_aid = AID('USER 2@127.0.0.1:8081')
    receiverAgent = User_2(receiver_agent_aid)
    agents.append(receiverAgent)
    start_loop(agents)