# Takes in input
# Calculate the transitional probabilities using MLE
# !! handle the special cases

# READING OF DATA
import sys
sys.stdout.reconfigure(encoding='utf-8')
with open("./Data/ES/train", "r", encoding="utf-8") as f:
    data = f.read()

# CALCULATE: TRANSITION PARAMETER 
## q(yi|yi−1) = Count(yi−1, yi) / Count(yi−1)

def transitionParameter(data, yi_1) :

    lines = data.split('\n')
    transition_probabilities = {} 

    ## CALCULATE: Count(yi−1, yi)
    transition_counts = {}
    for i in range(1, len(lines)):
        yi_1, yi = lines[i - 1], lines[i]

        # Updating Counts
        if (yi_1, yi) in transition_counts:
            transition_counts[(yi_1, yi)] += 1
        else:
            transition_counts[(yi_1, yi)] = 1

    ## CALCULATE: Count(yi−1)
    for pair, count in transition_counts.items():
        yi_1, yi = pair
        count_yi_1 = sum(1 for line in lines if line.startswith(yi_1))  # Count(yi−1)

        # CALCULATE: q(yi | yi−1) = Count(yi−1, yi) / Count(yi−1)
        transition_probabilities[pair] = count / count_yi_1

    return transition_probabilities

transition_params = transitionParameter(data, 'O')
print(transition_params)






       


    



