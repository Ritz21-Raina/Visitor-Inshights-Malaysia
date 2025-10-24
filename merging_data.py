import pandas as pd

soe = pd.read_csv("Dataset1.csv")
poe = pd.read_csv('poe.csv')
pd.set_option('display.max_columns', None)
pd.set_option("display.width", 200)

poe =poe[poe['state']!= "Singapore"]

# Clean state names in poe to match soe
poe["state"] = poe["state"].str.replace("_", " ")

# seeing how many point of entry does each state have
# Group POE data by state and type, then count
poe_counts = poe.groupby(["state", "type"]).size().unstack(fill_value=0).reset_index()
print(poe_counts)

soe_with_poe = soe.merge(poe_counts, left_on="soe", right_on="state", how="left")
soe_with_poe = soe_with_poe.drop(columns=["state"])

print(soe_with_poe.head())

# Save to a new CSV file
soe_with_poe.to_csv("data_file.csv", index=False)