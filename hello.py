def run_program():
    name = input("Adınız nedir? ")

    try:
        age = int(input("Kaç yaşındasınız? "))

        print("Merhaba", name)

        if age >= 18:
            print(name, "reşitsiniz.")
        else:
            print(name, "reşit değilsiniz.")

        print(name, "GitHub'daki ilk Python programınızı çalıştırıyorsunuz!")

    except ValueError:
        print("Lütfen yaşınızı sayı olarak giriniz.")


run_program()
