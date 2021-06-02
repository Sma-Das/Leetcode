# Python Leetcode Tasks

All of the ones I have attempted/completed

### 1-Easy
> * backspaceCompare.py
> * intersection_II.py
> * isPalindrome.py
> * PalindromeLinkedList.py
> * maxDepth.py
> * countNegatives.py
> * isBalanced.py
> * checkSortRotate.py
> * lengthLastWord.py
> * arrayPairSum.py
> * runningSum.py
> * removeDuplicates.py
> * intersection.py
> * vowelReverse.py
> * diStringMatch.py
### 2-Medium
> * findOrder.py
> * minOperations.py
> * nonDecreasingArray.py
> * maxAncestorDiff.py
> * checkInclusion.py
> * uglyNumber.py
> * matrixScore.py
> * numRescueBoats.py
> * alphabetBoardPath.py
> * mergeIntervals.py
> * leastUniqueInts.py
> * maxProfitAssigned.py
> * maximumUniqueSubarray.py
> * biggestMountain.py
> * minSetSize.py
> * checkPow3.py
> * spiralMatrix.py
> * maxDistance.py
> * maxAverageSum.py
> * pushDominoes.py
> * countBattleships.py
> * displayTable.py
> * findCenter.py
> * LinkedListBinaryTree.py
> * canReach.py
> * maxProfit.py
> * minimumLength.py
> * hasAllCodes.py
> * numsSameConsecDiff.py
> * maxEvents.py
> * 01Matrix.py
> * CoinChange.py
> * findLongestWord.py
> * isValidBST.py
> * Notes.md
> * maxProductTree.py
> * rotateBox.py
> * newInterval.py
> * kFreqElements.py
> * LongestBeautifulSubString.py
> * numOfSubarrays.py
> * minFallingPathSum.py
> * characterReplacement.py
> * DiceTargetSum.py
> * countVowelString.py
### 3-Hard
> * uniquePathsIII.py
> * minDistance.py
> * RussianDolls.py
> * MaxRequests.py
> * orderlyQueue.py
> * RangeModule.py
> * getCoprimes.py
> * maxPathSum.py
> * isPossible.py

---
## Notes

2/6/21
2-Medium/minSetSize.py

One of the weirdest things I've noticed has been **dot references outperforming non-dot references**. This also includes var = var2 = val notation; typically it has been though that these should yield better performance. This has led me to the conclusion that while non-dots outperform dot references - in a localised system using multiple imports - it makes it easier to recognise which one your are referencing to.

This was highlighted after using minSetSize and noticed the ~200ms difference between dot and non-dot references in favour of dot references.

`counter = collections.Counter` > `counter=Counter`

A second note I noticed from the exercise,

`list.sort()` outperforms `list=sorted(list)`
