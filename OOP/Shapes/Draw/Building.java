package Draw;

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.Polygon;
import java.awt.geom.AffineTransform;
import java.awt.geom.Rectangle2D;
import java.awt.geom.RoundRectangle2D;

public class Building extends LandscapeObject {
	private String buildingColor;
	private String windowColor;
	private int floors;
	private int buildY = 100;
	private int buildX = buildY/2;
	private int window = buildY/3;
	private int doorX = buildY/3;
	private int doorY = buildY/2;
	private int di = 10;
	

	public Building(Graphics2D g2, int x, int y, double scale, int floors, String buildingColor, String windowColor) {
		super(g2, x, y, scale);
		this.buildingColor = "#" + buildingColor;
		this.windowColor = "#" + windowColor;
		this.floors = floors;
	}

	@Override
	public void draw() {
		applyScale();
		buidling();
		door();
		windows();
		floors();
	}

	@Override
	public void applyScale() {
		buildX *= super.getScale();
		buildY *= super.getScale();
		window *= super.getScale();
		doorX *= super.getScale();
		doorY *= super.getScale();
		di *= super.getScale();
	}
	
	private void buidling() {
		g2.setColor(Color.decode(buildingColor));
		Rectangle2D.Double build = new Rectangle2D.Double(currentX,	currentY, buildY, buildY);
		g2.fill(build);
	}
	
	private void door() {
		AffineTransform origenC = g2.getTransform();
		g2.setColor(Color.decode(windowColor));
		g2.translate(currentX, currentY);
		g2.fillRect((buildY/2)-(doorX/2), buildY-doorY, doorX,doorY );
		g2.setTransform(origenC);
	}
	
	private void windows() { 
		AffineTransform origenC = g2.getTransform();
		g2.setColor(Color.decode("000"));
		g2.translate(currentX, currentY);
		g2.fillRect((buildY-window-di), di , window,window );
		g2.fillRect( di, di , window,window );
		
		g2.setColor(Color.decode(buildingColor));
		g2.fillRect(di,(window/2)+(di)-(window/20),window, window/10);
		g2.fillRect((buildY-window-di),(window/2)+(di)-(window/20),window, window/10);
		g2.fillRect(di+ (window/2) - (window/20),di,window/10, window);
		g2.fillRect(((buildY)-(window/2)-di- (window/20)), di, window/10, window);
		
		g2.setTransform(origenC);
	}
	
	private void floors() {
		AffineTransform origen_AT = g2.getTransform(); 
		for (int t = 0; t < floors; t++) {
			g2.setColor(Color.decode(buildingColor)); 
			g2.translate(currentX, currentY);
			currentY -= (50 * super.getScale()); 
			g2.fillRect(0, -buildX, buildY, buildX );
			
					
			g2.setColor(Color.decode("#F4D03F"));
			g2.fillRect( di, -buildX + di , window,window );
			g2.fillRect((buildY-window-di), -buildX + di , window,window );
			
			g2.setColor(Color.decode(buildingColor));
			g2.fillRect(di,-buildX +(window/2)+(di)-(window/20),window, window/10);
			g2.fillRect((buildY-window-di),-buildX +(window/2)+(di)-(window/20),window, window/10);
			
			g2.fillRect(di+ (window/2) - (window/20),-buildX + di,window/10, window);
			g2.fillRect(((buildY)-(window/2)-di- (window/20)), -buildX + di, window/10, window);

			
			g2.setTransform(origen_AT);
		}
		
	}

}
