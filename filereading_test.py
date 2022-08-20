import unittest
from unittest import mock
from filereading import read_by_records


class TestFileHandler(unittest.TestCase):

    def test_file_read_correct_data_in_file_successfully(self):

        data_lines = [
            'x,y1,y2,y3,y4',
            '-20.0,13.293808,-19.596016,-5.0705276,289.465',
            '-19.9,13.417889,-19.932789,-5.759763,285.60815']

        m = mock.mock_open(read_data='\n'.join(data_lines))

        with mock.patch('builtins.open', m):
            index: int = 0

            # ACT
            for record in read_by_records('test_file'):
                if record.is_header:
                    data_line = data_lines[index].split(sep=',')

                    # ASSERT
                    self.assertTupleEqual(
                        tuple(data_line), record.items)
                else:
                    data_line = [float(x)
                                 for x in data_lines[index].split(sep=',')]

                    # ASSERT
                    self.assertTupleEqual(
                        tuple(data_line), record.items)
                index += 1


if __name__ == '__main__':
    unittest.main()
