from pygrouptheory import Permutation

class TestPermutation:
        
    pass




if __name__ == "__main__":
    p1 = Permutation({1:3, 2:2, 3:1})
    p2 = Permutation({1:2, 2:3, 3:1})
    print((p1*p2).to_matrix())
    print(p1.to_cycles())
    print(p2.to_cycles())
    print((p1*p2).to_cycles())
    p3 = Permutation({1:2,2:3,3:4,4:1})
    print(p3.to_cycles())
