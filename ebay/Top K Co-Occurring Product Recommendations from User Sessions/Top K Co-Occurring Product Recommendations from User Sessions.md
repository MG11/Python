You are building a product recommendation engine for an e-commerce platform.


Given a list of user browsing sessions, where each session is a list of product IDs viewed by a user, and a target product ID target, find the k most frequently co-occurring products with the target product.


A product p co-occurs with target in a session if both p and target appear in that session. Count the total number of sessions in which each product co-occurs with the target. Return the k products with the highest co-occurrence count, sorted by frequency in descending order. If two products have the same frequency, break ties consistently, e.g. by product ID ascending.


Do NOT include the target product itself in the result.


Constraints


1 <= len(sessions) <= 10^5

1 <= len(sessions[i]) <= 100

1 <= k <= number of unique co-occurring products

Product IDs are strings or integers

Target is guaranteed to appear in at least one session


Examples

Input: sessions = [["A","B","C"], ["A","B","D"], ["A","C","D"], ["B","D","E"]], target = "A", k = 2


Output: ["B", "C"]


Explanation: Sessions containing 'A': sessions 0, 1, 2. Co-occurrence counts: B=2, C=2, D=2. With a consistent tie-break by product ID, the top 2 are ["B", "C"].


 


Input: sessions = [["X","Y"], ["X","Y","Z"], ["X","Z"], ["Y","Z"]], target = "X", k = 1


Output: ["Y"]


Explanation: Sessions containing 'X': sessions 0, 1, 2. Co-occurrence counts: Y=2, Z=2. With a consistent tie-break by product ID, return ["Y"].


 


Input: sessions = [[1,2,3], [1,2], [1,3,4], [2,3,4], [1,4]], target = 1, k = 3


Output: [2, 3, 4]


Explanation: Sessions containing 1: sessions 0, 1, 2, 4. Co-occurrence: 2->2, 3->2, 4->2. With ascending product ID as the tie-break, the result is [2, 3, 4].

Insider Tips
What they are testing: Combining hash maps with efficient top-K retrieval, plus production code quality awareness in Java.
If you require deterministic tie-breaking by product ID, be careful: sorting each bucket breaks the claimed O(N + U) worst-case bound. For strict O(N + U), bucket extraction can only guarantee arbitrary order within a bucket; for deterministic ordering, use a heap or sort candidates and state the higher complexity.
