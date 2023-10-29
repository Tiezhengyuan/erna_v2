'''
trim adapter, index, or polyA
'''
from .sequence import Sequence
from pipelines.match.shift import Shift
from pipelines.match.distance import Distance

class TrimSeq:
    def __init__(
        self,
        adapter:str,
        min_match:int=None,
        trim_end:str=None,
        max_err:int = None,
    ):
        self.adapter = adapter
        self.max_len = len(self.adapter)
        self.min_match = 12 if min_match is None else min_match
        self.trim_end = trim_end if trim_end is not None else '3end'
        self.max_err = max_err if (max_err is not None and \
            max_err < 3) else 0
        #
        seed_adapter = self.adapter[-self.min_match] if self.trim_end \
            == '5end' else self.adapter[0:self.min_match]
        self.seed_pattern = Shift(seed_adapter)
        self.distance = Distance(self.adapter)

    def trim_3end(self, read_seq:str):
        match = self.seed_pattern.shift_and(read_seq, True)
        if match:
            pos = match[0]
            read_3end = read_seq[pos:pos+self.max_len]
            dist_score = self.distance.match_5end(read_3end)
            if dist_score >= len(read_3end) - self.max_err:
                return read_seq[0:pos]
        return read_seq
        
    


