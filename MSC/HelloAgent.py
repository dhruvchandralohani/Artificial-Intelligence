from pade.core.agent import Agent, AID, display_message

class MyAgent(Agent):
    def __init__(self, aid):                        # __init__ is a reserved method in Python classes.
        super().__init__(aid = aid)                 # By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
        display_message(self.aid.name, 'Hello!')
        #print(self.aid.name, ':','Hello!') This can be used instead of display_message

MyAgent(AID('Agent'))                               # You can pass port number like this "@localhost:20000" as an argument to AID() to run this at port no 20000.
                                                    # Empty arguments for AID() will print "[None]"" as the agent name when display_message() is used.