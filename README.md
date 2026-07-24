# Xplainsight

**A tool for testing market claims against history.**

People say a lot about markets — chart signals, timing rules, "buy the dip," candlestick patterns. Xplainsight checks each claim against decades of real price history, using the same fixed, pre-declared test for every claim, and shows what actually happened — including when the claim failed. It never tells you what to buy.

The point isn't any single result. It's the method: how to check whether *any* market claim has evidence behind it.

## How to use it

Open `index.html` in any browser, or visit the hosted version. It works on a phone. Start with the **Start Here** room if you're new.

## What makes it different

- **Pre-registered tests.** The scoring rules are printed before any data loads, so they can't be bent to fit a result.
- **One rule for every claim.** No grading on a curve — the famous signals face the same checks as the deliberately meaningless ones.
- **It shows failures.** Claims that don't hold up are shown failing, in plain sight.
- **Plain language first.** Every technical term is tap-to-define; you never need to know statistics to understand the conclusion.
- **Nothing to sell.** No accounts, no wallet connections, no ads, no financial advice. Free to use, forever.

## Honest notes

- This is educational, not investment advice. It measures what happened in the past under fixed rules — never what will happen next.
- It reads real public data live from sources like DBnomics (OECD) and CoinGecko; those requests go to those services. Your own uploaded files never leave your device.
- It's in beta. If something looks wrong, assume it's a bug — and tell us.

## Checking our work

Every page's claims can be checked. The included `plainsight-validate.py` runs structural checks anyone can reproduce. The whole app is static files with no hidden code — use view-source on any page.

## Contact

Feedback: Xplainsight@duck.com

## Licence

MIT — see `LICENSE`. You are free to use, copy, modify, merge, publish, distribute,
sublicense and sell copies of this software, provided the copyright notice and licence
text travel with it.

This matches the project's founding vow: *free and forkable, public, no hidden logic.*
An earlier `COPYRIGHT.txt` reserved all rights and granted no licence, which contradicted
that vow and had no recorded decision behind it. It has been replaced.

**Note on scope:** MIT is a software licence and refers throughout to "the Software".
This project also contains substantial written educational content. If you want the prose
explicitly covered too, the usual companion is a Creative Commons licence (CC-BY-4.0) for
content alongside MIT for code. That decision has not been made here.
