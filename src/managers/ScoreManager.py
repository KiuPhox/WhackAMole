class ScoreManager:
    hit: int = 0
    miss: int = 0

    def getRate(self) -> float:
        return round(ScoreManager.hit / (ScoreManager.hit + ScoreManager.miss), 2)
