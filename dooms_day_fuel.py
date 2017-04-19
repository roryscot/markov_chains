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



    for i in range(0,len(m)):
      sum = 0
      count = 0
      print(m[i])
      too_many_results.append(0)
      for j in range(0,len(m[i])):
        sum += m[i][j]
      # print(m[i][i] == sum)
      # print("This is crazy")
      # print([m[i][i],sum])

      if sum == 0 or (m[i][i] == sum) and (i not in terminal):
        terminal.append(i)
      if sum == 0:
        divisions.append(1)
      else:
        divisions.append(sum)

    for i in range(1,len(m)):
      default_terminal = 0
      j = 0
      if i not in terminal:
        if m[i][j] == 0:
          default_terminal += 1
        if default_terminal == len(m):
          terminal.append(i)
      j+=1



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
    idm = identity_matrix(m,q)
    print("IDM")
    print(idm)
    print(q == idm)
    print("q checker")
    print(q_checker(q))
    print(" ")
    if q_checker(q)==0 or q == idm:
      result = matrix_fractionator(m)
      print(len(result))
      print(len(terminal))
      print("FRACTIONATOR")
      print result
      if q == idm:
        return result[len(result)-(len(terminal)+2):]
      else:
        return result[len(result)-(len(terminal)+1):]

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
    #
    # placeholder
    #
    if getMatrixDeternminant(i_q)==0:
      # numerators.append(common_denominator)
      # return (numerators)

      print("HEERRERERERE!!!!!!!!!!!!!!!")


      result = matrix_fractionator(m)
      print("Result = ")
      print(result)


      if q == idm:
        return result[len(result)-(len(terminal)+2):]
      else:
        return result[len(result)-(len(terminal)+1):]



      print("Result = ")
      print(result)

      result.append(1)
      return result[len(result)-(len(terminal)+1):]


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

def q_checker(m):
  sum = 0
  for i in range(len(m)):
    for j in range(len(m)):
      sum += m[i][j]
  return sum



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

    print("identity")
    print(row)
  print("identity[0]")
  identity[0][0]=float(identity[0][0])
  print(identity[0][0])

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

o = [
  [0, 1, 0, 0, 0, 1],
  [0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0]
  ]
testtttt=[
  [0, 0, 1, 2],
  [0, 0, 1, 1],
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  ]#=> [1,2,3]?
testtttt2=[
  [0, 0, 1, 2],
  [0, 0, 1, 1],
  [0, 0, 1, 1],
  [0, 0, 0, 0],
  ]#=> [1,1]?
testtttt3=[
  [0, 0, 1, 2, 0],
  [0, 0, 1, 1, 0],
  [0, 0, 1, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  ]#=> [1,1]?
testtttt4=[
  [0, 0, 1, 2, 0],
  [0, 0, 1, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  ]#=> [1,2,0,3]?
testtttt5=[
  [0, 0, 1, 2],
  [0, 0, 1, 3],
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  ]#=> [0,1,2,3]?
testtttt6=[
  [0, 0, 0, 0, 0, 4, 3, 2, 1],
  [0, 0, 0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 5, 2, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 0, 1, 0, 0, 0],
  [0, 1, 0, 0, 0, 4, 0, 7, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  #[0, 0, 0, 0, 0, 0, 0, 0, 0],
  ]

testtttt7=[
  [1,0],[0,0]
  ]

testtttt8 =  [
  [5,0],[0,0]
  ]

testtttt9=[
  [0, 1, 2],
  [4, 3, 2],
  [0, 0, 0],
]

testtttt10=[
[0,0,5],
[0,0,1],
[0,0,5]
]

testtttt11=[
[0,0,5],
[0,0,0],
[0,0,5]
]

testtttt12=[
[0,0,5],
[0,0,0],
[0,0,0]
]

mikes=[
[0,0,0,0,3,2],
[0,0,0,0,0,2],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,7,0,3],
[0,0,0,0,0,8]
]#=> [0,0,0,1,1]



print(answer(m))
#print(answer(n))
#print(answer(o))
#print(answer(testtttt4))
#print(answer(testtttt10))
#print(answer(mikes))

#example = [[1,0,2,3],[0,1,1,1],[0,0,0,0],[0,0,0,0]]

#print(getMatrixDeternminant(this_thing))
#print(answer(example))
#print(answer(testtttt6))
