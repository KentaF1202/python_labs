# benchmark with timeit and tracemalloc to see the performance of loading a .env file with
# multiple .env file sizes and different numbers of variables

# illustrate the performance is negligble for typical use cases where the variables are loaded once
# bottleneck if used in a loop, should not be used that way