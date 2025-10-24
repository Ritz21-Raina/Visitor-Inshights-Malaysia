poe_counts = poe.groupby(["state", "type"]).size().unstack(fill_value=0).reset_index()
print(poe_counts)