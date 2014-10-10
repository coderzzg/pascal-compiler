# -*- parser.py -*-
# -*- MIT License (c) 2014 David Leonard -*-
# -*- drksephy.github.io -*-

#----------------------------------------
#                  TODO      
#----------------------------------------

# - [done] Consumes tokens one at a time
# - [    ] Needs grammar to handle arithmetic structures
# - [    ] Needs to handle if statements
# - [    ] Needs to handle while statements
# - [    ] Needs to handle for statements
# - [    ] Needs to handle if-then-else statements
# - [    ] Create functions to handle each token
# - [    ] Returns parse tree

class Parser(object):

    def __init__(self, tokens, curr_token, op):
        # Parameters:
        #   * tokens : list of tuples of tokens
        #       - tokens produced by scanner
        #   * curr_token : current token being processed
        #       - current token being read
        #   * op : current operation to handle
        #       - current operation to print to stack
        self.tokens     = tokens
        self.curr_token = curr_token
        self.op         = op

    def parse(self):
        iterator = self.get_token()
        # self.curr_token = iterator.next()
        for i in range(1, 29):
            self.curr_token = iterator.next()
            print self.curr_token

    def get_token(self):
        # Returns an iterator for tokens
        tokens = iter(self.tokens)
        return tokens

    def expression(self):
    # Function for building expressions
        pass

    def term(self):
    # Function for building terms
        pass

    def factor(self):
    # Function for building factors
        pass

        



        

