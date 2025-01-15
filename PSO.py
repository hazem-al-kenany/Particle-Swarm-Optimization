import random
import math

class Agent:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.personal_best = position
        self.personal_best_value = float('inf')

#evaluate how good a position is by returning the distance from the origin point (0,0)
def objective_function(position):
    return math.sqrt((position[0]**2 - 0) + (position[1]**2 - 0))  #What is the name of this theorem?

#initialize 10 agents w/ random positions and velocities
def initialize_agents(num_agents, space_size):
    agents = []
    for _ in range(num_agents):
        position = [random.uniform(-space_size, space_size), random.uniform(-space_size, space_size)] #"uniform" is used to define the range
        velocity = [random.uniform(-1, 1), random.uniform(-1, 1)]
        agents.append(Agent(position, velocity))
    return agents

#update the velocity of each agent
def update_velocity(agent, global_best, c1, c2):
    inertia = []
    for v in agent.velocity:
        inertia.append(0.5 * v) #inertia: maintains 50% of the old velocity

    cognitive = []
    for i in range(len(agent.position)):
        cognitive.append(c1 * (agent.personal_best[i] - agent.position[i])) #cognitive: 25% influence towards personal best (local best)

    social = []
    for i in range(len(agent.position)):
        social.append(c2 * (global_best[i] - agent.position[i])) #social: 25% influence towards global best

    new_velocity = []
    for i in range(len(inertia)):
        velocity = inertia[i] + cognitive[i] + social[i] #new velocity= inertia + cognitive + social
        
        #ensuring velocity stays within the range -1 and 1
        if velocity > 1:
            velocity = 1
        elif velocity < -1:
            velocity = -1
        
        new_velocity.append(velocity)
    
    return new_velocity

def update_position(agent):
    new_position = []
    for i in range(2): #range = 2 to update x and y axis
        new_position.append(agent.position[i] + agent.velocity[i])
    
    agent.position = new_position #move the agent by updating its position

#run 100 simulations
def run_simulation(agents, iterations):
    global_best = agents[0].position
    global_best_value = float('inf')

    for _ in range(iterations):
        for agent in agents:
            value = objective_function(agent.position) #evaluate the objective function (how good a position is)

            #update personal best
            if value < agent.personal_best_value:
                agent.personal_best_value = value
                agent.personal_best = agent.position

            #update global best
            if value < global_best_value:
                global_best_value = value
                global_best = agent.position

        #update velocities and positions of agents
        for agent in agents:
            agent.velocity = update_velocity(agent, global_best, c1, c2)
            update_position(agent)

    return global_best, global_best_value

#print the positions of agents
def print_agent_positions(agents, global_best, title):
    print(title)

    index = 1
    for agent in agents:
        print("Agent " + str(index) + ": " + str(agent.position))
        index += 1

    print("Global Best: " + str(global_best))
    print("-" * 30)

#main
if __name__ == "__main__":
    num_agents = 10
    space_size = 50
    iterations = 100
    c1 = 0.25
    c2 = 0.25

    agents = initialize_agents(num_agents, space_size)

    #print initial positions
    print_agent_positions(agents, agents[0].position, "Initial Positions")

    #run simulation for 100 iterations
    global_best, best_value = run_simulation(agents, iterations)

    #print final positions
    print_agent_positions(agents, global_best, "Final Positions After 100 Iterations")

    #print final positions
    print(f"Best Objective Function Value: {best_value}")