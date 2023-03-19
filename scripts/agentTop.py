from scripts.agentMiddle import Rob_middle_layer
from scripts.agents import Environment
import matplotlib.pyplot as plt

class Rob_top_layer(Environment):

    def __init__(self, middle, 
                 timeout = 200, 
                 locations = {'mail':(-5,10),
                              'o103':(50,10), 
                              'o109':(100,10),
                              'storage':(101,51)}):
        
        """middle is the middle layer
        18 timeout is the number of steps the middle layer goes before giving
        up locations is a loc:pos dictionary
        where loc is a named location, and pos is an (x,y) position.
        """

        self.middle = middle
        self.timeout = timeout # number of steps before the middle layer should give up
        self.locations = locations

    def do(self,plan):
        """carry out actions.
        actions is of the form {'visit':list_of_locations}
        It visits the locations in turn.
        """
        
        to_do = plan['visit']
        for loc in to_do:
            position = self.locations[loc]
            arrived = self.middle.do({'go_to':position,
                                        'timeout':self.timeout})
  
            self.display(1,"Arrived at",loc,arrived)
            
        
class Plot_env(object):
    
    def __init__(self, body,top):
        """sets up the plot
        """
    
        self.body = body
        plt.ion()
        plt.clf()
        plt.axes().set_aspect('equal')
        for wall in body.env.walls:
            ((x0,y0),(x1,y1)) = wall
            plt.plot([x0,x1],[y0,y1],"-k",linewidth=3)
        
        for loc in top.locations:
            (x,y) = top.locations[loc]
            plt.plot([x],[y],"k<")
            plt.text(x+1.0,y+0.5,loc) # print the label above and to the right
        
        plt.plot([body.rob_x],[body.rob_y],"go")
        plt.draw()


    def plot_run(self):
        """plots the history after the agent has finished.
        This is typically only used if body.plotting==False
        """
    
        xs,ys = zip(*self.body.history)
        plt.plot(xs,ys,"go")

        wxs,wys = zip(*self.body.wall_history)
        plt.plot(wxs,wys,"ro")

        #plt.draw()
        