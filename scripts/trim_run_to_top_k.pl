#
# Pyserini: Python interface to the Anserini IR toolkit built on Lucene
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""Filter a TREC run file to retain only the topk-k."""

import argparse


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=lambda prog: argparse.HelpFormatter(prog, width=100))
    parser.add_argument('--input', metavar='FILE', type=str, help='Input run.', required=True)
    parser.add_argument('--output', metavar='FILE', type=str, help='Output run.', required=True)
    parser.add_argument('--runtag', metavar='STRING', type=str, default=None, help='Runtag.')
    parser.add_argument('--k', metavar='NUM', type=int, default=1000, help='Number of hits to retain per topic.')
    args = parser.parse_args()

    with open(args.output, 'w') as output_f:
        with open(args.input) as input_f:
            for line in input_f:
                cols = line.split()
                qid = cols[0]
                docid = cols[2]
                rank = int(cols[3])
                score = cols[4] # Explicitly leave as str to avoid any rounding
                tag = cols[5]

                if rank > args.k:
                    continue

                if args.runtag:
                    tag = args.runtag

                output_f.write(f'{qid} Q0 {docid} {rank} {score} {tag}\n')


if __name__ == '__main__':
    main()
