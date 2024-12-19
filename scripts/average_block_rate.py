from time import time_ns
from tqdm import tqdm
from blockchain.blockchain import Blockchain
import pandas as pd
import matplotlib.pyplot as plt
from configs.config import SECONDS

blockchain = Blockchain()

times = []

n = 100

for i in tqdm(range(n)):
    start_ts = time_ns()
    blockchain.add_block(i)
    end_ts = time_ns()

    times.append((end_ts - start_ts) / SECONDS)

df = pd.DataFrame({
    'Time_to_mine': times
})

df['cum_sum_time'] = df['Time_to_mine'].cumsum()
df['avg_time_to_mine'] = df['cum_sum_time'] / (df.index.values + 1)
print(df)

plt.plot(df['Time_to_mine'], label = 'time to mine')
plt.plot(df['avg_time_to_mine'], label = 'AVG time to mine')
plt.legends()
plt.show()