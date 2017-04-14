from context import selection
import unittest

from selection import RadientController
from selection.util.config import load_settings

# todo : add more tests
class RadientTest(unittest.TestCase):

    def test_column_equality_src_target(self):
        controller = RadientController()
        source = controller.extract()
        target = controller.transform(source)
        self.assertTrue((target['rpsn_main']['nazn_vvst'] == source['uch']['uchgroupnaznach']).all())

    def test_by_count_of_columns_mapping_target(self):
        controller = RadientController()
        source = controller.extract()
        target = controller.transform(source)
        settings = load_settings(is_local=True)
        mapping_columns_count = len(settings['radient'].keys())
        target_columns_count = sum([len(v.columns) for k, v in target.items()])
        self.assertEqual(target_columns_count, mapping_columns_count)


if __name__ == '__main__':
    unittest.main()
