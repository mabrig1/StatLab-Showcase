"""Independent synthetic frequency-summary example."""
import math

def summarize(counts: list[int]) -> dict:
    if len(counts) != 5 or any(type(c) is not int or c < 0 for c in counts):
        raise ValueError("Provide five nonnegative integer counts")
    n = sum(counts)
    if n == 0:
        raise ValueError("At least one response required")
    mean = sum(i*c for i,c in enumerate(counts, 1))/n
    ss = sum(c*(i-mean)**2 for i,c in enumerate(counts, 1))
    return {"n": n, "mean": mean, "population_sd": math.sqrt(ss/n),
            "sample_sd": math.sqrt(ss/(n-1)) if n > 1 else None,
            "percentages": [100*c/n for c in counts]}

if __name__ == "__main__":
    print(summarize([1,2,4,2,1]))
