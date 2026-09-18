class FuzzySet:

    def __init__(self, A, B, nameA="A", nameB="B"):
        self.A = A
        self.B = B
        self.nameA = nameA
        self.nameB = nameB

    def union(self):
        return {k: max(self.A[k], self.B[k]) for k in self.A}

    def intersection(self):
        return {k: min(self.A[k], self.B[k]) for k in self.A}

    def complement(self, set_name="A"):
        S = self.A if set_name == "A" else self.B
        return {k: 1 - S[k] for k in S}

    def difference(self):
        return {
            k: round(min(self.A[k], 1 - self.B[k]), 2)
            for k in self.A
        }


A = {"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6}
B = {"a": 0.9, "b": 0.9, "c": 0.4, "d": 0.5}

fs = FuzzySet(A, B)

print("Union:", fs.union())
print("Intersection:", fs.intersection())
print("Complement of A:", fs.complement("A"))
print("Difference A - B:", fs.difference())