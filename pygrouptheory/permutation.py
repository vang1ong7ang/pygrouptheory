class permutation(dict):
    def __init__(self, data):
        K = set(data.keys())
        V = set(data.values())
        if len(K) != len(V):
            raise 'ERR'
        super().__init__(data)
