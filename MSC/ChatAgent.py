from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.aid import AID
from pade.acl.messages import ACLMessage
import sys

flag = True

class User_1(Agent):
    def __init__(self, aid, receiver_agent):
        super().__init__(aid)
        self.receiver_agent = receiver_agent
    
    def react(self, message):
        super().react(message)
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
            global flag
            if flag == True:
                msg = input('user 1:')
                message.set_content(msg)
                display_message(self.aid.localname, 'USER_1 -> {}'.format(message.content))
                self.send(message)
                if msg == 'BYE':
                    sys.exit()
                else:
                    flag = False
        except:
                print('Conversation Over!')
    
    def add_all_agents(self, receivers):
        for receiver in receivers:
            self.agentInstance.table[receiver.localname] = receiver

class User_2(Agent):
    def __init__(self, aid):
        super().__init__(aid)
    
    def react(self, message):
        super().react(message)
        self.send_message(message.sender.name)
    
    def send_message(self, receiver_agent):
        try:
            message = ACLMessage(ACLMessage.INFORM)
            message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
            message.add_receiver(receiver_agent)
            self.add_all_agents(message.receivers)
            global flag
            if flag == False:
                msg = input('user 2:')
                message.set_content(msg)
                display_message(self.aid.localname, 'USER_2 -> {}'.format(message.content))
                self.send(message)
                if msg == 'BYE':
                    sys.exit()
                else:
                    flag = True
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
    sender_agent = User_1(AID('USER 1@127.0.0.1:8080'), receiver_agent_aid)
    agents.append(sender_agent)
    start_loop(agents)