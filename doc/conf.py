"""Sphinx configuration file for an LSST stack package.

This configuration only affects single-package Sphinx documentation builds.
"""

from documenteer.sphinxconfig.stackconf import build_package_configs
import lsst.kafka-connect-manager


_g = globals()
_g.update(build_package_configs(
    project_name='kafka-connect-manager',
    version=lsst.kafka-connect-manager.version.__version__))
