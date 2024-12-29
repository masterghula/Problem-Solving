import matplotlib.pyplot as plt
expenses=["rent", "transport", "food", "clothing", "socializing", "misc"]
amount=[1000, 300, 400, 150, 200, 100]

fig, ax = plt.subplots()
ax.pie(amount, labels=expenses, autopct='%1.1f%%', startangle=90, explode=(0.05,0.05,0.05,0.05,0.05,0.05), shadow=True)
plt.show