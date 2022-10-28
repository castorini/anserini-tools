# dedup script shared by Sean MacAvaney on TREC Slack workspace, 2022/10/28

# usage: python dedup.py msmarco-v2-passage-neardupes.txt.gz myrun1 myrun2 ...
# outputs myrun1.dedup, myrun2.dedup, etc.

from collections import Counter
import argparse
import gzip

parser = argparse.ArgumentParser()
parser.add_argument('dupefile')
parser.add_argument('runs', nargs='+')
args = parser.parse_args()

equiv_map = {}
for line in gzip.open(args.dupefile, 'rt'):
  cols = line.split()
  class_id, doc_id = cols[0], cols[1]
  if class_id != doc_id:
    equiv_map[doc_id] = class_id

for run in args.runs:
  classes = set()
  qid_count = Counter()
  with open(run, 'rt') as fin, open(run+'.dedup', 'wt') as fout:
    for line in fin:
      qid, q0, did, rank, score, runid = line.split()
      class_id = equiv_map.get(did, did)
      key = (qid, class_id)
      if key not in classes:
        classes.add(key)
        new_rank = str(qid_count[qid])
        fout.write(' '.join([qid, q0, class_id, new_rank, score, runid]) + '\n')
        qid_count[qid] += 1
