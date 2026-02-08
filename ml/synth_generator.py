import numpy as np
import pandas as pd

np.random.seed(42)
N = 10000

def score():
    return round(np.clip(np.random.normal(6.5, 1.0), 0, 9), 1)

rows = []

for _ in range(N):
    visa_type = np.random.choice(
        ["STUDENT", "WORK", "DEPENDENT"],
        p=[0.5, 0.35, 0.15]
    )

    reading = score()
    listening = score()
    writing = score()
    speaking = score()

    age = np.random.randint(18, 60)
    gap_year = np.random.randint(0, 8)
    marital_status = np.random.choice(
        ["single", "married", "divorced"],
        p=[0.55, 0.4, 0.05]
    )

    avg = (reading + listening + writing + speaking) / 4

    if visa_type == "STUDENT":
        label = int(avg >= 6.0 and gap_year <= 2)
    elif visa_type == "WORK":
        label = int(avg >= 6.5 and age >= 21 and gap_year <= 3)
    else:
        label = int(avg >= 5.5 and marital_status == "married")

    rows.append([
        reading, listening, writing, speaking,
        age, gap_year, marital_status, visa_type, label
    ])

df = pd.DataFrame(rows, columns=[
    "reading_score", "listening_score", "writing_score", "speaking_score",
    "age", "gap_year", "marital_status", "visa_type", "label"
])

df.to_csv("ml/data/synthetic_raw.csv", index=False)
print("Synthetic data generated:", df.shape)
