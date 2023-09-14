def sliding_window_maximum(nums, k):
    if not nums or k <= 0:
        return []

    result = []
    window = []

    for i, num in enumerate(nums):
        while window and nums[window[-1]] < num:
            window.pop()
        window.append(i)

        if window[0] == i - k:
            window.pop(0)

        if i >= k - 1:
            result.append(nums[window[0]])

    return result
