import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise7.py')
_spec = importlib.util.spec_from_file_location("exercise7_lab6", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
manage_playlist = _module.manage_playlist

def test_example_from_lab():
    """Test the exact example from the lab description"""
    current_playlist = {"Song_A", "Song_B", "Song_C"}
    add_songs = ["Song_D", "Song_E", "Song_F"]
    import_playlist = {"Song_G", "Song_H", "Song_I"}
    banned_songs = {"Song_B", "Song_E", "Song_H"}
    result = manage_playlist(current_playlist, add_songs, import_playlist, banned_songs)
    assert result == 6

def test_no_operations():
    """Test when playlist stays as is"""
    current_playlist = {"Song_A", "Song_B"}
    add_songs = []
    import_playlist = set()
    banned_songs = set()
    result = manage_playlist(current_playlist, add_songs, import_playlist, banned_songs)
    assert result == 2

def test_add_only():
    """Test adding songs individually"""
    current_playlist = {"Song_A"}
    add_songs = ["Song_B", "Song_C"]
    import_playlist = set()
    banned_songs = set()
    result = manage_playlist(current_playlist, add_songs, import_playlist, banned_songs)
    assert result == 3

def test_import_only():
    """Test importing playlist"""
    current_playlist = {"Song_A"}
    add_songs = []
    import_playlist = {"Song_B", "Song_C", "Song_D"}
    banned_songs = set()
    result = manage_playlist(current_playlist, add_songs, import_playlist, banned_songs)
    assert result == 4

def test_ban_only():
    """Test removing banned songs"""
    current_playlist = {"Song_A", "Song_B", "Song_C", "Song_D"}
    add_songs = []
    import_playlist = set()
    banned_songs = {"Song_B", "Song_D"}
    result = manage_playlist(current_playlist, add_songs, import_playlist, banned_songs)
    assert result == 2

def test_exceeds_limit_needs_trimming():
    """Test when playlist exceeds 6 and needs random removal"""
    current_playlist = {"Song_A"}
    add_songs = ["Song_B", "Song_C", "Song_D"]
    import_playlist = {"Song_E", "Song_F", "Song_G", "Song_H"}
    banned_songs = set()
    result = manage_playlist(current_playlist, add_songs, import_playlist, banned_songs)
    assert result == 6  # Should trim to exactly 6

def test_empty_playlist_build_from_scratch():
    """Test building playlist from empty"""
    current_playlist = set()
    add_songs = ["Song_A", "Song_B"]
    import_playlist = {"Song_C", "Song_D"}
    banned_songs = set()
    result = manage_playlist(current_playlist, add_songs, import_playlist, banned_songs)
    assert result == 4

def test_add_duplicate_songs():
    """Test adding duplicate songs (should only add once)"""
    current_playlist = {"Song_A"}
    add_songs = ["Song_A", "Song_B", "Song_A"]
    import_playlist = set()
    banned_songs = set()
    result = manage_playlist(current_playlist, add_songs, import_playlist, banned_songs)
    assert result == 2  # Song_A already exists, Song_B added

def test_ban_nonexistent_songs():
    """Test banning songs that don't exist (should not error)"""
    current_playlist = {"Song_A", "Song_B"}
    add_songs = []
    import_playlist = set()
    banned_songs = {"Song_Z", "Song_Y"}
    result = manage_playlist(current_playlist, add_songs, import_playlist, banned_songs)
    assert result == 2

def test_all_songs_banned():
    """Test when all songs get banned"""
    current_playlist = {"Song_A", "Song_B"}
    add_songs = []
    import_playlist = set()
    banned_songs = {"Song_A", "Song_B"}
    result = manage_playlist(current_playlist, add_songs, import_playlist, banned_songs)
    assert result == 0

def test_import_overlaps_with_current():
    """Test importing songs that already exist"""
    current_playlist = {"Song_A", "Song_B"}
    add_songs = []
    import_playlist = {"Song_A", "Song_C"}
    banned_songs = set()
    result = manage_playlist(current_playlist, add_songs, import_playlist, banned_songs)
    assert result == 3  # A, B, C

def test_exactly_6_no_trimming():
    """Test when playlist is exactly 6 after operations"""
    current_playlist = {"Song_A", "Song_B"}
    add_songs = ["Song_C", "Song_D"]
    import_playlist = {"Song_E", "Song_F"}
    banned_songs = set()
    result = manage_playlist(current_playlist, add_songs, import_playlist, banned_songs)
    assert result == 6

def test_large_playlist_trimmed_to_6():
    """Test large playlist getting trimmed"""
    current_playlist = set()
    add_songs = [f"Song_{i}" for i in range(5)]
    import_playlist = {f"New_{i}" for i in range(10)}
    banned_songs = set()
    result = manage_playlist(current_playlist, add_songs, import_playlist, banned_songs)
    assert result == 6  # Should be trimmed to 6

def test_add_then_ban_same_song():
    """Test adding a song then banning it"""
    current_playlist = {"Song_A"}
    add_songs = ["Song_B", "Song_C"]
    import_playlist = set()
    banned_songs = {"Song_B"}
    result = manage_playlist(current_playlist, add_songs, import_playlist, banned_songs)
    assert result == 2  # Song_A, Song_C (Song_B added then removed)

def test_empty_everything():
    """Test with all empty inputs"""
    result = manage_playlist(set(), [], set(), set())
    assert result == 0
