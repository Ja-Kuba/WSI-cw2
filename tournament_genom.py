import numpy as np


class TournamentGenom:
    def __init__(self, genom, rand_obj = np.random) -> None:
        self.genom:np.array = genom
        self.uncover_cnt = None
        self.positive_cnt = None
        self.rand = rand_obj

    @classmethod
    def copy_init(cls, other) -> None:
        tmp = cls(other.getGenom(), rand_obj=other.rand)
        tmp.uncover_cnt = other.uncover_cnt
        tmp.positive_cnt = other.positive_cnt

        return tmp


    def __str__(self) -> str:
        return f"{self.genom}, un: {self.uncover_cnt}, pc: {self.positive_cnt}"

    def getGenom(self):
        return self.genom

    def mutate(self, force:int = 1, p:float =.3):
        if self.rand.choice([0, 1], size=1, p=[1-p, p]):
            mutate_vector = np.zeros(len(self.genom))
            mutate_vector[:force] = 1
            np.random.shuffle(mutate_vector)
            self.genom = np.abs(self.genom - mutate_vector)


    def fitProblem(self, problem):
        self.uncover_cnt = self.count_uncover(problem)
        self.positive_cnt = self.count_positives()


    def validScores(self):
        if self.uncover_cnt is None or self.positive_cnt is None:
            raise Exception("TournamentGenom not fitted")


    # "<" operator
    # if equal returns False
    def __lt__(self, other): 
        self.validScores()
        other.validScores()
        un_s = self.score_fun(self.uncover_cnt, other.uncover_cnt)
        pos_s = self.score_fun(self.positive_cnt, other.positive_cnt)

        #if un_s > 0: return False
        #elif un_s < 0: return True
        #else:
        #    if pos_s > 0: return False
        #    elif pos_s < 0: return True
        #    else: return False

    # ">" operator
    # if equal returns True
    def __gt__(self, other): 
        return not self.__lt__(other)


    def score_fun(self, s1:int, s2:int)->int:
        comp = s1 - s2
        if comp < 0: return 1
        elif comp > 0: return -1
        else: return 0

    def count_uncover(self, problem):
        p = problem.copy()
        for i, x in enumerate(self.getGenom()):
            if x == 1:
                p[:, i] = 0
                p[i, :] = 0

        return int(np.sum(p))


    def count_positives(self):
        return int(self.genom.sum())