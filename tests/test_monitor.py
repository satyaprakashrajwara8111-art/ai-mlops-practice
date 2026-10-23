
import unittest
from app.monitor import get_system_status


class TestSystemMonitor(unittest.TestCase):

    def test_status_has_required_fields(self):
        result = get_system_status()

        self.assertIn("timestamp", result)
        self.assertIn("cpu", result)
        self.assertIn("memory", result)
        self.assertIn("status", result)

    def test_cpu_is_numeric(self):
        result = get_system_status()

        self.assertIsInstance(result["cpu"], (int, float))

    def test_memory_is_numeric(self):
        result = get_system_status()

        self.assertIsInstance(result["memory"], (int, float))

    def test_status_is_valid(self):
        result = get_system_status()

        self.assertIn(result["status"], ["NORMAL", "ALERT"])
    
    def test_cpu_is_in_valid_range(self):
        result = get_system_status()

        self.assertGreaterEqual(result["cpu"], 0)
        self.assertLessEqual(result["cpu"], 100)

    def test_memory_is_in_valid_range(self):
        result = get_system_status()

        self.assertGreaterEqual(result["memory"], 0)
        self.assertLessEqual(result["memory"], 100)

if __name__ == "__main__":
    unittest.main()
