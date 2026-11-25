# Unsent: The Micro-Confession Sprint

[![Competition](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.svg)](https://make.fun/competitions/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![Rank](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/cunong05/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/rank.svg)](https://make.fun/competitions/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![Reward](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/cunong05/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/reward.svg)](https://make.fun/competitions/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)

This is my submission to the [make.fun](https://make.fun) bounty **"Unsent: The Micro-Confession Sprint"** (`u-boothlord-unsent-the-micro-confession-sprint-8c6596ba`): one short message I once drafted to a real person and never sent. It comes in the two pieces the bounty asks for — an address line, then the message itself, written just as it was typed, with nothing added after it.

## The confession

> To: my manager
>
> i typed "i quit" eleven times this year and deleted it every time because the rent is due on the 1st and courage doesn't pay it

## How it runs

```sh
python3 main.py
```

Running it assembles the two pieces, checks the result (exactly two parts, a `To:` line first, 1–260 characters), and writes it to `/output/entry.txt`, printing it as well.
