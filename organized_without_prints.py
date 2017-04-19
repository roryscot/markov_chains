from fractions import Fraction

def answer(m):
  if len(m)==1:
    return [1,1]
 #----Initial Info------
  terminals = terminal_finder(m)
  divisions = divisions_of(m)
  common_denominator = common_denominator_finder(divisions)
  fractions = fratctionator(m, divisions)

  mapped_order = mapper(m,terminals)
  reference_order = find_reference_order(mapped_order)

  #New row order
  row_order = reordered_rows(mapped_order)
  #Change columns
  columns_order = column_sorter(m,row_order,reference_order)
  #Move new columns to new rows
  working_order = make_working_order(columns_order,reference_order)
  #Reorder divisions
  reordered_divisions = divisions_reorder(divisions,reference_order)

  #-------Probability Matrix
  probabilities = probability_matrix(working_order, reordered_divisions, common_denominator, terminals)
  #Find Q
  q = q_finder(probabilities,terminals)
  #Set Identity Matrix
  idm = identity_matrix(m,q)
  #Find R
  r = r_finder(probabilities,terminals)
  #Find I-Q
  i_q = matrix_subtraction(idm, q)
  #Get inversion
  inverse = getMatrixInverse(i_q)
  #multiply by R
  resultant_matrix = matrix_multiplier(inverse,r)
  #convert to fractions
  translated_resultant_matrix = matrix_fractionator(resultant_matrix)

  return translated_resultant_matrix






 #======Initial Info ===================

def terminal_finder(m):
  terminal = []

  for i in range(0,len(m)):
    sum = 0
    for j in range(0,len(m[i])):
      sum += m[i][j]
    if sum == 0 or (m[i][i] == sum) and (i not in terminal):
      terminal.append(i)

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

          ##########

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

          ##########

def common_denominator_finder(array):
  common_denominator = 1
  for i in array:
    if i != 0:
        common_denominator *= i
  return common_denominator


          ##########


def mapper(m,terminal):
  mapp = []
  for i in range(len(m)):
    if i not in terminal:
      mapp.append([i,m[i]])
  for i in range(len(m)):
    if i in terminal:
      mapp.append([i,m[i]])

  return mapp

          ##########

def reordered_rows(mapped_order):
  working_order = []
  for i in range(len(mapped_order)):
    working_order.append(mapped_order[i][1])
  return working_order

          ##########

def fratctionator(m, divisions):
  fractions = []
  for i in range(0,len(m)):
    for j in range(0,len(m[i])):
      if m[i][j] != 0:
        fractions.append([m[i][j],divisions[i]])
  return fractions

         ##########

def column_sorter(m,m_prime,order):
  #this depends on the number of terminals being right
  new = []
  for i in range(len(m)):
    row = []
    for j in range(len(m)):
      row.append(m[i][order[j]])
    new.append(row)
  return new

          ##########

def find_reference_order(mapp):
  new = []
  for i in range(len(mapp)):
    new.append(mapp[i][0])
  return new

          ##########

def make_working_order(m,order):
  working_orderer = []
  for i in range(len(order)):
    working_orderer.append(m[order[i]])
  return working_orderer


          ##########

def divisions_reorder(divisions,order):
  new = []
  for i in range(len(order)):
    new.append(divisions[order[i]])
  return new

          ##########




#======Probability Matrix===================
      #This should examine the reordered matrix so that it give a standard form

def probability_matrix(m, divisions, denominator,terminal):
  probs = []
  for i in range(0,len(m)):
    row = []
    for j in range(0,len(m[i])):
      if m[i][j] != 0:
        row.append((m[i][j])/float(divisions[i]))
      # elif (m[i][j] == m[i][i]):
      #   if i in terminal:
          # row.append(1)
      else:
        row.append(0)
    probs.append(row)
  for i in range(len(m)-len(terminal),len(m)):
    for j in range(len(m)):
      if (i == j):
        probs[i][j] = 1
  return probs

#============Matrix Quadrants =================

def q_finder(m, terminal):
  q = []
  t = len(m)-len(terminal)
  for i in range(0,t):
    row = []
    for j in range(0,t):
      row.append(m[i][j])
    q.append(row)
  return q

