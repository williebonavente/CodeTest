public class FastInverseSquareRoot {
    public static void main(String[] args) {
        float x = 4.0f; // Replace with the desired value

        float result = fastInverseSqrt(x);
        System.out.println("Fast Inverse Square Root of " + x + " is approximately " + result);
    }

    public static float fastInverseSqrt(float x) {
        float xhalf = 0.5f * x;
        int i = Float.floatToIntBits(x); // Convert float to 32-bit integer
        i = 0x5f3759df - (i >> 1); // Initial guess using magic number
        x = Float.intBitsToFloat(i); // Convert back to float

        x = x * (1.5f - xhalf * x * x); // Newton-Raphson iteration
        return x;
    }
}
