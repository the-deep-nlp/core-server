def batched(iterable, batch_size=100):
    batches = []
    for i, x in enumerate(iterable):
        batches.append(x)
        if (i+1) % batch_size == 0:
            yield batches
            batches = []
    if batches:
        yield batches
    return
