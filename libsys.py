import os

class Library:
    def __init__(self, filename="books.txt"):

        self.filename = filename
        self.file = open(filename, "a+")

    def close(self):
        self.file.close()

    def list_books(self):
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
            for line in lines:
                title, author, release_year, pages = line.strip().split(",")
                print(f"Adı: {title}, Yazarı: {author}, Yayınlanma tarihi: {release_year}, Sayfa sayısı: {pages}")
        except FileNotFoundError:
            print("Kitap bulunamadı.")

    def add_book(self):
        title = input("Kitap adı: ")
        author = input("Kitap yazarı: ")
        release_year = input("yayınlanma tarihi: ")
        pages = input("Sayfa sayısı: ")
        with open(self.filename, "a+") as file:
            file.write(f"{title},{author},{release_year},{pages}\n")
        print(f" '{title}' adlı kitap eklendi.")

    def remove_book(self):
        title = input("Silmek için kitap adı giriniz: ")
        with open(self.filename, "r") as file:
            lines = file.readlines()
        new_lines = []
        for line in lines:
            if not line.strip().startswith(title):
                new_lines.append(line)
        with open(self.filename, "w") as file:
            file.writelines(new_lines)
        print(f"'{title}' adlı kitap başarıyla kaldırıldı.") if new_lines else print("Book not found.")

def main():
    lib = Library()

    while True:
        print("\n*** MENU ***")
        print("1) Kitapları Listele")
        print("2) Kitap Ekle")
        print("3) Kitap Sil")
        print("4) Çıkış")

        choice = input("\nBir şık seçiniz: ")

        if choice == "1":
            lib.list_books()
        elif choice == "2":
            lib.add_book()
        elif choice == "3":
            lib.remove_book()
        elif choice == "4":
            break
        else:
            print("Hatalı Seçim. Tekrar deneyin.")

    lib.close()  # Ensure file is closed before exiting

if __name__ == "__main__":
    main()
