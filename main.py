# -*- coding: utf-8 -*-
"""
@author: Fabian Pawelczyk
"""

from River import River

river = River(5)
river.initialize()
river.display()

river.next_time_step(10)