def q_checker(m):
  sum = 0
  for i in range(len(m)):
    for j in range(len(m)):
      sum += m[i][j]
  return sum


          ##########


def r_finder(m,terminal):
  r = []
  t = len(m)-len(terminal)
  for i in range(0,t):
    row = []
    for j in range(t,len(m)):
      row.append(m[i][j])
    r.append(row)
  return r

          ##########

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
  identity[0][0]=float(identity[0][0])

  return identity


#==========Matrix Interaction======================


def matrix_subtraction(identity,m):
  result = []
  for i in range(0,len(m)):
    row = []
    for j in range(0,len(m)):
      row.append(identity[i][j]-m[i][j])
    result.append(row)
  return result

          ##########


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

  return result

          ##########

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
    return t

          ##########


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


          ##########


def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
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




 #======Initial Info ===================

def terminal_finder(m):
  terminal = []

  for i in range(0,len(m)):
    sum = 0
    for j in range(0,len(m[i])):
      sum += m[i][j]
    if sum == 0 or (m[i][i] == sum) and (i not in terminal):
      terminal.append(i)

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

          ##########

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

          ##########

def common_denominator_finder(array):
  common_denominator = 1
  for i in array:
    if i != 0:
        common_denominator *= i
  return common_denominator


          ##########


def mapper(m,terminal):
  mapp = []
  for i in range(len(m)):
    if i not in terminal:
      mapp.append([i,m[i]])
  for i in range(len(m)):
    if i in terminal:
      mapp.append([i,m[i]])

  return mapp

          ##########

def reordered_rows(mapped_order):
  working_order = []
  for i in range(len(mapped_order)):
    working_order.append(mapped_order[i][1])
  return working_order

          ##########

def fratctionator(m, divisions):
  fractions = []
  for i in range(0,len(m)):
    for j in range(0,len(m[i])):
      if m[i][j] != 0:
        fractions.append([m[i][j],divisions[i]])
  return fractions

         ##########

def column_sorter(m,m_prime,order):
  #this depends on the number of terminals being right
  new = []
  for i in range(len(m)):
    row = []
    for j in range(len(m)):
      row.append(m[i][order[j]])
    new.append(row)
  return new

          ##########

def find_reference_order(mapp):
  new = []
  for i in range(len(mapp)):
    new.append(mapp[i][0])
  return new

          ##########

def make_working_order(m,order):
  working_orderer = []
  for i in range(len(order)):
    working_orderer.append(m[order[i]])
  return working_orderer


          ##########

def divisions_reorder(divisions,order):
  new = []
  for i in range(len(order)):
    new.append(divisions[order[i]])
  return new

          ##########




#======Probability Matrix===================
      #This should examine the reordered matrix so that it give a standard form

def probability_matrix(m, divisions, denominator,terminal):
  probs = []
  for i in range(0,len(m)):
    row = []
    for j in range(0,len(m[i])):
      if m[i][j] != 0:
        row.append((m[i][j])/float(divisions[i]))
      # elif (m[i][j] == m[i][i]):
      #   if i in terminal:
          # row.append(1)
      else:
        row.append(0)
    probs.append(row)
  for i in range(len(m)-len(terminal),len(m)):
    for j in range(len(m)):
      if (i == j):
        probs[i][j] = 1
  return probs

#============Matrix Quadrants =================

def q_finder(m, terminal):
  q = []
  t = len(m)-len(terminal)
  for i in range(0,t):
    row = []
    for j in range(0,t):
      row.append(m[i][j])
    q.append(row)
  return q

def q_checker(m):
  sum = 0
  for i in range(len(m)):
    for j in range(len(m)):
      sum += m[i][j]
  return sum


          ##########


def r_finder(m,terminal):
  r = []
  t = len(m)-len(terminal)
  for i in range(0,t):
    row = []
    for j in range(t,len(m)):
      row.append(m[i][j])
    r.append(row)
  return r

          ##########

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
  identity[0][0]=float(identity[0][0])

  return identity


#==========Matrix Interaction======================


def matrix_subtraction(identity,m):
  result = []
  for i in range(0,len(m)):
    row = []
    for j in range(0,len(m)):
      row.append(identity[i][j]-m[i][j])
    result.append(row)
  return result

          ##########


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

  return result

          ##########

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
    return t

          ##########


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


          ##########


def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
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
