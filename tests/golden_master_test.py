import unittest

from src.gilded_rose import GildedRose, Item

class GoldenMasterTest(unittest.TestCase):

    def test_update_items(self):
        items = [
            Item(name="4 Pints of Milk", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Fabergé egg", sell_in=0, quality=80),
            Item(name="Fabergé egg", sell_in=-1, quality=80),
            Item(name="Backstage passes to a Coldplay concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a Coldplay concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a Coldplay concert", sell_in=5, quality=49),
            Item(name="Lemon Drizzle Cake", sell_in=3, quality=6),
        ]

        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        self.assertEqual(
            str(gilded_rose.items),
            "[4 Pints of Milk, 9, 19, Aged Brie, 1, 1, Elixir of the Mongoose, 4, 6, Fabergé egg, 0, "
            "80, Fabergé egg, -1, 80, Backstage passes to a Coldplay concert, 14, 21, "
            "Backstage passes to a Coldplay concert, 9, 50, Backstage passes to a Coldplay concert, 4, 50, "
            "Lemon Drizzle Cake, 2, 5]"
        )

        for _ in range(10):
            gilded_rose.update_quality()

        self.assertEqual(
            str(gilded_rose.items),
            "[4 Pints of Milk, -1, 8, Aged Brie, -9, 20, Elixir of the Mongoose, -6, 0, Fabergé egg, "
            "0, 80, Fabergé egg, -1, 80, Backstage passes to a "
            "Coldplay concert, 4, 38, Backstage passes to a Coldplay concert, -1, 0, "
            "Backstage passes to a Coldplay concert, -6, 0, Lemon Drizzle Cake, -8, 0]"
        )


if __name__ == "__main__":
    unittest.main()