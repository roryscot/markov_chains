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

      divisions.append(sum)



    fractions = fratctionator(m, divisions)
    #you can reduce the fraction if necessary by iterating through the numbers from sums.min to 1 and if they and the divisions all mod to 0 you can set them all equal to that mod


    print(" ")
    print("divisions: ")
    print(divisions)

    common_denominator = 1
    # if not non_termination:
    if True: #adjust and realign whitespace
      for i in divisions:
        print(i)
        if i != 0:
          common_denominator *= i


    for i in range(0, len(fractions)):
      numerators.append(fractions[i][0]*common_denominator/fractions[i][1])

     #you should actually build a "probability matrix" in which every non-zero number gets stored as a fraction, then you can iterate through and multiply by a common denominator

    print(" ")

    print("terminal: ")
    print(terminal)
    print(" ")

    # print("non_termination: ")
    # print(non_termination)
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

    denominator = common_denominator
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

def probability_matrix(m, divisions, denominator,terminal):
  for i in range(0,len(m)):
    for j in range(0,len(m[i])):
      if m[i][j] != 0:
        m[i][j] = (m[i][j]*denominator)/divisions[i]
    print(m[i])
  return m


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


#print(answer(m))
print(answer(n))
