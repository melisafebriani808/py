# phone = input("Phone: ")
# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }
# output = ""
# for ch in phone:
#     output += digits_mapping.get(ch, "!") + " "
# print(output)


buah = input("Masukkan nama buah: ")
buah_mapping = {
    "apple": "🍎",
    "banana": "🍌",
    "mango": "🥭",
    "pear": "🍐",
    "grape": "🍇",
    "kiwi":"🥝",
    "cherry":"🍒",
    "peach":"🍑",
    "melon":"🍈",
    "lime":"🍋"
}

# Pisahkan input jadi kata-
# kata, lalu ubah jika ada di kamus
words = buah.split()
output = ""
for word in words:
    output += buah_mapping.get(word.lower(), word) + " "

print(output.strip())
