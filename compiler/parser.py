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

#----------------------------------------------
#               ARITHMETIC GRAMMAR
#----------------------------------------------

#----------------------------------------------
#
#   G   -> E | EOF
#   E   -> T E'
#   E'  -> empty | + T (+) E' | - T (-) E'
#   T   -> fT'
#   T'  -> empty | x F (*) T' | / F (/) T'
#   F   -> Lit | id | - F(-) | + F | not F | (F)
#
#-----------------------------------------------

#-----------------------------------------------
#               TERMINAL SYMBOLS
#-----------------------------------------------

#-----------------------------------------------
#
#  "+", "-", "*", "/", "=", "<", "<=", ">", ">="
#
#-----------------------------------------------

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
        pass
