import math
import datetime
import pandas as pd

for x in range(0, int(2 * math.pi)):
    print(f"Sin {x} = {math.sin(x)}")

print(datetime.datetime.now())

df = pd.DataFrame(
    {
        "Name": [
            "Smoley, Oleksandr",
            "Salo, Maxim",
            "Polulih, Natalia",
        ],
        "Age": [19, 19, 16],
        "Sex": ["male", "male", "female"],
    }
)

print(df)