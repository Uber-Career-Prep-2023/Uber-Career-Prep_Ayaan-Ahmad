import heapq

def merge_k_sorted_arrays(k, arrays):
    result = []
    min_heap = []

    # Push the first element from each array into the min_heap
    for i in range(k):
        if arrays[i]:
            heapq.heappush(min_heap, (arrays[i][0], i, 0))  # (element, array_index, index_in_array)

    while min_heap:
        element, array_index, index_in_array = heapq.heappop(min_heap)
        result.append(element)

        # Move to the next element in the same array
        if index_in_array + 1 < len(arrays[array_index]):
            heapq.heappush(min_heap, (arrays[array_index][index_in_array + 1], array_index, index_in_array + 1))

    return result