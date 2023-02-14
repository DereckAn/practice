package RealEstate;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class PropertyTest {

	@Test
	void testGetStreetAddress() {
		Condo c1 = new Condo("Mi casita de amor", 31415, 12.3, 45.6, 3, 1.5, 3, 1);
		Assertions.assertEquals(c1.getStreetAddress(), "Mi casita de amor");
	}

	@Test
	void testGetZip() {
		Condo c1 = new Condo("Mi casita de amor", 31415, 12.3, 45.6, 3, 1.5, 3, 1);
		Assertions.assertEquals(c1.getZip(), 31415);
	}

	@Test
	void testGetListPrice() {
		Condo c1 = new Condo("Mi casita de amor", 31415, 12.3, 45.6, 3, 1.5, 3, 1);
		Assertions.assertEquals(c1.getListPrice(), 12.3);
	}

	@Test
	void testGetApraisalPrice() {
		Condo c1 = new Condo("Mi casita de amor", 31415, 12.3, 45.6, 3, 1.5, 3, 1);
		Assertions.assertEquals(c1.calculateAppraisalPrice(), 39264);
	}

	@Test
	void testSetStreetAddress() {
		Condo c1 = new Condo("Mi casita de amor", 31415, 12.3, 45.6, 3, 1.5, 3, 1);
		c1.setStreetAddress("A la vuelta de la esquina");
		Assertions.assertEquals(c1.getStreetAddress(), "A la vuelta de la esquina");
	}

	@Test
	void testSetZip() {
		Condo c1 = new Condo("Mi casita de amor", 31415, 12.3, 45.6, 3, 1.5, 3, 1);
		c1.setZip(214);
		Assertions.assertEquals(c1.getZip(), 214);
	}

	@Test
	void testSetListPrice() {
		Condo c1 = new Condo("Mi casita de amor", 31415, 12.3, 45.6, 3, 1.5, 3, 1);
		c1.setListPrice(3.1415);
		Assertions.assertEquals(c1.getListPrice(), 3.1415);
	}

	@Test
	void testSetAppraisalPrice() {
		Condo c1 = new Condo("Mi casita de amor", 31415, 12.3, 45.6, 3, 1.5, 3, 1);
		c1.setBeds(5);
		Assertions.assertEquals(c1.calculateAppraisalPrice(), 55264);
	}

	@Test
	void testCalculateAppraisalPrice() {
		Condo c1 = new Condo("Mi casita de amor", 31415, 12.3, 45.6, 3, 1.5, 3, 1);
		Assertions.assertEquals(c1.calculateAppraisalPrice(), 39264);
	}

}
