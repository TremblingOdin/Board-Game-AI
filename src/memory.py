import numpy as np
from collections import deque

import config

class Memory:
    def __init__(self, MEMORY_SIZE):
        self.MEMORY_SIZE = config.MEMORY_SIZE
        # long term memory
        self.ltmemory = deque(maxlen=config.MEMORY_SIZE)
        # short term memory
        self.stmemory = deque(maxlen=config.MEMORY_SIZE)

    def commit_stmemroy(self, identities, state, action_values):
        for r in identities(state, action_values):
            self.stmemory.append({
                'board': r[0].board
                , 'state': r[0]
                , 'id': r[0].id
                , 'AV': r[1]
                , 'playerTurn': r[0].player_turn
                })

    def commit_ltmemory(self):
        for i in self.stmemory:
            self.ltmemory.append(i)
        self.clear_stmemory()

    def clear_stmemory(self):
        self.stmemory=deque(maxlen=config.MEMORY_SIZE)
