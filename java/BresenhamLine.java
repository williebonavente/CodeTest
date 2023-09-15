import java.awt.*;
import java.awt.image.BufferedImage;
import javax.swing.*;

public class BresenhamLine extends JPanel {

    private BufferedImage canvas;

    public BresenhamLine(int width, int height) {
        canvas = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
        drawLine(20, 20, 250, 100);
    }

    private void setPixel(int x, int y, Color color) {
        canvas.setRGB(x, y, color.getRGB());
    }

    private void drawLine(int x1, int y1, int x2, int y2) {
        int dx = Math.abs(x2 - x1);
        int dy = Math.abs(y2 - y1);

        int sx = (x1 < x2) ? 1 : -1;
        int sy = (y1 < y2) ? 1 : -1;

        int err = dx - dy;
        int err2;

        while (true) {
            setPixel(x1, y1, Color.BLACK);

            if (x1 == x2 && y1 == y2) {
                break;
            }

            err2 = 2 * err;

            if (err2 > -dy) {
                err -= dy;
                x1 += sx;
            }

            if (err2 < dx) {
                err += dx;
                y1 += sy;
            }
        }
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.drawImage(canvas, 0, 0, this);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Bresenham's Line Algorithm");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.add(new BresenhamLine(300, 200));
            frame.pack();
            frame.setLocationRelativeTo(null);
            frame.setVisible(true);
        });
    }
}
