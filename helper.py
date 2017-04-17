from fractions import Fraction, gcd

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

  # for i in result:
  #   print(i)

  return result


inverted = [
  [1.2857142857142856, 0.6428571428571428],
[0.5714285714285714, 1.2857142857142856]
]

r = [
  [0, 0, 0, 0.5],
[0, 0.3333333333333333, 0.2222222222222222, 0]
]


# print(len(inverted))
# print(len(r[0]))
# matrix_multiplier(inverted,r)


def matrix_fractionator(m):
  pairs= []
  denominators=[]

  for j in m[0]:
    pairs.append([Fraction(j).limit_denominator().numerator,Fraction(j).limit_denominator().denominator])
    denominators.append(Fraction(j).limit_denominator().denominator)
  greatest_cd=max(denominators)
  print(greatest_cd)
  for i in pairs:
    if
      greatest_cd = gcd(greatest_cd,i[1])
    print(greatest_cd)

  print(pairs)

  return(m)

print(matrix_fractionator(matrix_multiplier(inverted,r)))
