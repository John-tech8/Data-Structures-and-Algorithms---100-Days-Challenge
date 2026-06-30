def rotateArray(arr: list, k: int) -> list:
    # Write your code here.
    n=len(arr)
    if n==0:
        return
    k=k%n
    arr[:]=arr[k:]+arr[:k]
    return arr
