# From https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Welford's_online_algorithm

# for a new value newValue, compute the new count, new mean, the new M2.
# mean accumulates the mean of the entire dataset
# M2 aggregates the squared distance from the mean
# count aggregates the number of samples seen so far
def update(existingAggregate, newValue):
    (count, mean, M2) = existingAggregate
    count += 1 
    delta = newValue - mean
    mean += delta / count
    delta2 = newValue - mean
    M2 += delta * delta2

    return (count, mean, M2)

# retrieve the mean, variance and sample variance from an aggregate
def finalize(existingAggregate):
    (count, mean, M2) = existingAggregate
    (mean, variance, sampleVariance) = (mean, M2/count, M2/(count - 1)) 
    if count < 2:
        return float('nan')
    else:
        return (mean, variance, sampleVariance)


existingAggregate = [0,0,0]

print(existingAggregate)
existingAggregate  = update(existingAggregate,1.)
print(existingAggregate)
existingAggregate  = update(existingAggregate,2.)
print(existingAggregate)
existingAggregate  = update(existingAggregate,3.)
print(existingAggregate)
existingAggregate  = update(existingAggregate,4.)
print(existingAggregate)

mean, variance, sampleVariance = finalize(existingAggregate)

print(mean)
print(variance)
print(sampleVariance)

