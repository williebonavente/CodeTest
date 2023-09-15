import javax.swing.*;
import java.awt.*;
import java.awt.geom.Path2D;

public class KochSnowflake extends JPanel {

    private int depth;

    public KochSnowflake(int depth) {
        this.depth = depth;
        setPreferredSize(new Dimension(800, 800));
    }

    private void drawKochSnowflake(Graphics2D g2, int depth, Point2D p1, Point2D p2) {
        if (depth == 0) {
            g2.drawLine((int) p1.getX(), (int) p1.getY(), (int) p2.getX(), (int) p2.getY());
        } else {
            double deltaX = p2.getX() - p1.getX();
            double deltaY = p2.getY() - p1.getY();

            Point2D p3 = new Point2D.Double(p1.getX() + deltaX / 3, p1.getY() + deltaY / 3);
            Point2D p4 = new Point2D.Double(p1.getX() + deltaX / 2 + deltaY * Math.sqrt(3) / 6, p1.getY() + deltaY / 2 - deltaX * Math.sqrt(3) / 6);
            Point2D p5 = new Point2D.Double(p1.getX() + 2 * deltaX / 3, p1.getY() + 2 * deltaY / 3);

            drawKochSnowflake(g2, depth - 1, p1, p3);
            drawKochSnowflake(g2, depth - 1, p3, p4);
            drawKochSnowflake(g2, depth - 1, p4, p5);
            drawKochSnowflake(g2, depth - 1, p5, p2);
        }
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2 = (Graphics2D) g;
        g2.setColor(Color.BLACK);

        int sideLength = 600;
        int centerX = getWidth() / 2;
        int centerY = getHeight() / 2;

        Point2D p1 = new Point2D.Double(centerX - sideLength / 2, centerY + Math.sqrt(3) * sideLength / 6);
        Point2D p2 = new Point2D.Double(centerX + sideLength / 2, centerY + Math.sqrt(3) * sideLength / 6);
        Point2D p3 = new Point2D.Double(centerX, centerY - Math.sqrt(3) * sideLength / 3);

        Path2D path = new Path2D.Double();
        path.moveTo(p1.getX(), p1.getY());
        path.lineTo(p2.getX(), p2.getY());
        path.lineTo(p3.getX(), p3.getY());
        path.closePath();

        drawKochSnowflake(g2, depth, p1, p2);
        drawKochSnowflake(g2, depth, p2, p3);
        drawKochSnowflake(g2, depth, p3, p1);
    }

    public static void main(String[] args) {
        int depth = 4; // Change the depth to control the level of detail in the snowflake
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Koch Snowflake Fractal");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.add(new KochSnowflake(depth));
            frame.pack();
            frame.setLocationRelativeTo(null);
            frame.setVisible(true);
        });
    }
}
