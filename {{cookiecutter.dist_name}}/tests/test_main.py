from absl import app
from absl import flags

from absl.testing import absltest
from absl.testing import flagsaver
from absl.tests import app_test_helper

from {{ cookiecutter.package_name }} import main

FLAGS = flags.FLAGS

class UnitTest(absltest.TestCase):

    def test_main(self):
        with flagsaver.flagsaver(config='{{cookiecutter.dist_name}}/{{cookiecutter.package_name}}/config/default.py'):
            app_test_helper.main(main)