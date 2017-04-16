from fractions import Fraction

def answer(m):
    divisions = []
    numerators = []
    result = []
    terminal = []
    too_many_results = []
    # non_termination = []

    for i in range(0,len(m)):
      sum = 0
      count = 0
      print(m[i])
      too_many_results.append(0)
      for j in range(0,len(m[i])):
        # if m[i][j]>0 and m[j][i]>0:
          # if [j,i] not in non_termination:
          #   non_termination.append([i,j])
        sum += m[i][j]
      if sum == 0:
        terminal.append(i)
      if sum == 0:
        divisions.append(1)
      else:
        divisions.append(sum)

    fractions = fratctionator(m, divisions)

    print(" ")
    print("divisions: ")
    print(divisions)

    common_denominator = 1
    # if not non_termination:
    if True: #adjust and realign whitespace
      for i in divisions:
        if i != 0:
          common_denominator *= i


    for i in range(0, len(fractions)):
      numerators.append(fractions[i][0]*common_denominator/fractions[i][1])

    print(" ")

    print("terminal: ")
    print(terminal)
    print(" ")

    print(" ")
    print("divisions: ")
    print(divisions)
    print(" ")

    print("numerators")
    print(numerators)
    print(" ")

    print("common_denominator: ")
    print(common_denominator)
    print(" ")

    print("fractions:")
    print(fractions)
    print("probability_matrix:")
    probability_matrix(m,divisions,common_denominator,terminal)
    print(" ")

    #I'm going to have to draw from "too_many_results" at the end in order to refer to each terminating state by it's position. Then can append them to result, which will omit the transitional values from "result".

    for i in range(0, len(too_many_results)):
      if i in terminal:
        result.append(too_many_results[i])

    denominator = common_denominator#I can use reducer to find a common denominator
    result.append(denominator)
    print("Result: ")

    return result


def fratctionator(m, divisions):
  fractions = []
  for i in range(0,len(m)):
    for j in range(0,len(m[i])):
      if m[i][j] != 0:
        fractions.append([m[i][j],divisions[i]])
      # else:
      #   fractions.append([0,1])
  return fractions

       #you should actually build a "probability matrix" in which every non-zero number gets stored as a fraction, then you can iterate through and multiply by a common denominator
def probability_matrix(m, divisions, denominator,terminal):
  for i in range(0,len(m)):
    for j in range(0,len(m[i])):
      if m[i][j] != 0:
        m[i][j] = (m[i][j]*denominator)/divisions[i]
      if (m[i][j] == m[i][i]):
        if i in terminal:
          m[i][i]=denominator

    print(m[i])
  return m

def reducer(num_array):

  min(num_array)
  for i in range(min(num_array), 1):
    print("you can reduce the fraction if necessary by iterating through the numbers from sums.min to 1 and if they and the divisions all mod to 0 you can set them all equal to that mod ")





m = [
  [0, 2, 1, 0, 0],
  [0, 0, 0, 3, 4],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0]
  ]
n = [
  [0, 1, 0, 0, 0, 1],
  [4, 0, 0, 3, 2, 0],
  [0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0]
  ]
q = [
  [0, 1.0/2],
  [ (4.0/9),0],
  ]

# q = [
#   [0, 9],
#   [ 8 ,0],
#   ]


def identity_matrix(m):
  identity = []
  for i in range(0,len(m)):
    row = []
    for j in range(0,len(m)):
      if (i == j ):
        row.append(1)
      else:
        row.append(0)
    identity.append(row)
    print(row)
  return identity

def matrix_subtraction(identity,m):
  result = []
  for i in range(0,len(m)):
    row = []
    for j in range(0,len(m)):
      print(m[i][j])
      row.append(identity[i][j]-m[i][j])
    result.append(row)
    print(row)
  return result




#print(answer(m))
#print(answer(n))


def transposeMatrix(m):
    t = []
    for r in range(len(m)):
        tRow = []
        for c in range(len(m[r])):
            if c == r:
                tRow.append(m[r][c])
            else:
                tRow.append(m[c][r])
        t.append(tRow)
        print(tRow)
    return t

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    print("determinant")
    print(Fraction(determinant))
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

# def fraction_converter(m):
#   new_m = []
#   for i in range(0,len(m)):
#     for j in range(0,len(m)):
#       new_m.append(Fraction(m[i][j]))
#   return new_m

print(matrix_subtraction(identity_matrix(q),q))
sample = getMatrixInverse(matrix_subtraction(identity_matrix(q),q))
print(sample)
print(" ")
# print(fraction_converter(sample))
