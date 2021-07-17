# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 10:58:59 2020

@author: gkhayes

URL: https://gist.github.com/gkhayes/3d154e0505e31d6367be22ed3da2e955#file-mountain_car-py
"""

import numpy as np
import gym
import matplotlib.pyplot as plt

# Importar e inicializar el ambiente Mountain Car
env = gym.make('MountainCar-v0')
env.reset()

# Defininir funcion de aprendizaje Q
def QLearning(env, learning, discount, epsilon, min_eps, episodes):
    # Determinar tamano del espacio de estados discretizado
    num_states = (env.observation_space.high - env.observation_space.low)*\
                    np.array([10, 100])
    num_states = np.round(num_states, 0).astype(int) + 1
    
    # Inicializar tabla Q
    Q = np.random.uniform(low = -1, high = 1, 
                          size = (num_states[0], num_states[1], 
                                  env.action_space.n))
    
    # Inicializar variables para rastrear recompensas
    reward_list = []
    ave_reward_list = []
    
    # Calcular reduccion episodica en epsilon
    reduction = (epsilon - min_eps)/episodes
    
    # Run Q learning algorithm
    for i in range(episodes):
        # Inicializar parametros
        done = False
        tot_reward, reward = 0,0
        state = env.reset()
        
        # Discretizar estado
        state_adj = (state - env.observation_space.low)*np.array([10, 100])
        state_adj = np.round(state_adj, 0).astype(int)
    
        while done != True:   
            # Renderizar ambiente para los ultimos cinco episodios
            if i >= (episodes - 20):
                env.render()
                
            # Determinar siguiente accion mediante estrategia avariciosa epsilon
            if np.random.random() < 1 - epsilon:
                action = np.argmax(Q[state_adj[0], state_adj[1]]) 
            else:
                action = np.random.randint(0, env.action_space.n)
                
            # Obtener siguiente estado y recompensa
            state2, reward, done, info = env.step(action) 
            
            # Discretizar state2
            state2_adj = (state2 - env.observation_space.low)*np.array([10, 100])
            state2_adj = np.round(state2_adj, 0).astype(int)
            
            #Permitir estados terminales
            if done and state2[0] >= 0.5:
                Q[state_adj[0], state_adj[1], action] = reward
                
            # Ajustar valor Q para estado actual
            else:
                delta = learning*(reward + 
                                 discount*np.max(Q[state2_adj[0], 
                                                   state2_adj[1]]) - 
                                 Q[state_adj[0], state_adj[1],action])
                Q[state_adj[0], state_adj[1],action] += delta
                                     
            # Actualizar variables
            tot_reward += reward
            state_adj = state2_adj
        
        # Decay epsilon
        if epsilon > min_eps:
            epsilon -= reduction
        
        # Rastrear recompensas
        reward_list.append(tot_reward)
        
        if (i+1) % 100 == 0:
            ave_reward = np.mean(reward_list)
            ave_reward_list.append(ave_reward)
            reward_list = []
            
        if (i+1) % 100 == 0:    
            print('Episode {} Average Reward: {}'.format(i+1, ave_reward))
            
    env.close()
    
    return ave_reward_list

# Correr algoritmo de aprendizaje-Q
rewards = QLearning(env, 0.2, 0.9, 0.8, 0, 5000)

# Graficar recompensas
plt.plot(100*(np.arange(len(rewards)) + 1), rewards)
plt.xlabel('Episodios')
plt.ylabel('Recompensa promedio')
plt.title('Recompensa promedio vs Episodios')
plt.savefig('recompensas.jpg')     
plt.close()  