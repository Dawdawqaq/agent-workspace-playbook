"""Self-contained acceptance example for a task that lists duplicate entries."""
import unittest


def duplicates(entries):
    seen = set()
    repeated = set()
    for entry in entries:
        if entry in seen:
            repeated.add(entry)
        seen.add(entry)
    return sorted(repeated)


class AcceptanceTest(unittest.TestCase):
    def test_repeated_bookmarks_are_reported_once(self):
        self.assertEqual(duplicates(["guide", "notes", "guide", "guide"]), ["guide"])

    def test_unique_bookmarks_have_no_duplicates(self):
        self.assertEqual(duplicates(["guide", "notes"]), [])


if __name__ == "__main__":
    unittest.main()
