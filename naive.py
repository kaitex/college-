from collections import Counter

# Dataset
data = [
    ("Red", "Sports", "Domestic", "Yes"),
    ("Red", "Sports", "Domestic", "No"),
    ("Red", "Sports", "Domestic", "Yes"),
    ("Yellow", "Sports", "Domestic", "No"),
    ("Yellow", "Sports", "Imported", "Yes"),
    ("Yellow", "SUV", "Imported", "No"),
    ("Yellow", "SUV", "Imported", "Yes"),
    ("Yellow", "SUV", "Domestic", "No"),
    ("Red", "SUV", "Imported", "No"),
    ("Red", "Sports", "Imported", "Yes"),
]

# Separate Yes and No examples
yes_data = [d for d in data if d[3] == "Yes"]
no_data = [d for d in data if d[3] == "No"]

# Priors
p_yes = len(yes_data) / len(data)
p_no = len(no_data) / len(data)

# Conditional probability function
def conditional_prob(feature_index, feature_value, subset):
    count = sum(1 for row in subset if row[feature_index] == feature_value)
    return count / len(subset)

# Features for Red SUV Domestic
features = [("Red", 0), ("SUV", 1), ("Domestic", 2)]

# Calculate P(features|Yes) * P(Yes)
p_yes_given_features = p_yes
for value, idx in features:
    p_yes_given_features *= conditional_prob(idx, value, yes_data)

# Calculate P(features|No) * P(No)
p_no_given_features = p_no
for value, idx in features:
    p_no_given_features *= conditional_prob(idx, value, no_data)

# Results
print("P(Yes|features) ∝", p_yes_given_features)
print("P(No|features) ∝", p_no_given_features)

# Decision
if p_yes_given_features > p_no_given_features:
    print("Prediction: YES (stolen)")
else:
    print("Prediction: NO (not stolen)")

