#Day 18 Testing practice - feature branch
import unittest


def check_status(cpu, memory, threshold=80):
    if cpu >= threshold or memory >= threshold:
        return "ALERT"
    return "NORMAL"


class TestSystemMonitor(unittest.TestCase):

    def test_normal_usage(self):
        self.assertEqual(
            check_status(30, 40),
            "NORMAL"
        )

    def test_high_cpu(self):
        self.assertEqual(
            check_status(90, 40),
            "ALERT"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)