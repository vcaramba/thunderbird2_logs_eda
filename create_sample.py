import dask.dataframe as dd
import gc

"""Extract 0,5% from original logs data"""
data = dd.read_csv('tbird2/tbird2.txt', sep='\t', header=None)
data = data.repartition(
    npartitions=data.npartitions // 100)  # work with dask dataframe in parallel - 100 MB per partition
df = data.sample(frac=0.005, replace=False)

# Explicitly clean up memory:
del data
gc.collect()

df.to_csv('data/tbird2.csv', single_file=True, index=False, header=False)
