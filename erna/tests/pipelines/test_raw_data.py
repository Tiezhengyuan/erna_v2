from unittest import TestCase

from pipelines.process.raw_data import RawData
from pipelines.tests import DIR_RAW_DATA

class TestRawData(TestCase):

  def test_scan_raw_data(self):
    RawData(DIR_RAW_DATA).scan_raw_data()