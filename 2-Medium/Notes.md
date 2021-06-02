~~~
2/6/21
One of the weirdest things I've noticed has been dot references outperforming non-dot references. This also includes var = var2 = val notation; typically it has been though that these should yield better performance. This has led me to the conclusion that while non-dots outperform dot references - in a localised system using multiple imports - it makes it easier to recognise which one your are referencing to.

This was highlighted after using minSetSize and noticed the ~200ms difference between dot and non-dot references in favour of dot references.
`counter = collections.Counter` > `counter=Counter`

A second note I noticed from the exercise, `list.sort()` outperforms `list=sorted(list)`

~~~
