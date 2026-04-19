from search_agent import SearchAgent
from priority_queue import PriorityQueue
from typing import Callable


class AStarAgent(SearchAgent):

    def __init__(self, env, initial_state, end_state, model, heuristic_func: Callable[[object, object], int]=None):
        super().__init__(env, initial_state, end_state, model)
        self.action_list = []
        self.heuristics = {}
        if heuristic_func is None:
            heuristic_func = lambda state, goal: 0
        self.h = heuristic_func


    def next_action(self):
        #Usar action_list o llamar a a_star para actualizar self.action_list
        raise NotImplementedError

    def a_star(self):
        #Algoritmo de a_star que retorna la lista de acciones para llegar al destino
        raise NotImplementedError

