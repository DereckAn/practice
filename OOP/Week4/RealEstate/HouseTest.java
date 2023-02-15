package RealEstate;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class HouseTest {

	@Test
	void testCalculateAppraisalPrice() {
		House h1 = new House("Mi casita de amor", 31415, 12.3, 45.6, 3, 1.5, 3, 1);
//		h1.calculateAppraisalPrice();
		Assertions.assertEquals(h1.calculateAppraisalPrice(), 508291);
	}
	
	@Test
	void testCalculateAppraisalPriceFail() {
		House h1 = new House("Mi casita de amor", 31415, 12.3, 45.6, 3, 1.5, 3, 1);
//		h1.calculateAppraisalPrice();
//		h1.setAppraisalPrice(600000);
		Assertions.assertNotEquals(h1.calculateAppraisalPrice(), 600000);
	}

	@Test
	void testGetYardAcres() {
		House h1 = new House("Mi casita de amor", 31415, 12.3, 45.6, 3, 1.5, 3, 1);
		Assertions.assertEquals(h1.getYardAcres(), 1);
	}

	@Test
	void testSetYardAcres() {
		House h1 = new House("Mi casita de amor", 31415, 12.3, 45.6, 3, 1.5, 3, 1);
		h1.setYardAcres(4);
		Assertions.assertEquals(h1.getYardAcres(), 4);
	}

}
