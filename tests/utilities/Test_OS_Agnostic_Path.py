import os
import pytest
from utilities.OS_Agnostic_Path import get_os_agnostic_path

def test_get_os_agnostic_path_single_rel_path():
    rel_path = 'subdir'
    expected_path = os.path.join(os.getcwd(), rel_path)
    assert get_os_agnostic_path(rel_path) == expected_path

def test_get_os_agnostic_path_multiple_rel_paths():
    rel_paths = ['subdir1', 'subdir2', 'subdir3']
    expected_path = os.path.join(os.getcwd(), *rel_paths)
    assert get_os_agnostic_path(*rel_paths) == expected_path

def test_get_os_agnostic_path_empty_input():
    assert get_os_agnostic_path() == os.getcwd()

def test_get_os_agnostic_path_non_string_input():
    with pytest.raises(TypeError):
        get_os_agnostic_path(123)

def test_get_os_agnostic_path_invalid_input():
    with pytest.raises(TypeError):
        get_os_agnostic_path(None)