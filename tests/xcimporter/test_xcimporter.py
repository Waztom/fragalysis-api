import unittest
import os
from fragalysis_api import xcimporter

from fragalysis_api.xcimporter.single_import import import_single_file


class XcImporterTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.in_dir = os.path.join(
            'tests', 'data_for_tests', 'examples_to_test5')
        cls.in_file = os.path.join(
            'tests', 'data_for_tests', 'examples_to_test5', 'Mpro-x0978.pdb')
        cls.in_file_no_ext = 'Mpro-x0978'
        cls.out_dir = os.path.join('tests', 'data_for_tests')
        cls.target = 'TestTarget'
        cls.validate = False
        cls.rrf = True
        cls.biomol = os.path.join(
            'tests', 'data_for_tests', 'examples_to_test5', 'biomol.txt')
        cls.metadata = True
        cls.covalent = True
        cls.reference = 'Mpro-x0981_A'
        cls.mll = -1

    @classmethod
    def tearDownClass(cls):
        #rmtree(os.path.join(cls.out_dir, cls.target))
        pass

    def test_xcimporter(self):

        xcimporter(
            in_dir=self.in_dir,
            out_dir=self.out_dir,
            target=self.target,
            validate=self.validate,
            reduce_reference_frame=self.rrf,
            metadata=self.metadata,
            biomol=self.biomol,
            covalent=self.covalent,
            pdb_ref=self.reference,
            max_lig_len=self.mll
        )
        # Write more Tests
        self.assertTrue(expr=os.path.exists(
            os.path.join(self.out_dir, self.target)))
        self.assertTrue(expr=os.path.exists(os.path.join(
            self.out_dir, self.target, 'reference.pdb')))

        import_single_file(in_file=self.in_file,
                           out_dir=self.out_dir,
                           target=self.target,
                           reduce_reference_frame=self.rrf,
                           reference_pdb=os.path.join(
                               self.out_dir, self.target, 'reference.pdb'),
                           biomol=self.biomol,
                           covalent=self.covalent,
                           max_lig_len=self.mll)

        # Tests should check if a thing is correctly removed and readded etc...
        # Write Many More... Single import should use a pdb in a seperate test!
        self.assertTrue(expr=os.path.exists(os.path.join(
            self.out_dir, self.target, 'reference.pdb')))


if __name__ == '__main__':
    unittest.main()
