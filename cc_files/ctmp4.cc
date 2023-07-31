#include <iostream>
#include <cmath>
#include <random>
#include <functional>
#include <cassert>

// Base Monte Carlo Estimator class
class MonteCarloEstimator
{
protected:
    int iterations; // Number of iterations for estimation

public:
    MonteCarloEstimator(int iterations) : iterations(iterations) {}

    // Virtual function to estimate the value
    virtual double estimate() = 0;
};

// Estimator for estimating π using Monte Carlo method
class PiEstimator : public MonteCarloEstimator
{
public:
    PiEstimator(int iterations) : MonteCarloEstimator(iterations) {}

    double estimate() override
    {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_real_distribution<double> dist(-1.0, 1.0);

        int insideCircleCount = 0;
        for (int i = 0; i < iterations; i++)
        {
            double x = dist(gen);
            double y = dist(gen);
            double distanceFromOrigin = std::sqrt(x * x + y * y);
            if (distanceFromOrigin <= 1.0)
            {
                insideCircleCount++;
            }
        }

        return static_cast<double>(insideCircleCount) / iterations * 4.0;
    }
};

// Estimator for finding the area under a curve using Monte Carlo method
class AreaUnderCurveEstimator : public MonteCarloEstimator
{
private:
    std::function<double(double)> curveFunction;
    double min_value, max_value;

public:
    AreaUnderCurveEstimator(int iterations, std::function<double(double)> function,
                            double min_value, double max_value)
        : MonteCarloEstimator(iterations), curveFunction(function), min_value(min_value), max_value(max_value) {}

    double estimate() override
    {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_real_distribution<double> dist(min_value, max_value);

        double sum = 0.0;
        for (int i = 0; i < iterations; i++)
        {
            double x = dist(gen);
            sum += curveFunction(x);
        }

        return sum / iterations * (max_value - min_value);
    }
};

int main()
{
    int iterations = 1000000;

    // Estimating π
    PiEstimator piEstimator(iterations);
    double pi_estimate = piEstimator.estimate();
    std::cout << "Estimated value of π: " << pi_estimate << std::endl;

    // Estimating the area under the curve y = sqrt(4 - x^2) in the range [0, 2]
    auto curveFunction = [](double x)
    { return std::sqrt(4.0 - x * x); };
    AreaUnderCurveEstimator areaEstimator(iterations, curveFunction, 0.0, 2.0);
    double area_estimate = areaEstimator.estimate();
    std::cout << "Estimated area under the curve: " << area_estimate << std::endl;

    return 0;
}
