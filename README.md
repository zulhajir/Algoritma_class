# Algoritma_class

Muh. zulhjair. AR
F55123952

# Penjelasan Quiz
# Navie
**Best Case untuk Bubble Sort** terjadi ketika array yang diberikan sudah terurut. Dalam kondisi ini, **Bubble Sort** akan berjalan lebih efisien karena tidak perlu melakukan pertukaran elemen. Dengan optimasi yang menggunakan flag `swapped`, algoritma akan mendeteksi bahwa tidak ada pertukaran yang diperlukan setelah satu iterasi. Jika flag `swapped` tetap `False` pada akhir satu putaran, algoritma akan langsung berhenti, menghindari iterasi lebih lanjut.

Pada **best case**, algoritma hanya memerlukan satu putaran untuk memeriksa array, sehingga **kompleksitas waktunya** menjadi **O(n)**, di mana `n` adalah jumlah elemen dalam array. Ini adalah kondisi paling efisien untuk **Bubble Sort**, karena tidak ada pertukaran yang dilakukan dan algoritma berhenti lebih awal.

# Conquer
**Best Case** untuk **Merge Sort** terjadi ketika array yang diberikan sudah terurut. Meskipun **Merge Sort** selalu membagi array menjadi dua bagian dan menggabungkannya kembali, dalam kondisi terbaik, penggabungan elemen akan lebih efisien karena elemen-elemen dalam kedua bagian sudah terurut.

Pada **best case**, meskipun algoritma tetap membagi array, proses penggabungan akan lebih cepat karena tidak ada elemen yang perlu dipindahkan. Meskipun kompleksitas waktu untuk **Merge Sort** tetap **O(n log n)**, kondisi terbaik memungkinkan penggabungan yang lebih efisien karena tidak ada perubahan besar pada susunan array yang sudah terurut.

Dengan memeriksa apakah array sudah terurut sebelumnya, algoritma dapat langsung mengembalikan array tanpa melakukan pembagian lebih lanjut, yang membuatnya lebih cepat dalam kondisi terbaik.
