#include <iostream>
#include <string>
#include <cmath>

int rabin_karp_search(const std::string& text, const std::string& pattern) {
    int d = 256; // Number of possible characters (ASCII range)
    int q = 101; // A prime number for the modulo operation
    int m = pattern.length();
    int n = text.length();
    int p = 0; // Hash value for the pattern
    int t = 0; // Hash value for the first substring of text
    int h = 1;

    // Calculate h as (d^(m-1)) % q
    for (int i = 0; i < m - 1; ++i) {
        h = (h * d) % q;
    }

    // Calculate the hash value for the pattern and the first substring of text
    for (int i = 0; i < m; ++i) {
        p = (d * p + pattern[i]) % q;
        t = (d * t + text[i]) % q;
    }

    // Perform the search
    for (int i = 0; i <= n - m; ++i) {
        // If the hash values match, check for a full match
        if (p == t) {
            int j;
            for (j = 0; j < m; ++j) {
                if (text[i + j] != pattern[j]) {
                    break;
                }
            }
            // If j reaches m, it means the pattern is found starting at index i
            if (j == m) {
                return i;
            }
        }

        // Calculate the hash value for the next substring of text
        if (i < n - m) {
            t = (d * (t - text[i] * h) + text[i + m]) % q;
            // Ensure that t remains positive
            if (t < 0) {
                t += q;
            }
        }
    }

    return -1; // Pattern not found in the text
}

int main() {
    std::string text = "AABAACAADAABAAABAA";
    std::string pattern = "AABA";

    int result = rabin_karp_search(text, pattern);

    if (result != -1) {
        std::cout << "Pattern found at index " << result << std::endl;
    } else {
        std::cout << "Pattern not found in the text." << std::endl;
    }

    return 0;
}
