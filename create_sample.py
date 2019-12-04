import dask.dataframe as dd
import gc

data = dd.read_csv('tbird2/tbird2.txt', sep='\t', header=None)
data = data.repartition(npartitions=data.npartitions // 100)
df = data.sample(frac=0.005, replace=False)
del data
gc.collect()
df.to_csv('data/tbird2.csv', single_file=True, index=False, header=False)
