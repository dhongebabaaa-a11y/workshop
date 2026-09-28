import pandas as pd
data={
    "name" : [ "ram_vai", "hari", "syaam"],
    "score" : [10,20,30]
    }
df=pd.DataFrame(data)
top_score=df["score"].max()
print(f" top score is : {top_score}")
df["passed"]=df["score"]>= 50
num_passed=df["passed"].sum()
print(f"Passed: {num_passed}")
