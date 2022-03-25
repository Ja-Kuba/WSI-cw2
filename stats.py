from tournament_genom import TournamentGenom


class Stats:
    def __init__(self, populations_list: list, result: TournamentGenom, best_iter_found: int) -> None:
        self.populations_list = populations_list
        self.result = result
        self.best_iter_found = best_iter_found
        
        
    
    