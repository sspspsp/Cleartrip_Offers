from POM.offers_hotels import HotelOffers

class TestHotelOffers:
    def test_hoteloffers(self,_driver):
        obj = HotelOffers(_driver)
        obj.cancel_popup()
        obj.click_offers()
        obj.click_hotels()
        obj.know_more()
        obj.book_now()
        obj.reset_filters()