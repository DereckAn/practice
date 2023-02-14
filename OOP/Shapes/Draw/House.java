package Draw;

import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.Polygon;
import java.awt.geom.AffineTransform;
import java.awt.geom.Rectangle2D;

public class House extends LandscapeObject {
	private int houseBody = 100; //100
	private int roofBase = 150;  //150
	private int roofHeight = roofBase/2;
	private int doorx = houseBody/3;
	private int doory = houseBody/2;
	private int chimex = roofHeight/5;
	private int chimey = roofHeight/3;
	private int window = houseBody/4;
	private int roundWindw = roofBase/4;
	private String houseColor;
	private String roofColor;
//	private String windowColor = "#white";
//	private String doorColor = "#BROWN";
	private BasicStroke houseStroke = new BasicStroke(1);

	public House(Graphics2D g2, int x, int y, double scale,String s_houseColor, String s_roofColor) {
		super(g2, x, y, scale);
		this.houseColor = "#" + s_houseColor;
		this.roofColor = "#" + s_roofColor;
		// TODO Auto-generated constructor stub
	}

	@Override
	public void draw() {
		applyScale();
		house();
		roof();
		roundWindow();
		door();
		window();
		chimenea();
		
	}

	@Override
	public void applyScale() {
		houseBody *= super.getScale();
		roofBase *= super.getScale();
		roofHeight *= super.getScale();
		doorx *= super.getScale();
		doory *= super.getScale();
		chimex *= super.getScale();
		chimey *= super.getScale();
		window *= super.getScale();
		roundWindw *= super.getScale();
	}
	
	private void house(){
//		g2.setStroke(houseStroke);
		g2.setColor(Color.decode(houseColor));
		Rectangle2D.Double housw = new Rectangle2D.Double(currentX + (roofBase/6), 
				currentY + (roofHeight), 
				houseBody, houseBody);
		g2.draw(housw);
		g2.fill(housw);
		
//		int[] xpoints = {850, 850, 1050, 1050};
//		int[] ypoints = {400, 600, 600, 400};
//		g2.fillPolygon(xpoints, ypoints, 4);
		
	}
	
	private void chimenea() {
		
		AffineTransform origenC = g2.getTransform();
		g2.setStroke(new BasicStroke(4));
//		g2.setStroke(houseStroke);
		g2.setColor(Color.decode("#283747"));
		g2.translate(currentX, currentY);
		g2.fillRect( roofBase/6, roofHeight/2, chimex,chimey );		
		g2.setTransform(origenC);
		
	}
	
	private void roof() {
		AffineTransform origenC = g2.getTransform();
		g2.setStroke(houseStroke);
		g2.setColor(Color.decode(roofColor));
		g2.translate(currentX, currentY);
		Polygon roof = new Polygon(new int[]{0, roofBase/2, roofBase}, new int[]{roofHeight, 0, roofHeight}, 3);
		g2.fillPolygon(roof);
		g2.setTransform(origenC);
	}
	
	private void roundWindow() {
		AffineTransform origenC = g2.getTransform();
		g2.setStroke(houseStroke);
		g2.setColor(Color.decode("#12E3D2"));
		g2.translate(currentX, currentY);
		g2.fillOval((roofBase/2)-(roundWindw/2), (roofHeight/2)-(roundWindw/2), roundWindw,roundWindw );
		
		g2.setColor(Color.decode(roofColor));
		
		g2.fillRect((roofBase/2)-(roundWindw/2),(roofHeight/2) - (roundWindw/10)/2, roundWindw, roundWindw/10 );
		
		g2.fillRect((roofBase/2) - (roundWindw/10)/2,(roofHeight/2)-(roundWindw/2), roundWindw/10, roundWindw );
		
		g2.setTransform(origenC);
	}
	
	private void door() {
		AffineTransform origenC = g2.getTransform();
//		g2.setStroke(houseStroke);
		g2.setColor(Color.decode("#283747"));
		g2.translate(currentX, currentY);
		g2.fillRect((roofBase/2)+(roofBase/13), ((roofHeight + houseBody)/2)+(((roofHeight + houseBody)/2)-doory), doorx,doory );
		
		g2.setColor(Color.decode("#B33CB8"));
		g2.fillOval((roofBase/2)+(roofBase/13)+(doorx/6), 
				((roofHeight + houseBody)/2)+(((roofHeight + houseBody)/2)-doory) + (doory/2), 
				roundWindw/7, roundWindw/7);
		
		g2.setTransform(origenC);
	}
	
	private void window() {
		AffineTransform origenC = g2.getTransform();
		g2.setColor(Color.decode("#CBC122"));
		g2.translate(currentX, currentY);
		g2.fillRect((roofBase/2)-(roofBase/4), ((roofHeight + houseBody)/2), window,window );
		
		g2.setColor(Color.decode(houseColor));
		
		g2.fillRect((roofBase/2)-(roofBase/4), 
				((roofHeight + houseBody)/2) + ((window/2)-(window/13)) 
				, window, window/10 );
		
		g2.fillRect((roofBase/2)-(roofBase/4)+((window/2)-(window/20)), 
				((roofHeight + houseBody)/2), 
				window/10, window );
		
		g2.setTransform(origenC);
		
	}
	

}
