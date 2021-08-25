import logging
import re
import typing

import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.transforms.external import ImplicitSchemaPayloadBuilder
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.typehints import KV


def run(input_path, output_path, pipeline_args):
  pipeline_options = PipelineOptions(pipeline_args)

  with beam.Pipeline(options=pipeline_options) as p:
    input = (
        p
        | 'Read' >> ReadFromText(input_path).with_output_types(str)
        | 'ExtractWords' >> beam.FlatMap(lambda x: re.findall(r'[A-Za-z\']+', x)).with_output_types(str))

    java_output = (
        input
        | 'CountWords' >> beam.ExternalTransform(
              'my.beam.transform.wordextract',
              ImplicitSchemaPayloadBuilder({'prefix': 'java:'}),
              "localhost:12345").with_output_types(KV[str, int]))

    output = java_output | 'PrepareResults' >> beam.MapTuple(lambda k, v: '%s: %s' % (k, v)).with_output_types(str)

    output | 'Write' >> beam.io.WriteToText(output_path).with_input_types(str)


if __name__ == '__main__':
  logging.getLogger().setLevel(logging.INFO)
  import argparse

  parser = argparse.ArgumentParser()
  parser.add_argument(
      '--input',
      dest='input',
      required=True,
      help='Input file')
  parser.add_argument(
      '--output',
      dest='output',
      required=True,
      help='Output file')
  known_args, pipeline_args = parser.parse_known_args()

  run(
      known_args.input,
      known_args.output,
      pipeline_args)
