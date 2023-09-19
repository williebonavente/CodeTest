c1 = 'a'
println(c1)
# the ascii value of a char can be found with Int():
println(c1, " ascii value = ", Int(c1))
#> a ascii value = 97
println("Int('α') == ", Int('α'))
#> Int('α') == 945