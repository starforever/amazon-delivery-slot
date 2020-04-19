from unittest import TestCase

from delivery_slot_checker_amazon_fresh import check_delivery_slot


class DeliverySlotCheckerAmazonFreshTest(TestCase):
    def test_check_delivery_slot(self):
        with open(
            "delivery_slot_page_source/amazon_fresh_no.htm"
        ) as page_source_file:
            page_source = page_source_file.read()
        self.assertFalse(check_delivery_slot(page_source))
