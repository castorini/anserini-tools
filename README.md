# Anserini Evaluation Tools

This repo holds evaluation tools shared across [anserini](http://anserini.io/), [pyserini](http://pyserini.io/), and [pygaggle](http://pygaggle.ai/) as a Git submodule.

Build included tools as follows (you might get warnings, but you can ignore):

```bash
tar xvfz trec_eval.9.0.4.tar.gz && cd trec_eval.9.0.4 && make && cd ..
cd ndeval && make && cd ..
```
