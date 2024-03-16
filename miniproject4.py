import math

class LinkedList:
    # Fungsi lain di sini ...

    def fibonacci_search(self, key, attribute):
        if not self.head:
            return None
        
        length = self.length()
        fib_m_minus_2 = 0
        fib_m_minus_1 = 1
        fib = fib_m_minus_1 + fib_m_minus_2

        while fib < length:
            fib_m_minus_2 = fib_m_minus_1
            fib_m_minus_1 = fib
            fib = fib_m_minus_1 + fib_m_minus_2

        offset = -1
        current = self.head

        while fib > 1:
            i = min(offset + fib_m_minus_2, length - 1)

            while i > offset and current:
                current = current.next
                i -= 1

            if not current:
                return None

            if current.data[attribute] < key:
                fib = fib_m_minus_1
                fib_m_minus_1 = fib_m_minus_2
                fib_m_minus_2 = fib - fib_m_minus_1
                offset = i
            elif current.data[attribute] > key:
                fib = fib_m_minus_2
                fib_m_minus_1 -= fib_m_minus_2
                fib_m_minus_2 = fib - fib_m_minus_1
            else:
                return current.data

        if fib_m_minus_1 and current and current.data[attribute] == key:
            return current.data

        return None

# Modifikasi bagian pemanggilan pencarian:

while True:
    # Bagian lain dari program ...
    elif choice == "4":  # Tambahkan pilihan untuk melakukan pencarian
        key = input("Masukkan kata kunci yang ingin Anda cari: ")
        attribute = input("Pilih atribut untuk mencari (misalnya, 'username', 'nama', dll.): ")
        result = miniatur_list.fibonacci_search(key, attribute)
        if result:
            print("Data ditemukan:", result)
        else:
            print("Data tidak ditemukan.")
    else:
        print("Pilihan tidak valid.")
