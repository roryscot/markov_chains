from fractions import Fraction

def answer(m):
  result = []

  terminals = terminal_finder(m)
  divisions = divisions_of(m)
  working_order = reorder
  fractions = fratctionator(m, divisions)

  #print(terminals)
  #print(divisions)
  #print(working_order(m,terminals))
  #print(fractions)



  return result





 #======Initial Info ===================

def terminal_finder(m):
  terminal = []
  divisions = []

  for i in range(0,len(m)):
    sum = 0
    for j in range(0,len(m[i])):
      sum += m[i][j]
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

  return terminal

          #------

def divisions_of(m):
  divisions = []

  for i in range(0,len(m)):
    sum = 0
    for j in range(0,len(m[i])):
      sum += m[i][j]
    if sum == 0:
      divisions.append(1)
    else:
      divisions.append(sum)
  return divisions

def reorder(m,terminal):
  reordered = []
  for i in range(len(m)):
    if i not in terminal:
      reordered.append([i,m[i]])
  for i in range(len(m)):
    if i in terminal:
      reordered.append([i,m[i]])

  return reordered

        #------

def fratctionator(m, divisions):
  fractions = []
  for i in range(0,len(m)):
    for j in range(0,len(m[i])):
      if m[i][j] != 0:
        fractions.append([m[i][j],divisions[i]])
  return fractions

#======Probability Matrix===================
      #This should examine the reordered matrix so that it give a standard form

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

#============Matrix Quadrants =================

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


      #------


def r_finder(m,terminal):
  r = []
  t = len(m)-len(terminal)
  for i in range(0,t):
    row = []
    for j in range(t,len(m)):
      row.append(m[i][j])
    r.append(row)
  return r

#==========Matrix Inversion======================
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

    #------


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


    #------


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



#------============================================--------------
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
