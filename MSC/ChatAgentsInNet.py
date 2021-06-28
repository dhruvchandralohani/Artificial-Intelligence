from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.aid import AID
from pade.acl.messages import ACLMessage
import sys

class User_1(Agent):
    def __init__(self, aid, receiver_agent):
        super().__init__(aid)
        self.receiver_agent = receiver_agent
    
    def react(self, message):
        super().react(message)
        display_message(self.aid.localname, 'USER_2 -> {}'.format(message.content))
        self.send_message()
    
    def on_start(self):
        super().on_start()
        self.send_message()

    def send_message(self):
        try:
            message = ACLMessage(ACLMessage.INFORM)
            message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
            message.add_receiver(self.receiver_agent)
            self.add_all_agents(message.receivers)
            msg = input('user 1:')
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
    sender_agent = User_1(AID('USER 1@27.7.233.156:8080'), AID('USER 2@27.7.233.156:8081'))
    agents.append(sender_agent)
    start_loop(agents)