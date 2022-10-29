import pytest
from miscell.tree import tree
import testdata


@pytest.mark.parametrize('test_input,test_expected',
                         [(testdata.source1, testdata.expected1),
                          (testdata.source2, testdata.expected2)])
def test_tree(test_input, test_expected):
    assert tree.build_tree(test_input) == test_expected


if __name__ == '__main__':
    pytest.main()
