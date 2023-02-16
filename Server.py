from mesa.visualization.modules import CanvasGrid,ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import Slider
from Model import VoterModel

NUMBER_OF_CELLS = 40

SIZE_OF_CANVAS_IN_PIXELS_X = 400
SIZE_OF_CANVAS_IN_PIXELS_Y = 400

simulation_params = {
    "proportion":Slider(
    "Number of Agents",
    0.5, #default
    0, #min
    1, #max
    0.05, #step
    description="Choose how many agents initially have State A"
    ),

    "width": NUMBER_OF_CELLS,
    "height": NUMBER_OF_CELLS,
}


def agent_portrayal(agent):
    portrayal={"Shape":"circle","Filled":"true","r":0.8}

    if agent.state == 0:
        portrayal["Color"]="orange"
        portrayal["Layer"]=0
    else:
        portrayal["Color"]="black"
        portrayal["Layer"]=1
    return portrayal

grid=CanvasGrid(agent_portrayal,NUMBER_OF_CELLS,NUMBER_OF_CELLS,SIZE_OF_CANVAS_IN_PIXELS_X,SIZE_OF_CANVAS_IN_PIXELS_Y)

chart_currents = ChartModule(
    [
        {"Label": "State A","Color":"orange"},
        {"Label": "State B","Color":"black"},
    ],
    canvas_height=300,
    data_collector_name="datacollector_currents"
)

server = ModularServer(
    VoterModel,
    [grid,chart_currents],
    "Voter Model",
    simulation_params
)
server.port = 8521
server.launch()