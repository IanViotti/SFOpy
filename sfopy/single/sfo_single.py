'''Sunflower optimization'''

from mimetypes import init
import numpy as np

class Flora():
    def __init__(
        self,
        n_plants,
        dimensions,
        init_pos = None,
    ):
        '''Creates a base class for flora
        
        Creates a Flora class from the given inputs

        Attributes
        ----------
        n_plants: int
            number of plants of the flora.
        dimensions: int
            number of dimensions of the problem.
        init_pos: np.ndarray, optional
            explicitly set the initial position of the plants.
            Set None to generate it randomly.

        '''

        try:
            assert n_plants > 0 and isinstance(n_plants, int)
        except AssertionError:
            raise AssertionError(
                "n_plants expects an integer value greater than 0"
            )
        
        try:
            assert dimensions > 0 and isinstance(dimensions, int)
        except AssertionError:
            raise AssertionError(
                "dimensions expects an integer value greater than 0"
            )

        self.n_plants = n_plants
        self.dimensions = dimensions
        self.init_pos = init_pos

class SingleSFO(Flora):
    def __init__(
        self,
        n_plants,
        dimensions,
        options,
        bounds,
        init_pos = None,
    ):
        '''Initializes the Sunflower optimizer
        
        Attributes
        ----------
        n_plants: int
            number of plants of the flora.
        dimensions: int
            number of dimensions of the problem.
        init_pos: np.ndarray, optional
            explicitly set the initial position of the plants.
            Set None to generate it randomly (default = None).
        options: dict with keys {'p', 'm', 's'}
            a dictionary containing the SFO parameters
                * p: float
                    pollination rate
                * m: float
                    mortality rate
                * s: float
                    survival rate
        bounds: tuple of np.ndarray
            a tuple of size equal to dimensions where each entry is an array with the minimum bound
            maximum bound of each dimensions. The tuble must be size (dimension)
        
        '''

        try:
            assert len(bounds) == dimensions 
        except AssertionError:
            raise AssertionError(
                "each bound must be a np.ndarray of size equal to (dimensions)"
            )

        self.n_plants = n_plants
        self.dimensions = dimensions
        self.init_pos = init_pos
        self.options = options
        self.bounds = bounds

    def initial_flora(
        self,
        obj_fun,
        method = 'random'
    ):
        '''
        Initializes the first population of plants 

        Atributes
        ---------
        method: string
            method for generating the initial population (default = random).

        Returns
        -------
        plants: np.ndarray
            an array with size (n_plants, dimensions) containing the position for each plant
        fitness:
            an array with size (n_plants) containing the fitness for each plant
        '''

        # Set the initial position of the plants 
        if self.init_pos == None:
            if method == 'random':
                plants_ones = np.ones((self.n_plants, self.dimensions))
                for p in range(self.n_plants):
                        plants_ones[p, :] *= self.bounds.T[0] + (self.bounds.T[1] - self.bounds.T[0]) * np.random.rand(self.dimensions) 

                plants = plants_ones
        
        else:
            plants = self.init_pos

        return plants

    def evaluate_flora(
        self,
        plants,
    ):
        '''
        Evaluates the flora fitness, pollination, step and mortality

        Atributes
        ---------
            a
        Returns
        -------

        
        '''


    def optimize(
        self,
        objective_func,
        iters,
    ):
        '''Optimize the objective function for a number of iterations using SFO

        Atributes
        ---------
        objective_func: callable
            objective function to be evaluated
        iters: int
            number of iterations
        
        Returns
        -------
        tuple
            a tuple containing the local best cost and local best position 
            among the flora.
        '''



        return None
