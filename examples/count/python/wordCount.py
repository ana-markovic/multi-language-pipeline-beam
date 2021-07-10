import logging
import re
import typing

import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.transforms.external import ImplicitSchemaPayloadBuilder
from apache_beam.options.pipeline_options import PipelineOptions


def run(input_path, output_path, pipeline_args):
  pipeline_options = PipelineOptions(pipeline_args)

  with beam.Pipeline(options=pipeline_options) as p:
    input = p | 'Read' >> ReadFromText(input_path).with_output_types(str)

    java_output = (
        input
        | 'ExtractWords' >> beam.ExternalTransform(
              'my.beam.transform.wordextract',
              ImplicitSchemaPayloadBuilder({}),
              "localhost:12345"))


    output = (
        java_output
        | 'CountWords' >>  beam.combiners.Count.PerElement()
        | 'PrepareResults' >> beam.MapTuple(lambda word, count: '%s: %s' % (word, count)))

    output | 'Write' >> WriteToText(output_path)


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
