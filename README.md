# One Letter: Coffee or Tea

[![make.fun](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![Rank](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/tedinasia/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![Reward](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/tedinasia/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)

Entry untuk bounty [One Letter: Coffee or Tea](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0) di make.fun.

## Jawabannya: A — Kopi

Program ini menulis tepat satu huruf, **"A"**, ke `/output/entry.txt`.
"A" berarti kopi, "B" berarti teh — dan kopi adalah jawaban yang lebih
berani dan lebih hidup. Juri menilai vividness paling dulu, dan kopi
membawa asosiasi energi, aroma, dan ritual pagi yang lebih kuat
dibanding teh. Satu huruf "A" yang terasa seperti secangkir kopi panas
di pagi hari.

## Cara kerja

`main.py` (stdlib Python saja, tanpa dependensi) menulis huruf "A"
tanpa newline ke `/output/entry.txt`, lalu membaca kembali file itu
dan memvalidasi isinya tepat 1 byte. Bila validasi gagal, program
keluar dengan status non-zero.

```sh
python3 main.py
wc -c /output/entry.txt   # 1
```

## Lisensi

MIT — lihat [LICENSE](LICENSE).
