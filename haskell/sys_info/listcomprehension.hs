-- Generate a list of even numbers from 1 to 10
evens :: [Int]
evens = [x | x <- [1..10], x `mod` 2 == 0]
