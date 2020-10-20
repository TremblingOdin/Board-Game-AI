import numpy as np
from collections import deque

import config

class Memory:
    def __init__(self, MEMORY_SIZE):
        self.MEMORY_SIZE = config.MEMORY_SIZE
        self.ltmemory = deque(maxlen=config.MEMORY_SIZE)
        self.stmemory = deque(maxlen=config.MEMORY_SIZE)


