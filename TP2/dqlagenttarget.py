import numpy as np
import random
from collections import namedtuple, deque

from model import QNN
from expereplay import ReplayBuffer

import torch
from torch import nn
import torch.nn.functional as F
import torch.optim as optim


class DQLAgentTarget():
     """Agent qui utilise l'algorithme de deep QLearning."""

    def __init__(self, seed=0):
        """Constructeur.
        
        Params
        ======
            seed (int): random seed
        """
        self.seed = random.seed(seed)

        #TODO