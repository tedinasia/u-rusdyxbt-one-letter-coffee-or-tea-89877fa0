"""One Letter: Coffee or Tea -- entry program.

Menulis tepat SATU huruf ke /output/entry.txt: "A" untuk kopi.

Alasan memilih "A" (kopi), bukan "B" (teh): kopi adalah jawaban yang
lebih berani dan lebih hidup. Juri menilai vividness paling dulu, dan
kopi membawa asosiasi energi, aroma, dan ritual pagi yang lebih kuat
dibanding teh -- sebuah huruf "A" yang terasa seperti secangkir kopi
panas di pagi hari, bukan sekadar pilihan yang aman.

KRITIS: file output harus TEPAT 1 byte. Huruf ditulis tanpa newline
("A\\n" = 2 byte = gagal gate), tanpa spasi, tanpa penjelasan apa pun.
"""

import os

# Huruf jawaban: "A" = kopi.
LETTER = "A"

# Lokasi output yang diminta kompetisi.
OUTPUT_PATH = "/output/entry.txt"


def write_letter(path, letter):
    """Tulis tepat satu huruf ke path, tanpa newline atau byte lain."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(letter)


def validate(path, letter):
    """Baca kembali file dan pastikan isinya tepat satu huruf itu.

    Mengembalikan True bila valid; bila tidak, raise SystemExit
    (exit non-zero) dengan pesan yang menjelaskan apa yang salah.
    """
    with open(path, "rb") as f:
        data = f.read()

    expected = letter.encode("utf-8")
    if data != expected or len(data) != 1:
        raise SystemExit(
            "entry tidak valid: isi=%r panjang=%d byte "
            "(harus %r, 1 byte)" % (data, len(data), expected)
        )
    return True


def main():
    write_letter(OUTPUT_PATH, LETTER)
    validate(OUTPUT_PATH, LETTER)


if __name__ == "__main__":
    main()
