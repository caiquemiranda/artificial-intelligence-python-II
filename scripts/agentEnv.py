import math
from scripts.agents import Environment

class Rob_env(Environment):
    
    def __init__(self,walls = {}):
        """walls is a set of line segments
        where each line segment is of the form ((x0,y0),(x1,y1))
        """
    
        self.walls = walls