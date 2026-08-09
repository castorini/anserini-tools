<img src="docs/pyserini-logo.png" width="200" />

# Evaluation Data for Anserini and Pyserini

This repository holds various data and various tools used by [anserini](http://anserini.io/), [pyserini](http://pyserini.io/).

Build the included evaluation tools as follows (you might get warnings, but you can ignore):

```bash
cd eval && tar xvfz trec_eval.9.0.4.tar.gz && cd trec_eval.9.0.4 && make && cd ../..
cd eval && cd ndeval && make && cd ../..
```

## Topics

Topics for various evaluations are stored in [`topics/`](topics/).
Metadata is stored in [`topics.json`](topics.json) and aliases in [`topics-aliases.json`](topics-aliases.json).
In the aliases file, the keys represent canonical topics.

## Qrels

Qrels for various evaluations are stored in [`qrels/`](qrels/).
Metadata is stored in [`qrels.json`](qrels.json) and aliases in [`qrels-aliases.json`](qrels-aliases.json).
In the aliases file, the keys represent canonical topics.
