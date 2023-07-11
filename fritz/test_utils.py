from unittest import TestCase

from fritz.utils import parse_call_log


class Test(TestCase):
    def test_parse_call_log_call(self):
        result = parse_call_log("05.07.23 16:59:01;CALL;0;0;004946342019022;01631643837;SIP0;")
        self.assertIsNotNone(result)
        self.assertEqual("CALL", result['type'])
        self.assertEqual("004946342019022", result['from'])
        self.assertEqual("01631643837", result['to'])

    def test_parse_call_log_ring(self):
        result = parse_call_log("01.07.23 11:34:03;RING;0;01331744839;004955142019022;SIP0;")
        # 01.07.23 11:34:07;DISCONNECT;0;0;")
        self.assertIsNotNone(result)
        self.assertEqual("RING", result['type'])
        self.assertEqual("01331744839", result['from'])
        self.assertEqual("004955142019022", result['to'])
