import importlib
import inspect
import pkgutil
import logging

logger = logging.getLogger(__name__)

from src.shapes.base_shape import Shapes


def list_classes_in_package(package_name):
  """
  Lists all classes in a given package (including submodules).

  Args:
    package_name: The name of the package to inspect.

  Returns:
    A list of class names in the package.
  """
  all_classes = []
  try:
    # Import the package
    package = importlib.import_module(package_name)
    # Iterate over all modules in the package
    for _, modname, ispkg in pkgutil.walk_packages(path=package.__path__):
      if not ispkg:  # Only process modules, not subpackages
        module_name = f"{package_name}.{modname}"
        module = importlib.import_module(module_name)

        # Get all classes in the module
        classes = inspect.getmembers(
          module, inspect.isclass)
        all_classes.extend(classes)

    return all_classes
  except ModuleNotFoundError:
    logger.error(f"Package '{package_name}' not found.")
    return []

# Example usage:
package_name = "src.shapes"  # Replace with your package name
class_list = list_classes_in_package(package_name)

base_subclasses = [(cls_name.lower(), cls) \
                   for cls_name, cls in class_list if issubclass(
  cls,Shapes)
]

shape_registry_mapping = dict(
  base_subclasses
)
print(shape_registry_mapping)
