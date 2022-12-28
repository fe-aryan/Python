def construct_matrices(n):
    A = []
    B = []
    for i in range(n):
        row_a = [(i+j) % n + 1 for j in range(n)]
        row_b = [(i-j+n) % n + 1 for j in range(n)]
        A.append(row_a)
        B.append(row_b)
    return A, B

A, B = construct_matrices(3)
print(A)
print(B)

def find_matrices(n: int) -> bool:
  # Create two empty matrices A and B
  A = [[0 for _ in range(n)] for _ in range(n)]
  B = [[0 for _ in range(n)] for _ in range(n)]

  # Fill in the values for matrix A
  for i in range(n):
    for j in range(n):
      A[i][j] = (i + j) % n + 1

  # Fill in the values for matrix B
  for i in range(n):
    for j in range(n):
      B[i][j] = (i - j + n) % n + 1

  # Create a set to store the pairs in matrix C
  pairs = set()

  # Combine the corresponding elements of A and B to form matrix C
  for i in range(n):
    for j in range(n):
      pairs.add((A[i][j], B[i][j]))

  # Check if the set contains all pairs from {1, 2, ..., n} x {1, 2, ..., n}
  return len(pairs) == n**2

# Test the function
print(find_matrices(3))  # should return True
print(find_matrices(4))  # should return False
