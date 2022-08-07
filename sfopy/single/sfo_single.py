'''Sunflower optimization'''

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
        self.dimentions = dimensions
        self.init_pos = init_pos

class SingleSFO(Flora):
    def __init__(
        self,
        n_plants,
        dimensions,
        init_pos,
        options,
        bounds
    ):
        '''Initialize the Flora
        
        Attributes
        ----------
        n_plants: int
            number of plants of the flora.
        dimensions: int
            number of dimensions of the problem.
        init_pos: np.ndarray, optional
            explicitly set the initial position of the plants.
            Set None to generate it randomly.
        options: dict with keys {'p', 'm', 's'}
            a dictionary containing the SFO parameters
                * p: float
                    pollination rate
                * m: float
                    mortality rate
                * s: float
                    survival rate
        bounds: tuple of np.ndarray
            a tuple of size 2 where the first entry is the minimum bound
            and the second is the maximum bound. Each array mus be the 
            size of (dimensions)
        
        '''

        try:
            assert len(bounds[0]) == dimensions and len(bounds[1]) == dimensions
        except AssertionError:
            raise AssertionError(
                "each bound must be a np.ndarray of size equal to (dimensions)"
            )

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
