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

import argparse
import logging
import os
from tqdm import tqdm
import pyarrow as pa
import pyarrow.parquet as pq


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Convert vector fields in parquet files from double to float, to reduce storage requirements.')
    parser.add_argument('--input', required=True, help='Directory containing input parquet files, as doubles.')
    parser.add_argument('--output', required=True, help='Directory to store output parquet files, as floats.')
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    new_schema = pa.schema([
        pa.field("docid", pa.string()),
        pa.field("vector", pa.list_(pa.float32()))
    ])

    parquet_files = [f for f in os.listdir(args.input) if f.endswith(".parquet")]

    for file_name in parquet_files:
        input_file = os.path.join(args.input, file_name)
        output_file = os.path.join(args.output, file_name.replace(".parquet", "_float.parquet"))

        logging.info(f"Processing {input_file}...")

        table = pq.read_table(input_file)

        logging.info("Converting 'vector' field from double to float...")
        new_columns = []
        for column in table.column_names:
            if column == "vector":
                float_vector = [
                    pa.array(row, type=pa.float32()) if row is not None else None
                    for row in tqdm(table[column].to_pylist(), desc="Converting rows")
                ]
                new_columns.append(pa.array(float_vector, type=pa.list_(pa.float32())))
            else:
                new_columns.append(table[column])

        logging.info("Creating new table...")
        new_table = pa.Table.from_arrays(new_columns, schema=new_schema)

        logging.info(f"Writing to {output_file}...")
        pq.write_table(new_table, output_file)

        logging.info(f"Completed! Converted file saved to {output_file}")