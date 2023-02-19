# -*- coding: utf-8 -*-
"""
Date: Feb 19th 2023
@author: Juan Pablo Brasdefer (juanbrasdefer) Fabian Pawelczyk (fpawelczyk)
"""
import numpy as np
from abc import ABCMeta, abstractmethod

# Abstract base class for creatures
class Creature(metaclass=ABCMeta):

    # Constructor for Creature object
    def __init__(self, ind):
        self.ind = ind  # Index of a creature in ecosystem.

    # Abstract method to be implemented by subclasses
    @abstractmethod
    def move(self):
        """Return index to move"""

# Class for Bear creatures
class Bear(Creature):

    # Returns string representation of Bear object
    def __repr__(self):
        return "Bear(%s)" % self.ind

    # Move method for Bear objects
    def move(self):
        # Bear moves left or right randomly
        to = np.random.choice([-1, 1])
        new_ind = self.ind + to
        # Print message indicating movement
        print(self, "moves", "left" if to == -1 else "right")
        return new_ind

# Class for Fish creatures
class Fish(Creature):

    # Returns string representation of Fish object
    def __repr__(self):
        return "Fish(%s)" % self.ind

    # Move method for Fish objects
    def move(self):
        # Fish moves left or right randomly
        to = np.random.choice([-1, 1])
        new_ind = self.ind + to
        # Print message indicating movement
        print(self, "moves", "left" if to == -1 else "right")
        return new_ind