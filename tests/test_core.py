import pytest

from r2d7.core import DroidCore


data_files = [
    'conditions',
    'damage-deck-core',
    'damage-deck-core-tfa',
    'pilots',
    # 'reference-cards',
    'ships',
    # 'sources',
    'upgrades',
]

def test_data(testbot):
    for filename in data_files:
        assert filename in testbot.data

    assert testbot.data_version is not None
    assert testbot.data['ships']['xwing'][0]['name'] == 'X-wing'
    assert testbot.data['conditions']['adebttopay'][0]['id'] == 3



partial_canonicalize_tests = {
    'X-Wing': 'xwing',
    'T-70 X-Wing': 't70xwing',
    'Veteran instincts': 'veteraninstincts',
}
@pytest.mark.parametrize('before, after', partial_canonicalize_tests.items())
def test_partial_canonicalize(before, after):
    assert DroidCore.partial_canonicalize(before) == after


def test_needs_update(testbot):
    assert testbot.data_version is not None
    assert not testbot.needs_update()
