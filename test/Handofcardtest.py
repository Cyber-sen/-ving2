import unittest

# Mock PlayingCard class for testing (you can replace this with your real PlayingCard class)
class MockPlayingCard:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def get_suit(self):
        return self.suit
    
    def get_as_string(self):
        return f"{self.value}{self.suit}"

# Import your actual HandOfCards class here.
# Example: 
# from your_module_name import HandOfCards
# For demonstration, I'll redefine the HandOfCards class as given in your question:
class HandOfCards:
    """
    A class to represent a hand of playing cards.
    """
    def __init__(self, cards):
        self.cards = cards

    def is_flush(self):
        if len(self.cards) < 5:
            return False
        
        first_suit = self.cards[0].get_suit()
        return all(card.get_suit() == first_suit for card in self.cards)

    def __str__(self):
        return ', '.join(card.get_as_string() for card in self.cards)


class TestHandOfCards(unittest.TestCase):

    def setUp(self):
        # Create some mock cards for the tests
        self.spade_cards = [
            MockPlayingCard('S', 1),
            MockPlayingCard('S', 2),
            MockPlayingCard('S', 3),
            MockPlayingCard('S', 4),
            MockPlayingCard('S', 5)
        ]
        self.mixed_cards = [
            MockPlayingCard('S', 1),
            MockPlayingCard('H', 2),
            MockPlayingCard('S', 3),
            MockPlayingCard('S', 4),
            MockPlayingCard('S', 5)
        ]
        self.four_cards = [
            MockPlayingCard('S', 1),
            MockPlayingCard('S', 2),
            MockPlayingCard('S', 3),
            MockPlayingCard('S', 4)
        ]

    def test_is_flush_true(self):
        """Test is_flush returns True if all 5 cards share the same suit."""
        hand = HandOfCards(self.spade_cards)
        self.assertTrue(hand.is_flush(), 
                        "Hand with five spade cards should be a flush.")

    def test_is_flush_false_mixed_suits(self):
        """Test is_flush returns False if at least one card has a different suit."""
        hand = HandOfCards(self.mixed_cards)
        self.assertFalse(hand.is_flush(), 
                         "Hand with mixed suits should not be a flush.")

    def test_is_flush_false_less_than_5_cards(self):
        """Test is_flush returns False when there are fewer than 5 cards."""
        hand = HandOfCards(self.four_cards)
        self.assertFalse(hand.is_flush(), 
                         "Hand with fewer than 5 cards should not be a flush.")

    def test_str_representation(self):
        """Test the string representation of the hand."""
        hand = HandOfCards(self.spade_cards)
        hand_str = str(hand)
        self.assertIsInstance(hand_str, str, 
                              "__str__ method should return a string.")
        # Check if it contains all the expected card representations
        for card in self.spade_cards:
            self.assertIn(card.get_as_string(), hand_str, 
                          "String representation should contain each card's string.")

    def test_cards_attribute(self):
        """Test that the cards attribute is correctly assigned."""
        hand = HandOfCards(self.spade_cards)
        self.assertEqual(hand.cards, self.spade_cards, 
                         "The hand's cards should match the cards passed to the constructor.")


if __name__ == '__main__':
    unittest.main()
