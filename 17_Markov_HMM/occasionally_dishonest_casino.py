import numpy as np
import matplotlib.pyplot as plt


def sample_occasionally_dishonest_casino(N, sides=6):
    '''
    Samples dice rolls according to the occasionally dishonest casino.
    Every so often the casino transitions from using a fair die to using a biased die.
    '''
    fair = np.empty(N, dtype=bool)
    fair[0] = True
    for i in range(N - 1):
        if fair[i]:
            fair[i + 1] = np.random.choice([True, False], p=[.95, .05])
        else:
            fair[i + 1] = np.random.choice([True, False], p=[.10, .90])

    p_fair = 1 / sides * np.ones(sides)
    p_biased = .5 / (sides - 1) * np.ones(sides)
    p_biased[-1] = .5
    fair_samples = np.random.choice(sides, N, p=p_fair)
    biased_samples = np.random.choice(sides, N, p=p_biased)

    return fair, np.where(fair, fair_samples, biased_samples)


if __name__ == '__main__':
    fair, samples = sample_occasionally_dishonest_casino(10000)
    plt.figure()
    plt.plot(fair)
    plt.figure()
    plt.hist(samples, bins=np.arange(7) - .5)
    plt.show()