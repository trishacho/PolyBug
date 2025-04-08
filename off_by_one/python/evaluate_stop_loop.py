class Dummy:
    def __init__(self, data, index):
        self.ctx = {f"{id(self)}_index": index, f"{id(self)}_data": data}
        self._id = id(self)

    def evaluate_stop_loop_bug(self):
        current_index = self.ctx.get(f"{self._id}_index", 0)
        data_length = len(self.ctx.get(f"{self._id}_data", []))
        return current_index > data_length

    def evaluate_stop_loop_fixed(self):
        current_index = self.ctx.get(f"{self._id}_index", 0)
        data_length = len(self.ctx.get(f"{self._id}_data", []))
        return current_index >= data_length