A = {'a','c','e','f'}
B = {'a','b','c','d'}
print(f"A = {A}")
print(f"B = {B}")

C_1 = A.symmetric_difference(B)
print(f"A、B的对称差：C.symmetric_difference(B) = {C_1}")

C_2 = (A | B) - (A & B)
print(f"A、B的并集减去A、B的交集：(A | B) - (A & B) = {C_2}")

if C_1 == C_2:
    print("A、B的并集减去A、B的交集等于A、B的对称差")
else:
    print("A、B的并集减去A、B的交集不等于A、B的对称差")