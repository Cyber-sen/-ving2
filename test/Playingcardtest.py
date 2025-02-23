import unittest
# If PlayingCard is defined in another module, import it like:
# from your_module_name import PlayingCard

class PlayingCard:
    """
    A class to represent a playing card.
    """
    def __init__(self, suit, face):
        if suit not in ['H', 'D', 'C', 'S']:
            raise ValueError("Parameter suit must be one of H, D, C or S")
        if not (1 <= face <= 13):
            raise ValueError("Parameter face must be a number between 1 to 13")
        self.suit = suit
        self.face = face

    def get_as_string(self):
        return f"{self.suit}{self.face}"

    def get_suit(self):
        return self.suit

    def get_face(self):
        return self.face

    def __eq__(self, other):
        if isinstance(other, PlayingCard):
            return self.suit == other.suit and self.face == other.face
        return False

    def __hash__(self):
        return hash((self.suit, self.face))


class TestPlayingCard(unittest.TestCase):

    def test_valid_init(self):
        """Test that valid suit and face values create a PlayingCard successfully."""
        card = PlayingCard('H', 1)
        self.assertEqual(card.suit, 'H')
        self.assertEqual(card.face, 1)

    def test_invalid_suit(self):
        """Test that initializing a card with an invalid suit raises a ValueError."""
        with self.assertRaises(ValueError):
            PlayingCard('X', 5)  # 'X' is not in ['H', 'D', 'C', 'S']

    def test_invalid_face_low(self):
        """Test that initializing a card with a face value too low raises a ValueError."""
        with self.assertRaises(ValueError):
            PlayingCard('H', 0)  # 0 is out of range

    def test_invalid_face_high(self):
        """Test that initializing a card with a face value too high raises a ValueError."""
        with self.assertRaises(ValueError):
            PlayingCard('D', 14)  # 14 is out of range

    def test_get_as_string(self):
        """Test the string representation of the card."""
        card = PlayingCard('C', 13)
        self.assertEqual(card.get_as_string(), "C13",
                         "get_as_string should return 'C13' for suit=C, face=13.")

    def test_get_suit(self):
        """Test that get_suit returns the correct suit."""
        card = PlayingCard('S', 7)
        self.assertEqual(card.get_suit(), 'S',
                         "get_suit should return 'S' for a spade card.")

    def test_get_face(self):
        """Test that get_face returns the correct face value."""
        card = PlayingCard('H', 10)
        self.assertEqual(card.get_face(), 10,
                         "get_face should return 10 for this card.")

    def test_eq_same_card(self):
        """Test that two cards with the same suit and face are considered equal."""
        card1 = PlayingCard('D', 5)
        card2 = PlayingCard('D', 5)
        self.assertEqual(card1, card2, "Cards with same suit and face should be equal.")

    def test_eq_different_suit(self):
        """Test that two cards with different suits are not considered equal."""
        card1 = PlayingCard('D', 5)
        card2 = PlayingCard('H', 5)
        self.assertNotEqual(card1, card2, 
                            "Cards with different suits should not be equal.")

    def test_eq_different_face(self):
        """Test that two cards with different faces are not considered equal."""
        card1 = PlayingCard('C', 4)
        card2 = PlayingCard('C', 5)
        self.assertNotEqual(card1, card2, 
                            "Cards with different faces should not be equal.")

    def test_eq_non_card(self):
        """Test that comparing a PlayingCard to a non-PlayingCard object returns False."""
        card = PlayingCard('S', 9)
        self.assertNotEqual(card, "NotACard",
                            "Comparing to a non-card object should return False.")

    def test_hash_equal_cards(self):
        """Test that two equal cards produce the same hash."""
        card1 = PlayingCard('H', 12)
        card2 = PlayingCard('H', 12)
        self.assertEqual(hash(card1), hash(card2),
                         "Equal cards should have the same hash.")

    def test_hash_different_cards(self):
        """Test that two different cards produce different hashes."""
        card1 = PlayingCard('S', 1)
        card2 = PlayingCard('S', 2)
        self.assertNotEqual(hash(card1), hash(card2),
                            "Different cards should have different hashes.")


if __name__ == '__main__':
    unittest.main()
