def max_score(cardPoints, k):
    n = len(cardPoints)
    total = sum(cardPoints)
    if k == n:
        return total
    
    min_subarray_sum = float('inf')
    current_sum = sum(cardPoints[:n-k])
    min_subarray_sum = current_sum
    
    for i in range(n-k, n):
        current_sum += cardPoints[i] - cardPoints[i - (n - k)]
        min_subarray_sum = min(min_subarray_sum, current_sum)
    
    return total - min_subarray_sum

# Example usage
print(max_score([1, 2, 3, 4, 5, 6, 1], 3))  # Output: 12
print(max_score([2, 2, 2], 2))              # Output: 4
print(max_score([9, 7, 7, 9, 7, 7, 9], 7))  # Output: 55
