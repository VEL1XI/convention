class TemperatureConverter:
    """Konversi suhu antar satuan: Celsius, Fahrenheit, Kelvin"""

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9

    @staticmethod
    def celsius_to_kelvin(c):
        return c + 273.15

    @staticmethod
    def kelvin_to_celsius(k):
        return k - 273.15


class LengthConverter:
    """Konversi panjang antar satuan: Meter, Kilometer, Mil, Feet"""

    @staticmethod
    def km_to_miles(km):
        return km * 0.621371

    @staticmethod
    def miles_to_km(miles):
        return miles / 0.621371

    @staticmethod
    def meter_to_feet(meter):
        return meter * 3.28084

    @staticmethod
    def feet_to_meter(feet):
        return feet / 3.28084


class WeightConverter:
    """Konversi berat antar satuan: Kilogram, Gram, Pound, Ounce"""

    @staticmethod
    def kg_to_pounds(kg):
        return kg * 2.20462

    @staticmethod
    def pounds_to_kg(pound):
        return pound / 2.20462

    @staticmethod
    def gram_to_ounce(gram):
        return gram / 28.3495

    @staticmethod
    def ounce_to_gram(ounce):
        return ounce * 28.3495


def main():
    while True:
        print("\n=== Aplikasi Konversi ===")
        print("1. Suhu")
        print("2. Panjang")
        print("3. Berat")
        print("4. Keluar")
        choice = input("Pilih kategori konversi (1-4): ")

        if choice == "1":
            print("\n1. Celsius ke Fahrenheit")
            print("2. Fahrenheit ke Celsius")
            print("3. Celsius ke Kelvin")
            print("4. Kelvin ke Celsius")
            sub = input("Pilih jenis konversi: ")
            val = float(input("Masukkan nilai: "))
            if sub == "1":
                print("Hasil:", TemperatureConverter.celsius_to_fahrenheit(val), "°F")
            elif sub == "2":
                print("Hasil:", TemperatureConverter.fahrenheit_to_celsius(val), "°C")
            elif sub == "3":
                print("Hasil:", TemperatureConverter.celsius_to_kelvin(val), "K")
            elif sub == "4":
                print("Hasil:", TemperatureConverter.kelvin_to_celsius(val), "°C")
            else:
                print("Pilihan tidak valid.")

        elif choice == "2":
            print("\n1. KM ke Mil")
            print("2. Mil ke KM")
            print("3. Meter ke Feet")
            print("4. Feet ke Meter")
            sub = input("Pilih jenis konversi: ")
            val = float(input("Masukkan nilai: "))
            if sub == "1":
                print("Hasil:", LengthConverter.km_to_miles(val), "mil")
            elif sub == "2":
                print("Hasil:", LengthConverter.miles_to_km(val), "km")
            elif sub == "3":
                print("Hasil:", LengthConverter.meter_to_feet(val), "feet")
            elif sub == "4":
                print("Hasil:", LengthConverter.feet_to_meter(val), "meter")
            else:
                print("Pilihan tidak valid.")

        elif choice == "3":
            print("\n1. KG ke Pound")
            print("2. Pound ke KG")
            print("3. Gram ke Ounce")
            print("4. Ounce ke Gram")
            sub = input("Pilih jenis konversi: ")
            val = float(input("Masukkan nilai: "))
            if sub == "1":
                print("Hasil:", WeightConverter.kg_to_pounds(val), "pounds")
            elif sub == "2":
                print("Hasil:", WeightConverter.pounds_to_kg(val), "kg")
            elif sub == "3":
                print("Hasil:", WeightConverter.gram_to_ounce(val), "ounce")
            elif sub == "4":
                print("Hasil:", WeightConverter.ounce_to_gram(val), "gram")
            else:
                print("Pilihan tidak valid.")

        elif choice == "4":
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")


if __name__ == "__main__":
    main()
