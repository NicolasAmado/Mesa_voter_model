from mesa import Agent

class VoterAgent(Agent):

    def __init__(self, model, state):
        super().__init__(self,model)
        self.state=state

    def step(self) -> None:
        self.voter_model_step()

    def voter_model_step(self):
        #Pick a random neighbor and copy it's state.
        neighbors = self.model.grid.get_neighbors(self.pos,moore=False) #False here means no diagonal neighbors
        
        other = self.random.choice(neighbors)
        copied_state = other.state
            
        self.state = copied_state
