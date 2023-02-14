/**
 * class name: DrawPanel.java
 * Assignment: Lab12a
 * Lessons Learned: Create a new shapes taking inmind its color, rotation, and number of sides. 
 * Ex. Packing Lists or Shopping Lists. 
 * @author Dereck Angeles
 * @since 11/30/2022
 */
package Draw12a;

import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Polygon;
import java.awt.RenderingHints;
import java.awt.Stroke;
import javax.swing.JPanel;
import java.awt.geom.*;

/**
 * Class used to create a DrawPanel where shapes will be drawn by the programmer (via code).
 * 
 * @author Jared N. Plumb
 * @version 1.0
 * @since 2019-11-26
 * @Minor modifications by Jeff Light
 * @since 2019-12-01
 */
public class DrawPanel extends JPanel {
	//Attributes
	private static final long serialVersionUID = 6311020027600344213L;

	public DrawPanel() {
		this.setPreferredSize(new Dimension(1600, 900));	//Sets the dimensions of the DrawPanel.  Change this if your screen doesn't support this size.
		this.setOpaque(true);
		this.setBackground(Color.WHITE);			//Sets the background of the DrawPanel LIGHT_GRAY.  You may change this if desired.
	}
	
	
	/**
	 * Overrides the JComponent.paintComponent method.
	 * EVERYTHING that gets drawn to the Component (which sits on the content frame of the JFrame) is drawn in this method.
	 * Draw12a
	 * Draw all your objects in the paintComponent method.
	 * Automatically called by the event handler whenever the screen needs to be redrawn.
	 * DO NOT CALL THIS METHOD MANUALLY
	 * 
	 * @param	g	//All drawing in Java must go through a Graphics object
	 */
	public void paintComponent(Graphics g) {
		super.paintComponent(g);
		Graphics2D g2 = (Graphics2D) g;			//Allows us to draw using both the Graphics class methods and the Graphics2D class methods

		g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);	//Makes drawn shapes and fonts clearer
		
		/*
		 * Use this section to write your code.
		 * DrawShapes
		 * Draw at least 6 shapes in BOTH draw and fill formats using methods found in the Graphics class and/or the Graphics2D class.
		 * In other words, if you draw an empty rectangle, you should also draw a filled rectangle.  That counts as one (1) shape.
		 * The empty and filled versions of the shape should be at different orientations.
		 * One of the shapes MUST be a triangle.
		 * Each shape should be a different color.  An empty and a filled rectangle may be the same color, but they must be a different color from an empty and filled triangle.
		 * At least one of the colors should NOT be a standard color from the COLOR palette.
		 * Each empty shape should have a different stroke size.
		 * Be sure all shapes are located such that they can all be seen.
		 */
		
		// Draw rectangle
		g2.setColor(Color.RED);
		g2.setStroke(new BasicStroke(1));
		g2.drawRect(50, 50, 200, 100);
		g2.fillRect(300, 50, 100, 200);


		//Draw12a a triangle
		g2.setColor(Color.BLUE);
		g2.setStroke(new BasicStroke(3));
		int[] xPoints1 = {1000, 1100, 1200}; //Define the x cords for each point
		int[] yPoints1 = {250, 50, 250}; //Define the y cords for each point
		g2.drawPolygon(xPoints1, yPoints1, 3);
		
		//Draw12a a triangle
		g2.setColor(Color.BLUE);
		g2.setStroke(new BasicStroke(3));
		int[] xPoints11 = {1300, 1500, 1300}; //Define the x cords for each point
		int[] yPoints11 = {50, 150, 250}; //Define the y cords for each point
		g2.fillPolygon(xPoints11, yPoints11, 3);

		//Create a rounded rectangle object and draw it
		g2.setColor(Color.decode("#008a2e"));
		g2.setStroke(new BasicStroke(4));
		var emptyRR = new RoundRectangle2D.Double(50, 350, 200, 100, 30, 30);
		g2.draw(emptyRR);
		
		//Create a rounded rectangle object and draw it
		g2.setColor(Color.decode("#008a2e"));
		g2.setStroke(new BasicStroke(4));
		var emptyRRr = new RoundRectangle2D.Double(250, 400, 100, 200, 30, 30);
		g2.fill(emptyRRr);
				
		// Draw a circle
		g2.setColor(Color.GREEN);
		g2.drawOval(450, 400, 150, 150);
		
		// Draw a filled circle
		g2.setColor(Color.GREEN);
		g2.fillOval(650, 400, 150, 150);
		
		// Draw an Oval
		g2.setColor(Color.decode("#12E3D2"));
		g2.drawOval(450, 100, 300, 150);
		
		// Draw an Oval
		g2.setColor(Color.decode("#12E3D2"));
		g2.fillOval(800, 40, 150, 300);
		
		// Draw square
		g2.setColor(Color.pink);
		int[] xpoints = {850, 850, 1050, 1050};
		int[] ypoints = {400, 600, 600, 400};
		g2.drawPolygon(xpoints, ypoints, 4);
		
		// Draw square
		g2.setColor(Color.pink);
		int[] xpoints1 = {1150, 1250, 1350, 1250};
		int[] ypoints1 = {500, 400, 500, 600};
		g2.fillPolygon(xpoints1, ypoints1, 4);
		
		

		
	}//end of method paintComponent(Graphics)

}//end of class DrawPanel