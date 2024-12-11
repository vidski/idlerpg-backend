class XORShift:
    def __init__(self, seed):
        self.seed = seed & 0xFFFFFFFF  # Ensure the seed is a 32-bit unsigned integer

    def next(self):
        x = self.seed
        print(f"Seed before operations: {x}")
        x ^= (x << 13) & 0xFFFFFFFF
        x ^= (x >> 17) & 0xFFFFFFFF
        x ^= (x << 5) & 0xFFFFFFFF
        self.seed = x & 0xFFFFFFFF
        print(f"Seed after operations: {self.seed}")
        return round(self.seed / 0x100000000, 17)

    def next_int(self, min, max):
        return int(self.next() * (max - min + 1)) + min


class SplitMix64:
    def __init__(self, seed):
        self.state = seed & 0xFFFFFFFFFFFFFFFF  # Ensure the state is 64-bit

    def next(self):
        self.state = (self.state + 0x9E3779B97F4A7C15) & 0xFFFFFFFFFFFFFFFF  # Increment state
        z = self.state
        z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9 & 0xFFFFFFFFFFFFFFFF
        z = (z ^ (z >> 27)) * 0x94D049BB133111EB & 0xFFFFFFFFFFFFFFFF
        z = z ^ (z >> 31)
        return z & 0xFFFFFFFFFFFFFFFF  # Return as 64-bit unsigned integer

    def next_float(self):
        return self.next() / 0xFFFFFFFFFFFFFFFF  # Normalize to [0, 1)

    def next_int(self, min_val, max_val):
        return min_val + int(self.next_float() * (max_val - min_val + 1))