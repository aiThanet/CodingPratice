## Coin Change Problem : Minimun number of coins for sum

### Solution 1:

```
let s <= SUM
for each coin_i <= s
   Let m = minimum number of coins for s-coin_i
   minimum of coins to sum s = min(m+1,current minimum of coins to sum s)

   #additional: which coins use to total the sum
```

### Solution 2:

```
let s <= SUM
for each coin_i
   update the best solution that found for s + coin_i so
   minimum of coins to sum(s + coin_i) = min(current minimum of coins to sum (s + coin_i), minimum of coins to sum(s) + 1)
```

### References

[click here](https://medium.com/@neroxiao/dynamic-programming-problems-e00d7f7cf1d6)
