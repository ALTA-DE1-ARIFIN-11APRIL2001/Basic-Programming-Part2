'''
Input Harga: 370000
Input Diskon: 15
Output: harga yang harus dibayar adalah Rp. 314.500
'''
harga_awal = 370000
diskon = 15
total_diskon = (diskon / 100) * harga_awal
harga_setelah_diskon = harga_awal - total_diskon

print("Harga yang harus dibayar adalah Rp.",harga_setelah_diskon)
