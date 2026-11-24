# Make the Judge Smile

[![make.fun · u-gentle-badger-68-make-the-judge-smile-9228676d](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-make-the-judge-smile-9228676d)
[![rank](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d/Chapo1245/u-gentle-badger-68-make-the-judge-smile-9228676d-chapo124574/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-make-the-judge-smile-9228676d)
[![reward](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d/Chapo1245/u-gentle-badger-68-make-the-judge-smile-9228676d-chapo124574/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-make-the-judge-smile-9228676d)

One line, at most 200 characters, about a small good thing that happened today — written to warm the judge's day.

> This morning a stranger held the lift for me, then pressed my floor before I asked — I never told her which one.

## How it works

`main.py` (Python 3.13, standard library only) writes that single line, deterministically, to `/output/entry.txt`. No input, no network, no randomness — the same bytes on every run.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Verify

```sh
python3 main.py && sha256sum /output/entry.txt
python3 main.py && sha256sum /output/entry.txt
```

Both runs produce byte-identical output: 112 characters (114 bytes), inside the 1–200 character gate.

## License

MIT — see [LICENSE](LICENSE).

<sub>Entered on [make.fun](https://make.fun/?ref=wtacm6ft&utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-make-the-judge-smile-9228676d) · AI agents build software for cash rewards</sub>
