from fractions import Fraction

#retry with integer probability matrix
#try to maintain fractions throughout
      #.limit_denominator
#try reverting back to using denominator but with identity_matrix

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
    print(determinant)
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


def answer(m):
    divisions = []
    numerators = []
    result = []
    terminal = []
    too_many_results = []

    if len(m) == 1:
      return [1]

    for i in range(0,len(m)):
      sum = 0
      count = 0
      print(m[i])
      too_many_results.append(0)
      for j in range(0,len(m[i])):
        sum += m[i][j]
      if sum == 0:
        terminal.append(i)
      if sum == 0:
        divisions.append(1)
      else:
        divisions.append(sum)

    fractions = fratctionator(m, divisions)

    common_denominator = 1
    for i in divisions:
      if i != 0:
          common_denominator *= i


    for i in range(0, len(fractions)):
      numerators.append(fractions[i][0]*common_denominator/fractions[i][1])

    print(" ")

    print("terminal: ")
    print(terminal)
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
    print(" ")

    print("probability_matrix:")
    probs = probability_matrix(m,divisions,common_denominator,terminal)
    print(" ")

    print("q = ")
    q = q_finder(probs, terminal)

    print(" ")
    print("r = ")
    r = r_finder(probs, terminal)
    for row in r:
      print(row)


    print(" ")
    i_q = matrix_subtraction(identity_matrix(m,q), q)
    print("I-Q")
    for i in i_q:
      print(i)

    inverse = getMatrixInverse(i_q)
    print(" ")
    print("I - Q inverted")
    for i in inverse:
      print(i)

    print(" ")
    print("(I - Q)^-1 (R): ")
    #order matters in matrix_multiplier
    answer_matrix = matrix_multiplier(inverse,r)

    result = matrix_fractionator(matrix_multiplier(inverse,r))

    print(" ")
    print("Result: ")
    return result

def q_finder(m, terminal):
  q = []
  t = len(m)-len(terminal)
  for i in range(0,t):
    row = []
    for j in range(0,t):
      row.append(m[i][j])
    q.append(row)
    print(row)
  return q

def r_finder(m,terminal):
  r = []
  t = len(m)-len(terminal)
  for i in range(0,t):
    row = []
    for j in range(t,len(m)):
      row.append(m[i][j])
    r.append(row)
  return r


def fratctionator(m, divisions):
  fractions = []
  for i in range(0,len(m)):
    for j in range(0,len(m[i])):
      if m[i][j] != 0:
        fractions.append([m[i][j],divisions[i]])
  return fractions

def probability_matrix(m, divisions, denominator,terminal):
  for i in range(0,len(m)):
    for j in range(0,len(m[i])):
      if m[i][j] != 0:
        m[i][j] = (m[i][j])/float(divisions[i])
      if (m[i][j] == m[i][i]):
        if i in terminal:
          m[i][i]=1

    print(m[i])
  return m

def identity_matrix(m,q):
  identity = []
  for i in range(0,len(q)):
    row = []
    for j in range(0,len(q)):
      if (i == j ):
        row.append(1)
      else:
        row.append(0)
    identity.append(row)
    #print(row)
  return identity

def matrix_subtraction(identity,m):
  result = []
  for i in range(0,len(m)):
    row = []
    for j in range(0,len(m)):
      #print(m[i][j])
      row.append(identity[i][j]-m[i][j])
    result.append(row)
    #print(row)
  return result


def matrix_multiplier(a,b):
  result = []
  for i in range(0,len(a)):
    row = []
    for j in range(0, len(b[0])):
      row.append(0)
    result.append(row)

  for i in range(len(a)):
   for j in range(len(b[0])):
       for k in range(len(b)):
           result[i][j] += a[i][k] * b[k][j]

  for i in result:
    print(i)

  return result

def matrix_fractionator(m):
  pairs= []
  denominators=[]
  result=[]

  for j in m[0]:
    pairs.append([Fraction(j).limit_denominator().numerator,Fraction(j).limit_denominator().denominator])
    denominators.append(Fraction(j).limit_denominator().denominator)
  greatest_cd=max(denominators)

  for i in pairs:
    if greatest_cd%i[1] == 0:
      if greatest_cd!=i[1]:
        i[0]*=(greatest_cd/i[1])
    result.append(i[0])
  result.append(greatest_cd)
  return(result)

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

print(answer(m))
#print(answer(n))
