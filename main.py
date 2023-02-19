# -*- coding: utf-8 -*-
"""
Date: Feb 19th 2023
@author: Juan Pablo Brasdefer (juanbrasdefer) Fabian Pawelczyk (fpawelczyk)
"""

from River import River

river = River(5)
river.initialize()
river.display()

river.next_time_step(10)