import importlib
import io
import math
import os
import runpy
import statistics
import unittest
from unittest.mock import patch

import src.objects.modules_imports as module
from src.objects.modules_imports import ModuleTools


class TestModuleTools(unittest.TestCase):
    def setUp(self):
        self.tools = ModuleTools()

    def test_from_import(self):
        self.assertEqual(self.tools.square_root(16), 4.0)
        self.assertEqual(self.tools.square_root(2.25), 1.5)
        with self.assertRaises(ValueError):
            self.tools.square_root(-1)

    def test_import_with_alias(self):
        self.assertEqual(self.tools.mean_value([1, 2, 3, 4]), 2.5)
        # statistics.mean keeps int for whole-number results (fmean would give 3.0), and it is not the median (2).
        self.assertIs(type(self.tools.mean_value([1, 2, 6])), int)
        self.assertEqual(self.tools.mean_value([1, 2, 6]), 3)
        with self.assertRaises(statistics.StatisticsError):
            self.tools.mean_value([])

    def test_module_is_an_object_with_attributes(self):
        self.assertEqual(self.tools.module_attribute("math", "pi"), math.pi)
        self.assertIs(self.tools.module_attribute("os.path", "join"), os.path.join)

    def test_import_errors(self):
        with self.assertRaises(ModuleNotFoundError):
            self.tools.module_attribute("no_such_module_xyz", "x")
        # ModuleNotFoundError is a subclass of ImportError.
        self.assertTrue(issubclass(ModuleNotFoundError, ImportError))
        with self.assertRaises(AttributeError):
            self.tools.module_attribute("math", "no_such_name")

    def test_dunder_name_when_imported(self):
        self.assertEqual(self.tools.module_name(), "src.objects.modules_imports")

    def test_main_block_runs_only_when_started_directly(self):
        output = io.StringIO()
        with patch("sys.stdout", output):
            importlib.reload(module)
        self.assertEqual(output.getvalue(), "")
        output = io.StringIO()
        with patch("sys.stdout", output):
            runpy.run_path(module.__file__, run_name="__main__")
        self.assertEqual(output.getvalue(), "4.0\n")
