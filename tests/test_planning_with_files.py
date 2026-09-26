import unittest
import shutil
import tempfile
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from agent.planning_with_files import FilePlanner

class TestFilePlanner(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.planner = FilePlanner(self.test_dir)

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_plan_lifecycle(self):
        steps = ["Verify inventory stock", "Calculate batch costing", "Stage ERP invoice"]
        res = self.planner.init_plan("Batch Costing Workflow", steps)
        self.assertEqual(res["status"], "INITIALIZED")
        self.assertEqual(res["total_steps"], 3)

        # Step 1 in progress with finding
        u1 = self.planner.update_step(1, "in_progress", "Monomer emulsion stock is 450 Liters")
        self.assertEqual(u1["status"], "SUCCESS")
        self.assertTrue(u1["recorded_finding"])

        # Step 1 completed
        u2 = self.planner.update_step(1, "completed")
        self.assertEqual(u2["status"], "SUCCESS")

        # Read state
        state = self.planner.get_current_state()
        self.assertTrue(state["active"])
        self.assertIn("[x] Step 1:", state["plan"])
        self.assertIn("[ ] Step 2:", state["plan"])

    def test_uninitialized_plan_update(self):
        empty_planner = FilePlanner(tempfile.mkdtemp())
        res = empty_planner.update_step(1, "completed")
        self.assertEqual(res["status"], "ERROR")

if __name__ == "__main__":
    unittest.main()
