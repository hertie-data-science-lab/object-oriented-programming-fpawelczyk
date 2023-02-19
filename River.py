# -*- coding: utf-8 -*-
"""
Date: Feb 19th 2023
@author: Fabian Pawelczyk
"""
import numpy as np
from Creatures import Bear
from Creatures import Fish
from abc import ABCMeta, abstractmethod


class Creature(metaclass=ABCMeta):

    def __init__(self, ind):
        self.ind = ind  # Index of a creature in ecosystem.

    @abstractmethod
    def move(self):
        """Return index to move"""


class Bear(Creature):

    def __repr__(self):
        return "Bear(%s)" % self.ind

    def move(self):
        to = np.random.choice([-1, 1])
        new_ind = self.ind + to
        print(self, "advances", "left" if to == -1 else "right")
        return new_ind


class Fish(Creature):

    def __repr__(self):
        return "Fish(%s)" % self.ind

    def move(self):
        to = np.random.choice([-1, 1])
        new_ind = self.ind + to
        print(self, "swims", "left" if to == -1 else "right")
        return new_ind


class River:

    def __init__(self, n_room):
        self.n_room = n_room
        self.eco = None

    def initialize(self):
        self.eco = []
        creatures = np.random.choice([Bear, Fish, None], size=self.n_room)
        for ind, creature in enumerate(creatures):
            self.eco.append(creature(ind) if creature is not None else None)

    def next_time_step(self, n=1, verbose=True):
        for i in range(n):
            moving_ind = np.random.choice(list(range(self.n_room)))
            if self.eco[moving_ind] is None:
                print("There is no activity...")
                pass
            else:
                new_ind = self.eco[moving_ind].move()
                if new_ind < 0 or new_ind > len(self.eco) - 1:
                    pass
                elif isinstance(self.eco[moving_ind], Bear):
                    if isinstance(self.eco[new_ind], Bear):
                        pass
                    elif isinstance(self.eco[new_ind], Fish):
                        self.eco[new_ind] = Bear(new_ind)
                        self.eco[moving_ind] = None
                    else:
                        self.eco[new_ind] = Bear(new_ind)
                elif isinstance(self.eco[moving_ind], Fish):
                    if isinstance(self.eco[new_ind], Fish):
                        pass
                    elif isinstance(self.eco[new_ind], Bear):
                        self.eco[moving_ind] = None
                    else:
                        self.eco[new_ind] = Fish(new_ind)
                else:
                    raise ValueError("Unknown Creature")
            if verbose:
                self.display()

    def display(self):
        print("===================")
        print("Ecosystem status:\n")
        print(self.eco, "\n")
        print("===================")


river = River(10)

river.initialize()
river.display()
river.next_time_step(15)


