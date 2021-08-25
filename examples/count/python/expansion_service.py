from __future__ import absolute_import

import argparse
import logging
import signal
import sys

import grpc

import apache_beam as beam
from apache_beam.pipeline import PipelineOptions
from apache_beam.portability.api import beam_expansion_api_pb2_grpc
from apache_beam.runners.portability import expansion_service
from apache_beam.transforms import ptransform
from apache_beam.utils import thread_pool_executor
from apache_beam.utils.thread_pool_executor import UnboundedThreadPoolExecutor
from google.protobuf.text_format import Parse


class _MyFn(beam.DoFn):
    def process(self, element):
        print(element + ' \n xxxxxxxxxxxxxxxxxxxxxxx \n')
        return element + '#'

URN = "beam:transforms:xlang:pythontransform"

@ptransform.PTransform.register_urn(URN, None)
class PythonTransform(ptransform.PTransform):
    def __init__(self):
        super(PythonTransform, self).__init__()

    def expand(self, pcoll):
        return pcoll

    def to_runner_api_parameter(self, unused_context):
        return URN, None

    def from_runner_api_parameter(
        unused_ptransform, unused_paramter, unused_context):
        return PythonTransform()


server = None
_LOGGER = logging.getLogger(__name__)


def cleanup(unused_signum, unused_frame):
    _LOGGER.info('Shutting down expansion service.')
    server.stop(None)


def main(unused_argv):
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '-p', '--port', type=int, help='port on which to serve the job api')
  options = parser.parse_args()
  global server
  server = grpc.server(thread_pool_executor.shared_unbounded_instance())
  beam_expansion_api_pb2_grpc.add_ExpansionServiceServicer_to_server(
      expansion_service.ExpansionServiceServicer(
          PipelineOptions(
              ["--experiments", "beam_fn_api", "--sdk_location", "container"])), server)
  server.add_insecure_port('localhost:{}'.format(options.port))
  server.start()
  _LOGGER.info('Listening for expansion requests at %d', options.port)
  #print('Listening for expansion requests at', str(options.port)

  signal.signal(signal.SIGTERM, cleanup)
  signal.signal(signal.SIGINT, cleanup)
  signal.pause()


if __name__ == '__main__':
  logging.getLogger().setLevel(logging.INFO)
  main(sys.argv)