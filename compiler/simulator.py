# -*- simulator.py -*-
# -*- MIT License (c) 2014 David Leonard -*-
# -*- drksephy.github.io -*-

#---------------------------------------
#                  TODO
#---------------------------------------

# - [   ] Create code array
# - [   ] Create data array
# - [   ] Create stack array
# - [   ] Implement opcodes
# - [   ] Create simulator 
# - [   ] Build symbol tables

class Simulator(object):

    def __init__(self, ast, stack, symtable, ip):
        # Paramaters
        #   * ast : List
        #       - Abstract Syntax Tree returned by Parser
        #   * stack : List
        #       - Stack of operands
        #   * symtable: List
        #       - List of all allocated variables
        #   * ip: Integer
        #       - Points to current instruction address
        self.ast        = ast
        self.stack      = stack
        self.symtable   = symtable
        self.ip         = ip


    #--------------------------
    #         SIMULATOR
    #--------------------------
    def simulate(self, ast):
        for node in ast:
            print node


    