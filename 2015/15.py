with open("15.txt") as fh:
    content = fh.read().split("\n")


def score(ingredients,amounts,scores,n=4):
    # n is the number of ratings: flavor, texture etc.
    result = 1
    
    for i in range(n):
        s = 0
        for j in range(len(ingredients)):
            s += amounts[j] * scores[ingredients[j]][i]
        result *= max(s,0)

    return result

def cals(ingredients,amounts,scores,n=4):
    result = 0
    for j in range(len(ingredients)):
        result += amounts[j] * scores[ingredients[j]][n]
    return result


scores = {}
ingredients = []
for x in content:
    x = x.replace(":","").replace(",","").split()
    ingredient = x[0]
    capacity = int(x[2])
    durability = int(x[4])
    flavor = int(x[6])
    texture = int(x[8])
    calories = int(x[10])
    scores[ingredient] = capacity,durability,flavor,texture,calories
    ingredients.append(ingredient)


alldivisions = []
teaspoons = 100
for i in range(0, teaspoons + 1):
    for j in range(0,teaspoons + 1 - i):
        for k in range(0, teaspoons + 1 - j - i):
            l = teaspoons - (i+j+k)
            alldivisions.append((i,j,k,l))

Total_scores = []
Total_scores2 = []
for amounts in alldivisions:
    s = score(ingredients,amounts,scores)
    Total_scores.append(s)
    if cals(ingredients,amounts,scores) == 500:
        Total_scores2.append(score(ingredients,amounts,scores))

print("Part 1: ",max(Total_scores))


print("Part 2: ",max(Total_scores2))