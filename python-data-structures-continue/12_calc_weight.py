# Write a function that returns the weighted average of all integers tuple (<score>, <weight>)

#!/usr/bin/python3
def calc_weight(list_=[]):
    if not list_:
       return 0

    weighted_average = sum(score * weight for score, weight in list_)
    weight = sum(weight for _, weight in list_)

    return weighted_average / weight if weight !=0 else 0
   
if __name__=="__main__":
    list_ = [(3, 2), (5, 9), (7, 7)]
    # = ((3 * 2) + (5 * 9) + (7 * 7)) / (2 + 9 + 7)
    result = calc_weight(list_)
    print(f"Weight: {result:0.2f}")

