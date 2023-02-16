from mesa import Model
from Agent import VoterAgent
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
import random
class VoterModel(Model):

    def __init__(self,proportion,width,height):
        self.proportion = proportion #proportion of agents that initially have State B
        self.grid = MultiGrid(width,height,True) #True here, means periodic boundary conditions
        self.schedule = RandomActivation(self) #RandomActivation means iterate the model rules over all agents in random order every step

        self.datacollector_currents=DataCollector(
            {
                "State A": VoterModel.current_a_agents,
                "State B": VoterModel.current_b_agents,
            }
        )

        for cell in self.grid.coord_iter():
            x = cell[1]
            y = cell[2]
            if random.random() < self.proportion:
                agent_state = 1
            else:
                agent_state = 0

            agent = VoterAgent(self, agent_state)
            self.grid.place_agent(agent, (x, y))
            self.schedule.add(agent)
        
        self.running = True


    def step(self) :
        self.schedule.step()
        self.datacollector_currents.collect(self)
        #We want to stop the simulation if consensus is reached
        if (sum([1 for agent in self.schedule.agents if agent.state == 0]) == self.schedule.get_agent_count()):
            self.running = False
        elif (sum([1 for agent in self.schedule.agents if agent.state == 0]) == 0):
            self.running = False

    @staticmethod
    def current_a_agents(model) -> int:
        #Return the total number of agents with state A
        return sum([1 for agent in model.schedule.agents if agent.state == 0])

    @staticmethod
    def current_b_agents(model) -> int:
        #Return the total number of agents with state B
        return sum([1 for agent in model.schedule.agents if agent.state == 1])
    