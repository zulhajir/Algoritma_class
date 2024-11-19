# MUH. ZULHAJIR. AR 
# F551123052


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Rekursif sorting
        merge_sort(left_half)
        merge_sort(right_half)

        # Menggabungkan hasil sorting
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Menyalin elemen yang tersisa
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Data input
X = [1, 5, 6, 4, 3, 3, 3, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
merge_sort(X)
print("Hasil Merge Sort:", X)


         # Merge Sort
# Worst Case: O(n log n) karena selalu membagi array menjadi dua bagian yang sama dan menggabungkannya. Tidak ada kondisi buruk yang signifikan.
# Best Case: O(n log n), karena operasi pembagian dan penggabungan tetap sama.
# Average Case: O(n log n), rata-rata performanya selalu stabil.








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
