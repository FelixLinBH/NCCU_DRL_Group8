import pickle
import matplotlib.pyplot as plt

fh = open('./portfolio_val/202104202234-train.p', 'rb')
data = pickle.load(fh)
print(data)
fig, ax = plt.subplots(nrows=1, ncols=1)
ax.plot(data)
plt.xlabel("Episode")
plt.ylabel("Total assets")

fig.savefig('./portfolio_val/202104202234-train.p.png')

plt.close(fig)
