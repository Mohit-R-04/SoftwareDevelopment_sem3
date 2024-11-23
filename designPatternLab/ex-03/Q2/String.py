
class String:
    def __init__(self, value):
        self.value = value

    def string_distance(self, other):
        if len(self.value) < len(other.value):
            return String.string_distance(other, self)

        if len(other.value) == 0:
            return len(self.value)

        min_length = min(len(self.value), len(other.value))
        diff_count = sum(1 for i in range(min_length) if self.value[i] != other.value[i])
        length_diff = abs(len(self.value) - len(other.value))
        return diff_count + length_diff
