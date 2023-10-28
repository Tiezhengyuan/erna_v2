
from .dna import DNA

class Adapter:
    def __init__(
        self,
        seq: str,
        max_err: float = .1,
        min_overlap: int = 3
    ):
    self.seq = DNA(seq)
    self.max_err = max_err
    self.min_overlap = min_overlap