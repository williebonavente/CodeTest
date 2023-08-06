import math


def bilateral_filter(image, spatial_sigma, range_sigma):
    filtered_image = image.copy()
    height, width = image.shape

    for x in range(width):
        for y in range(height):
            pixel_value = 0
            weight_sum = 0

            for i in range(-2, 3):
                for j in range(-2, 3):
                    if 0 <= x + i < width and 0 <= y + j < height:
                        spatial_diff = (i ** 2 + j ** 2) / (2 * spatial_sigma ** 2)
                        range_diff = (image[y, x] - image[y + j, x + i]) ** 2 / (2 * range_sigma ** 2)
                        weight = math.exp(-spatial_diff - range_diff)

                        pixel_value += image[y + j, x + i] * weight
                        weight_sum += weight

            filtered_image[y, x] = pixel_value / weight_sum

    return filtered_image
