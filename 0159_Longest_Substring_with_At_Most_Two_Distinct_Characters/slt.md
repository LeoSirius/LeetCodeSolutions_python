### 思路1

用hashmap来保存字符和其出现的次数。


"eceba"

然后如果 HashMap 中的映射数量超过两个的时候，我们需要删掉一个映射，比如此时 HashMap 中e有2个，c有1个，此时把b也存入了 HashMap，那么就有三对映射了，这时我们的 left 是0，先从e开始，映射值减1，此时e还有1个，不删除，left 自增1。这时 HashMap 里还有三对映射，此时 left 是1，那么到c了，映射值减1，此时c映射为0，将c从 HashMap 中删除，left 自增1，然后我们更新结果为 i - left + 1，以此类推直至遍历完整个字符串

e 2
c 1