# MUH. ZULHAJIR. AR
# F55123052

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Data input
X = [1, 5, 6, 4, 3, 3, 3, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
X_sorted = quick_sort(X)
print("Hasil Quick Sort:", X_sorted)


      # Quick Sort
# Worst Case: O(n²), terjadi jika pivot terpilih selalu elemen terkecil atau terbesar, menyebabkan pembagian tidak seimbang.
# Best Case: O(n log n), terjadi jika pivot membagi array menjadi dua bagian yang seimbang.
# Average Case: O(n log n), rata-rata performa bergantung pada distribusi data dan pemilihan pivot.


         