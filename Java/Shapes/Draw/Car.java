package Draw;

import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.Polygon;
import java.awt.geom.AffineTransform;
import java.awt.geom.Rectangle2D;
import java.awt.geom.RoundRectangle2D;

public class Car extends LandscapeObject {
	private String carColor;
	private String windowColor;
	private int bodyX = 85;
	private int bodyY = bodyX/3;
	private int rueda = bodyY;
	private int door = bodyY/2;
	private int roofY = bodyY-(bodyY/4);
	private int roofX = bodyX/2;
	
	

	public Car(Graphics2D g2, int x, int y, double scale, String carColor,String windowColor) {
		super(g2, x, y, scale);
		this.carColor = "#" + carColor;
		this.windowColor = "#" + windowColor;

	}

	@Override
	public void draw() {
		applyScale();
		car();
		roof();
		ruedas();
		door();
		details();
	}

	@Override
	public void applyScale() {
		bodyX *= super.getScale();
		bodyY *= super.getScale();
		rueda *= super.getScale();
		door *= super.getScale();
		roofY *= super.getScale();
		roofX *= super.getScale();	
	}
	
	private void car(){
//		g2.setColor(Color.decode(carColor));
//		Rectangle2D.Double car = new Rectangle2D.Double(currentX , currentY, bodyX, bodyY);
//		g2.draw(car);
//		g2.fill(car);
		g2.setColor(Color.decode(carColor));
		var car = new RoundRectangle2D.Double(currentX, currentY, bodyX, bodyY, 15, 15);
		g2.fill(car);
	}
	
	private void roof(){
		AffineTransform origenC = g2.getTransform();
		g2.setColor(Color.decode(carColor));
		g2.translate(currentX, currentY);
		g2.fillRect((bodyX/2)-(roofX/2), -roofY, roofX, roofY );
		g2.setTransform(origenC);
	}
	
	private void ruedas() {
		AffineTransform origenC = g2.getTransform();
		g2.translate(currentX, currentY);
		g2.setColor(Color.BLACK	);
		g2.fillOval((bodyX/11), 2*(bodyY/3), rueda, rueda);
		g2.fillOval(6*(bodyX/10), 2*(bodyY/3), rueda, rueda);
		g2.setTransform(origenC);
	}
	
	private void door() {
		AffineTransform origenC = g2.getTransform();
		g2.translate(currentX, currentY);
		g2.setColor(Color.black);
		var puerta = new RoundRectangle2D.Double((bodyX/2)-(roofX/2), -(door), door, door+(door), 15, 15);
		g2.draw(puerta);
		g2.fillOval(3*(bodyX/10), 0, rueda/10, rueda/10);
		g2.fillRect(3*(bodyX/10), 0, rueda/5, rueda/16);
		g2.setTransform(origenC);
	}
	
	private void details() {
		AffineTransform origenC = g2.getTransform();
		g2.translate(currentX, currentY);
		g2.setColor(Color.yellow); // luz
		g2.fillOval(bodyX-(bodyX/15), 0, rueda/5, rueda/5);
		
		g2.setColor(Color.decode(carColor)); //Escape
		g2.fillRect(-(bodyX/10), bodyY-(rueda/3), rueda/2, rueda/3);
		
		g2.setColor(Color.decode("000")); // boca del escape
		g2.fillRect(-(bodyX/10), bodyY-(rueda/3), rueda/10, rueda/3);
		
		g2.setColor(Color.decode(windowColor));  //ventana intento
		g2.fillRect(bodyX/2, -(roofY), roofY, roofY);
		
		g2.setColor(Color.decode("#C0C0C0")); // rines
		g2.fillOval((bodyX/11)+(rueda/3), 2*(bodyY/3)+rueda/3, rueda/3, rueda/3);
		g2.fillOval(6*(bodyX/10)+(rueda/3), 2*(bodyY/3)+rueda/3, rueda/3, rueda/3);
		
		g2.setTransform(origenC);
		
	}

}
