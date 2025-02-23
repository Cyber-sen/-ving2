import unittest
import random
import sys, os
sys.path.append("src")
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src')))
from DeckOfCards import DeckOfCards, HandOfCards, PlayingCard







class TestDeckOfCards(unittest.TestCase):
    def setUp(self):
        """Create a fresh DeckOfCards instance before each test."""
        self.deck = DeckOfCards()

    def test_deck_initialization(self):
        """Test that a new deck has exactly 52 cards."""
        self.assertEqual(len(self.deck.cards), 52, 
                         "A new deck should contain 52 cards.")

        # Optional: Check that each card is an instance of PlayingCard
        for card in self.deck.cards:
            self.assertIsInstance(card, PlayingCard, 
                                  "Each card in the deck should be a PlayingCard instance.")

    def test_deal_hand_valid(self):
        """Test that dealing a valid number of cards returns a HandOfCards with the correct count."""
        n = 5
        hand = self.deck.deal_hand(n)
        self.assertIsInstance(hand, HandOfCards, 
                              "deal_hand should return a HandOfCards instance.")
        self.assertEqual(len(hand.cards), n, 
                         f"Hand should contain {n} cards.")

    def test_deal_hand_invalid_zero(self):
        """Test that dealing an invalid number of cards (0) raises a ValueError."""
        with self.assertRaises(ValueError, 
                               msg="Dealing 0 cards should raise ValueError."):
            self.deck.deal_hand(0)

    def test_deal_hand_invalid_above_52(self):
        """Test that dealing an invalid number of cards (more than 52) raises a ValueError."""
        with self.assertRaises(ValueError, 
                               msg="Dealing more than 52 cards should raise ValueError."):
            self.deck.deal_hand(53)

    def test_deck_integrity_after_deal(self):
        """
        Test that dealing a hand doesn't remove cards from the deck 
        (since random.sample is used, the deck should remain unchanged).
        """
        original_deck_size = len(self.deck.cards)
        _ = self.deck.deal_hand(5)  # Dealing 5 cards
        self.assertEqual(len(self.deck.cards), original_deck_size, 
                         "The deck size should remain 52 after dealing because random.sample does not remove cards.")

    def test_str_representation(self):
        """Test the string representation of the deck."""
        deck_str = str(self.deck)
        self.assertIsInstance(deck_str, str, 
                              "The __str__ method should return a string.")
        # A minimal check: the representation should list all 52 cards in some form
        # For instance, it might contain commas (one for each card except maybe the last).
        # This check can be adapted to your actual string format.
        self.assertTrue(len(deck_str) > 0, 
                        "String representation should not be empty.")
        # Optionally, you could check that there are 51 commas if you want to be strict:
        # self.assertEqual(deck_str.count(','), 51)

if __name__ == '__main__':
    unittest.main()
