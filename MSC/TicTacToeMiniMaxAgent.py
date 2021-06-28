from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.aid import AID
from pade.acl.messages import ACLMessage
import sys, time

board = [['.','.','.'],
         ['.','.','.'],
         ['.','.','.']]

def printBoard():
    print("\nTIC-TAC-TOE   Board Positions\n")
    print(board[0][0] + " | " + board[0][1] + " | " + board[0][2] + "     (0,0) | (0,1) | (0,2)")
    print(board[1][0] + " | " + board[1][1] + " | " + board[1][2] + "     (1,0) | (1,1) | (1,2)")
    print(board[2][0] + " | " + board[2][1] + " | " + board[2][2] + "     (2,0) | (2,1) | (2,2)")
    print("\n")

def is_valid(px, py):
    if px < 0 or px > 2 or py < 0 or py > 2:
        return False
    elif board[px][py] != '.':
        return False
    else:
        return True

def is_end():
    for i in range(0, 3):
        if (board[0][i] != '.' and
            board[0][i] == board[1][i] and
            board[1][i] == board[2][i]):
            return board[0][i]

    for i in range(0, 3):
        if (board[i] == ['X', 'X', 'X']):
            return 'X'
        elif (board[i] == ['O', 'O', 'O']):
            return 'O'

    if (board[0][0] != '.' and
        board[0][0] == board[1][1] and
        board[0][0] == board[2][2]):
        return board[0][0]

    if (board[0][2] != '.' and
        board[0][2] == board[1][1] and
        board[0][2] == board[2][0]):
        return board[0][2]

    for i in range(0, 3):
        for j in range(0, 3):
            if (board[i][j] == '.'):
                return None

    return '.'

def max():
    maxv = -2

    px = None
    py = None

    result = is_end()

    if result == 'X':
        return (-1, 0, 0)
    elif result == 'O':
        return (1, 0, 0)
    elif result == '.':
        return (0, 0, 0)

    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                board[i][j] = 'O'
                (m, min_i, min_j) = min()
                if m > maxv:
                    maxv = m
                    px = i
                    py = j
                board[i][j] = '.'
    return (maxv, px, py)

def min():
    minv = 2

    qx = None
    qy = None

    result = is_end()

    if result == 'X':
        return (-1, 0, 0)
    elif result == 'O':
        return (1, 0, 0)
    elif result == '.':
        return (0, 0, 0)

    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                board[i][j] = 'X'
                (m, max_i, max_j) = max()
                if m < minv:
                    minv = m
                    qx = i
                    qy = j
                board[i][j] = '.'
    return (minv, qx, qy)


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
        try:
            message = ACLMessage(ACLMessage.INFORM)
            message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
            message.add_receiver(self.receiver_agent)
            self.add_all_agents(message.receivers)
            
            printBoard()
            result = is_end()

            if result != None:
                if result == 'X':
                    print('The winner is X!')
                elif result == 'O':
                    print('The winner is O!')
                elif result == '.':
                    print("It's a tie!")
                    sys.exit()
            
            start = time.time()
            (m, qx, qy) = min()
            end = time.time()
            print('Evaluation time: {}s'.format(round(end - start, 7)))
            print('Recommended move: X = {}, Y = {}'.format(qx, qy))

            px = int(input('Insert the X coordinate: '))
            py = int(input('Insert the Y coordinate: '))
            message.set_content('Human Agent played "X" at position ({},{})'.format(px, py))

            if is_valid(px, py):
                board[px][py] = 'X'
            else:
                print('The move is not valid! Try again.')

            self.send(message)
        except:
            print("Game Over! (•‿ •)")
    
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
        
        result = is_end()

        if result != None:
            if result == 'X':
                print('The winner is X!')
            elif result == 'O':
                print('The winner is O!')
            elif result == '.':
                print("It's a tie!")

        (m, px, py) = max()
        board[px][py] = 'O'
        
        message.set_content('Computer Agent played "O" at ({},{}) position.'.format(px, py))
        self.send(message)
    
    def add_all_agents(self, receivers):
        for receiver in receivers:
            self.agentInstance.table[receiver.localname] = receiver
    
if __name__ == '__main__':
    agents = list()
    receiver_agent_aid = AID('Computer Agent')
    receiverAgent = Computer(receiver_agent_aid)
    agents.append(receiverAgent)
    sender_agent = Human(AID('Human Agent'), receiver_agent_aid)
    agents.append(sender_agent)
    start_loop(agents)