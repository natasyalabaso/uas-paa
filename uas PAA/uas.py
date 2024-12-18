# Insertion Sort
def insertion_sort(gaji):
    for i in range(1, len(gaji)):
        key, j = gaji[i], i - 1
        while j >= 0 and key < gaji[j]:
            gaji[j + 1] = gaji[j]
            j -= 1
        gaji[j + 1] = key
    return gaji

# Merge Sort
def merge_sort(gaji):
    if len(gaji) > 1:
        mid = len(gaji) // 2
        kiri, kanan = gaji[:mid], gaji[mid:]
        merge_sort(kiri)
        merge_sort(kanan)
        i = j = k = 0
        while i < len(kiri) and j < len(kanan):
            gaji[k] = kiri[i] if kiri[i] < kanan[j] else kanan[j]
            i, j = (i + 1, j) if kiri[i] < kanan[j] else (i, j + 1)
            k += 1
        gaji[k:] = kiri[i:] if i < len(kiri) else kanan[j:]
    return gaji

# Daftar Gaji Karyawan
gaji_karyawan = [4500000, 3200000, 5000000, 2800000, 7000000, 4000000]

# Pengurutan
print("Sebelum diurutkan:", gaji_karyawan)
print("di urutkan  menggunakan  Insertion Sort:", insertion_sort(gaji_karyawan.copy()))
print("di urutkan  menggunakan Merge Sort:", merge_sort(gaji_karyawan.copy()))
