import numpy as np
import random
from collections import namedtuple, deque

import torch
import torch.nn.functional as F
import torch.optim as optim


class ReplayBuffer:
    """Buffer de taille fixe pour mémoriser les tuples d'expériences rencontrés."""

    def __init__(self, action_size, buffer_size, batch_size, seed=0):
        """Constructeur.

        Params
        ======
            action_size (int): dimension de chaque action
            buffer_size (int): taille max du buffer
            batch_size (int): taille d'un batch
            seed (int): random seed
        """
        self.action_size = action_size
        self.memory = deque(maxlen=buffer_size)  
        self.batch_size = batch_size
        self.seed = random.seed(seed)
        
        self.experience = namedtuple("Experience", field_names=["done"])
        #TODO


    
    def add(self, done):
        """Ajout d'une experience au buffer."""
        #TODO
        
    
    def sample(self):
        """Recuperation d'un minibatch de données aléatoires dans le buffer."""
        experiences = random.sample(self.memory, k=self.batch_size) 

        dones = torch.from_numpy(np.vstack([e.done for e in experiences if e is not None]).astype(np.uint8)).float()
        states = torch.from_numpy(np.vstack([e.state for e in experiences if e is not None])).float()
 
        #TODO

        
  
        return (dones)

    def __len__(self):
        """Taille courante du buffer."""
        return len(self.memory)