## Coin Change Problem : Minimun number of coins for sum

### Problem:

Given a list of N coins, their values (V1, V2, … , VN), and the total sum S. Find the minimum number of coins the sum of which is S (we can use as many coins of one type as we want), or report that it’s not possible to select coins in such a way that they sum up to S.

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
