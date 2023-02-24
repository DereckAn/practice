package Draw;

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
	
	//Landscape Colors
	private final String LIGHT_SKY_BLUE = "87CEFA";
	private final String MIDNIGHT_BLUE = "191970";
	private final String SNOW3 = "CDC9C8";
	private final String WHITE = "FFFFFF";
	private final String MY_WHITE_SMOKE = "F5F5F5";
	private final String LAWN_GREEN = "7CFC00";
	private final String MEDIUM_SPRING_GREEN = "00FA9A";
	private final String SPRING_GREEN = "00FF7F";
	
	//Tree Colors
	private final String BROWN = "A52A2A";
	private final String DARK_GREEN = "006400";
	private final String FOREST_GREEN = "228B22";
	private final String GRAY = "808080";
	private final String GREEN = "008000";
	
	//House Colors
	private final String DARK_SLATE_GRAY = "2F4F4F";
	private final String FIREBRICK = "B22222";
	private final String INDIAN_RED = "CD5C5C";
	private final String MAROON = "800000";
	private final String MOCCASIN = "FFE4B5";
	private final String RED = "FF0000";
	private final String SADDLE_BROWN = "8B4513";
	private final String SIENNA = "A0522D";
	private final String SLATE_GRAY = "708090";
	private final String PERU = "CD853F";
	private final String WHITE_SMOKE = "F5F5F5";
	private final String BURLYWOOD = "DEB887";


	

	public DrawPanel() {
		this.setPreferredSize(new Dimension(1600, 900));	//Sets the dimensions of the DrawPanel.  Change this if your screen doesn't support this size.
		this.setOpaque(true);
		this.setBackground(Color.WHITE);			//Sets the background of the DrawPanel LIGHT_GRAY.  You may change this if desired.
	}
	/**
	 * Overrides the JComponent.paintComponent method.
	 * EVERYTHING that gets drawn to the Component (which sits on the content frame of the JFrame) is drawn in this method.
	 * Draw12b
	 * Draw all your objects here.
	 * Automatically called by the event handler whenever the screen needs to be redrawn.
	 * DO NOT CALL THIS METHOD MANUALLY
	 * 
	 * @param	g	//All drawing in Java must go through a Graphics object
	 */
	public void paintComponent(Graphics g) {
		super.paintComponent(g);
		Graphics2D g2 = (Graphics2D) g;			//Allows us to draw using both the Graphics class methods and the Graphics2D class methods

		g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);	//Makes drawn shapes and fonts clearer

		//DrawTree landscape
		g2.setColor(Color.decode("#" + LIGHT_SKY_BLUE));
		g2.fillRect(0,0,this.getWidth(),this.getHeight());
		
		g2.setColor(Color.decode("#" + LAWN_GREEN));
		g2.fillOval((-600), 350, this.getWidth() + 1200, 700);
		
		//DrawTree Trees
		Tree t1 = new Tree(g2, 50, 400, 1, 3, BROWN , DARK_GREEN);
		t1.draw();
		
		Tree t2 = new Tree(g2, 200, 375, 1, 5, BROWN , GRAY);
		t2.draw();
		
		Tree t3 = new Tree(g2, 300, 450, 1, 4, BROWN , FOREST_GREEN);
		t3.draw();
		
		
		//Populate the scene with your own trees here!
		
		
		
		
		
		
	}//end of method paintComponent(Graphics)

}//end of class DrawPanel