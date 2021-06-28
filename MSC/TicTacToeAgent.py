from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.aid import AID
from pade.acl.messages import ACLMessage
import random, sys

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

magicsquare = [8, 3, 4,
               1, 5, 9,
               6, 7, 2]

def checkWon(symbol):
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if i != j and j != k and k != i:
                    if board[i] == board[j] == board[k] == symbol:
                        if magicsquare[i] + magicsquare[j] + magicsquare[k] == 15:
                            return True
    return False

def checkTie():
    flag = True
    for i in range(9):
        if board[i] == '-':
            flag = False
            break
    return flag

def printBoard():
    print("\nTIC-TAC-TOE   Board Positions\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")

def blockHuman():
    for move in ['X', 'O']:
        for i in range(3):
            sm = 0
            j = i * 3
            if board[j] == board[j + 1] == move:
                sm = magicsquare[j] + magicsquare[j + 1]
            elif board[j] == board[j + 2] == move:
                sm = magicsquare[j] + magicsquare[j + 2]
            elif board[j + 1] == board[j + 2] == move:
                sm = magicsquare[j + 1] + magicsquare[j + 2]
            if sm != 0:
                pos = magicsquare.index(15 - sm)
                if board[pos] == '-':
                    return pos
    for move in ['X', 'O']:
        for j in range(3):
            sm = 0
            if board[j] == board[j + 3] == move:
                sm = magicsquare[j] + magicsquare[j + 3]
            elif board[j] == board[j + 6] == move:
                sm = magicsquare[j] + magicsquare[j + 6]
            elif board[j + 3] == board[j + 6] == move:
                sm = magicsquare[j + 3] + magicsquare[j + 6]
            if sm != 0:
                pos = magicsquare.index(15 - sm)
                if board[pos] == '-':
                    return pos
    for move in ['X', 'O']:
        sm = 0
        if board[0] == board[4] == move:
            sm = magicsquare[0] + magicsquare[4]
        elif board[0] == board[8] == move:
            sm = magicsquare[0] + magicsquare[8]
        elif board[4] == board[8] == move:
            sm = magicsquare[4] + magicsquare[8]
        if sm != 0:
                pos = magicsquare.index(15 - sm)
                if board[pos] == '-':
                    return pos
    for move in ['X', 'O']:
        sm = 0
        if board[2] == board[4] == move:
            sm = magicsquare[2] + magicsquare[4]
        elif board[2] == board[6] == move:
            sm = magicsquare[2] + magicsquare[6]
        elif board[4] == board[6] == move:
            sm = magicsquare[4] + magicsquare[6]
        if sm != 0:
                pos = magicsquare.index(15 - sm)
                if board[pos] == '-':
                    return pos
        randMoves = []
        for i in range(9):
            if board[i] == '-':
                randMoves.append(i)
        if len(randMoves) != 0:
            return randMoves[random.randint(0, len(randMoves))]

class Human(Agent):
    def __init__(self, aid, receiver_agent):
        super().__init__(aid)
        self.receiver_agent = receiver_agent
    
    def react(self, message):
        super().react(message)
        display_message(self.aid.localname, 'Message received from {}'.format(message.sender.name))
        display_message(self.aid.localname, 'Message is {}'.format(message.content))
        self.send_message()
    
    def on_start(self):
        super().on_start()
        self.send_message()

    def send_message(self):
        message = ACLMessage(ACLMessage.INFORM)
        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        message.add_receiver(self.receiver_agent)
        self.add_all_agents(message.receivers)
        
        pos = int(input('Enter the position: '))
        board[pos - 1] = 'X'
        printBoard()
        
        if checkWon('X'):
            print('You won!')
            sys.exit()
        
        if not checkWon('X'):
            if not checkWon('O'):
                if checkTie():
                    print("It's a TIE")
                    sys.exit()
        
        message.set_content('Human Agent played "X" at position {}'.format(pos))
        self.send(message)
    
    def add_all_agents(self, receivers):
        for receiver in receivers:
            self.agentInstance.table[receiver.localname] = receiver

class Computer(Agent):
    def __init__(self, aid):
        super().__init__(aid)
    
    def react(self, message):
        super().react(message)
        display_message(self.aid.localname, 'Message received from {}'.format(message.sender.name))
        display_message(self.aid.localname, 'Message is {}'.format(message.content))
        self.send_message(message.sender.name)
    
    def send_message(self, receiver_agent):
        message = ACLMessage(ACLMessage.INFORM)
        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        message.add_receiver(receiver_agent)
        self.add_all_agents(message.receivers)
        
        winMove = blockHuman()
        board[winMove] = 'O'
        printBoard()
        
        if checkWon('O'):
            print('You Lost!')
            sys.exit()
        
        if not checkWon('X'):
            if not checkWon('O'):
                if checkTie():
                    print('It is a TIE')
                    sys.exit.write("BYE")
        
        message.set_content('Computer Agent played "O" at {} position.'.format(winMove+1))
        self.send(message)
    
    def add_all_agents(self, receivers):
        for receiver in receivers:
            self.agentInstance.table[receiver.localname] = receiver
    
if __name__ == '__main__':
    agents = list()
    printBoard()
    receiver_agent_aid = AID('Computer Agent')
    receiverAgent = Computer(receiver_agent_aid)
    agents.append(receiverAgent)
    sender_agent = Human(AID('Human Agent'), receiver_agent_aid)
    agents.append(sender_agent)
    start_loop(agents)