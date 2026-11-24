class ModuleTools:
    def square_root(self, value):
        # Return the square root of value. Import only sqrt from the math module: from math import sqrt.
        # A negative value raises ValueError (math domain error).
        pass

    def mean_value(self, values):
        # Return the mean of values. Import the statistics module under a shorter name: import statistics as stats.
        # An empty list raises statistics.StatisticsError.
        pass

    def module_attribute(self, module_name, attribute):
        # Import the module whose name is given as text (importlib.import_module) and return its attribute
        # (getattr). A module is an object whose attributes are the names defined in it.
        # A missing module raises ModuleNotFoundError, a missing attribute raises AttributeError.
        pass

    def module_name(self):
        # Return __name__. When this file is imported, __name__ is its module path, e.g. "src.objects.modules_imports";
        # when the file is run directly (python file.py), __name__ is "__main__".
        pass


# At the end of this file add a main block - it runs only when the file is started directly,
# not when it is imported:
# if __name__ == "__main__":
#     print(ModuleTools().square_root(16))
