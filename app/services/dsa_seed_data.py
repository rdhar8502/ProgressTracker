"""
Comprehensive DSA Seed Dataset with Complete Searching & Sorting, Algorithms, and Company Tags
"""

DSA_COMPANIES = [
    # ── US/Global Tech ──
    "Adobe", "Airbnb", "Amazon", "Apple", "Atlassian", "Bloomberg",
    "ByteDance", "DE Shaw", "Dropbox", "Flipkart", "Goldman Sachs",
    "Google", "LinkedIn", "Meta", "Microsoft", "Netflix", "Oracle",
    "PayPal", "Paytm", "Pinterest", "Samsung", "Spotify",
    "Twitter / X", "Uber", "Valve",
    # ── 🇩🇪 Germany Tech ──
    "Zalando", "SAP", "Delivery Hero", "Siemens Tech",
    "Deutsche Bank Tech", "Celonis", "Personio", "Trade Republic",
    # ── 🇳🇱 Netherlands Tech ──
    "Booking.com", "Adyen", "ASML", "bol.com",
    "Philips Tech", "TomTom", "Takeaway / JustEat",
    # ── 🌍 EU / Pan-European ──
    "Spotify (Stockholm)", "Klarna", "Revolut", "Wise",
]

DSA_ALGORITHM_TOPICS = [
    "Kadane's Algorithm",
    "Dutch National Flag",
    "Boyer-Moore Voting",
    "Floyd's Tortoise & Hare",
    "Kahn's Algorithm (BFS Topo)",
    "Dijkstra's Algorithm",
    "Bellman-Ford Algorithm",
    "Floyd-Warshall Algorithm",
    "Kruskal's Algorithm (DSU)",
    "Prim's Algorithm",
    "0/1 Knapsack Pattern",
    "Unbounded Knapsack Pattern",
    "Longest Common Subsequence (LCS)",
    "Longest Increasing Subsequence (LIS)",
    "Morris Inorder Traversal",
    "Binary Search on Answer Range",
    "Monotonic Stack",
    "Monotonic Deque",
    "Trie Prefix Tree",
    "Cyclic Sort",
    "Prefix Sum & Hash Table",
    "Sliding Window (Dynamic)",
    "Backtracking & Pruning",
    "Bitmasking & Kernighan",
    "Sorting Algorithms",
    "Quickselect & Partition",
    "Merge Sort & Inversion Counting"
]

DSA_PROBLEMS_DATA = [
    {
        "category": "Arrays and Strings",
        "title": "Two Sum",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/two-sum/",
        "alternate_title": "Key Pair",
        "alternate_url": "https://www.geeksforgeeks.org/problems/key-pair5556/1",
        "pattern": "Hash Map Complement Lookup",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "HashMap / HashSet",
            "Prefix Sum & Hash Table"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Meta",
            "Microsoft",
            "Apple",
            "Bloomberg"
        ]
    },
    {
        "category": "Arrays and Strings",
        "title": "Best Time to Buy and Sell Stock",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/",
        "alternate_title": "Stock Buy and Sell \u2013 Max one transaction Allowed",
        "alternate_url": "https://www.geeksforgeeks.org/problems/buy-stock-2/1",
        "pattern": "Kadane's / One-Pass Min Tracking",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Kadane's Algorithm",
            "Dynamic Programming Basics"
        ],
        "companies": [
            "Amazon",
            "Meta",
            "Microsoft",
            "Google",
            "Goldman Sachs"
        ]
    },
    {
        "category": "Arrays and Strings",
        "title": "Maximum Subarray",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/maximum-subarray/",
        "alternate_title": "Kadane's Algorithm",
        "alternate_url": "https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1",
        "pattern": "Kadane's Algorithm (Max Subarray Sum)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Kadane's Algorithm",
            "Dynamic Programming Basics"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Google",
            "Meta",
            "Apple",
            "LinkedIn"
        ]
    },
    {
        "category": "Arrays and Strings",
        "title": "Maximum Product Subarray",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/maximum-product-subarray/",
        "alternate_title": "Maximum Product Subarray",
        "alternate_url": "https://www.geeksforgeeks.org/problems/maximum-product-subarray3604/1",
        "pattern": "Kadane's Variant (Min/Max Product Tracking)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Kadane's Algorithm",
            "Dynamic Programming Basics"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Microsoft",
            "LinkedIn"
        ]
    },
    {
        "category": "Sorting Algorithms",
        "title": "Sort Colors",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/sort-colors/",
        "alternate_title": "Sort an array of 0s, 1s and 2s",
        "alternate_url": "https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4242/1",
        "pattern": "Dutch National Flag Algorithm (3-Way Partition)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Dutch National Flag",
            "Two Pointers",
            "Sorting Algorithms"
        ],
        "companies": [
            "Microsoft",
            "Meta",
            "Amazon",
            "Apple",
            "Uber"
        ]
    },
    {
        "category": "Arrays and Strings",
        "title": "Majority Element",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/majority-element/",
        "alternate_title": "Majority Element",
        "alternate_url": "https://www.geeksforgeeks.org/problems/majority-element-1587115620/1",
        "pattern": "Boyer-Moore Voting Algorithm",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Boyer-Moore Voting"
        ],
        "companies": [
            "Google",
            "Amazon",
            "Microsoft",
            "Adobe"
        ]
    },
    {
        "category": "Arrays and Strings",
        "title": "Majority Element II",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/majority-element-ii/",
        "alternate_title": "Majority Vote (N/3 Times)",
        "alternate_url": "https://www.geeksforgeeks.org/problems/majority-vote/1",
        "pattern": "Extended Boyer-Moore Voting (2 Candidates)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Boyer-Moore Voting"
        ],
        "companies": [
            "Google",
            "Amazon",
            "Meta"
        ]
    },
    {
        "category": "Arrays and Strings",
        "title": "Next Permutation",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/next-permutation/",
        "alternate_title": "Next Permutation",
        "alternate_url": "https://www.geeksforgeeks.org/problems/next-permutation5226/1",
        "pattern": "Lexicographical Suffix Pivot & Swap",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Two Pointers"
        ],
        "companies": [
            "Meta",
            "Google",
            "Amazon",
            "Microsoft",
            "ByteDance"
        ]
    },
    {
        "category": "Arrays and Strings",
        "title": "Pascal's Triangle",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/pascals-triangle/",
        "alternate_title": "Pascal Triangle",
        "alternate_url": "https://www.geeksforgeeks.org/problems/pascal-triangle0652/1",
        "pattern": "Combinatorics / Row Generation",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N^2)",
        "secondary_topics": [
            "Dynamic Programming Basics"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Apple",
            "Microsoft"
        ]
    },
    {
        "category": "Arrays and Strings",
        "title": "Set Matrix Zeroes",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/set-matrix-zeroes/",
        "alternate_title": "Set Matrix Zeroes",
        "alternate_url": "https://www.geeksforgeeks.org/problems/set-matrix-zeroes/1",
        "pattern": "In-Place Matrix First Row/Col Marker",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Microsoft",
            "Amazon",
            "Meta",
            "Google"
        ]
    },
    {
        "category": "Arrays and Strings",
        "title": "Rotate Image",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/rotate-image/",
        "alternate_title": "Rotate by 90 degree",
        "alternate_url": "https://www.geeksforgeeks.org/problems/rotate-by-90-degree-1587115621/1",
        "pattern": "Matrix Transpose + Horizontal Reverse",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Microsoft",
            "Meta",
            "Google",
            "Apple"
        ]
    },
    {
        "category": "Arrays and Strings",
        "title": "Spiral Matrix",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/spiral-matrix/",
        "alternate_title": "Spirally traversing a matrix",
        "alternate_url": "https://www.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1",
        "pattern": "4-Boundary Shrinking Traversal",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Microsoft",
            "Amazon",
            "Apple",
            "Google"
        ]
    },
    {
        "category": "Arrays and Strings",
        "title": "Subarray Sum Equals K",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/subarray-sum-equals-k/",
        "alternate_title": "Subarrays with sum K",
        "alternate_url": "https://www.geeksforgeeks.org/problems/subarrays-with-sum-k/1",
        "pattern": "Prefix Sum + Hash Map Frequency",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "HashMap / HashSet",
            "Prefix Sum & Hash Table"
        ],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Microsoft",
            "Bloomberg"
        ]
    },
    {
        "category": "Arrays and Strings",
        "title": "Subarray Sums Divisible by K",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/subarray-sums-divisible-by-k/",
        "alternate_title": "Sub-Array sum divisible by K",
        "alternate_url": "https://www.geeksforgeeks.org/problems/sub-array-sum-divisible-by-k2617/1",
        "pattern": "Prefix Sum Modulo Hashing",
        "time_complexity": "O(N)",
        "space_complexity": "O(K)",
        "secondary_topics": [
            "HashMap / HashSet",
            "Prefix Sum & Hash Table"
        ],
        "companies": [
            "Amazon",
            "Meta",
            "Microsoft"
        ]
    },
    {
        "category": "Arrays and Strings",
        "title": "First Missing Positive",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/first-missing-positive/",
        "alternate_title": "Smallest Positive Missing Number",
        "alternate_url": "https://www.geeksforgeeks.org/problems/smallest-positive-missing-number-1587115621/1",
        "pattern": "Cyclic Sort / In-Place Index Hashing",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Cyclic Sort"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Microsoft",
            "Meta"
        ]
    },
    {
        "category": "Arrays and Strings",
        "title": "Find the Duplicate Number",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/find-the-duplicate-number/",
        "alternate_title": "Find duplicates in an array",
        "alternate_url": "https://www.geeksforgeeks.org/problems/find-duplicates-in-an-array/1",
        "pattern": "Floyd's Tortoise and Hare (Cycle Detection)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Floyd's Tortoise & Hare",
            "Two Pointers"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Google"
        ]
    },
    {
        "category": "Arrays and Strings",
        "title": "Merge Intervals",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/merge-intervals/",
        "alternate_title": "Overlapping Intervals",
        "alternate_url": "https://www.geeksforgeeks.org/problems/overlapping-intervals--170633/1",
        "pattern": "Sorting + Interval Greedy Merge",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Intervals"
        ],
        "companies": [
            "Meta",
            "Google",
            "Amazon",
            "Microsoft",
            "Bloomberg",
            "Uber"
        ]
    },
    {
        "category": "Arrays and Strings",
        "title": "Merge Sorted Array",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/merge-sorted-array/",
        "alternate_title": "Merge Without Extra Space",
        "alternate_url": "https://www.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1",
        "pattern": "Three Pointers (Backward Fill)",
        "time_complexity": "O(M + N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Two Pointers"
        ],
        "companies": [
            "Meta",
            "Microsoft",
            "Amazon",
            "Apple"
        ]
    },
    {
        "category": "Arrays and Strings",
        "title": "Find Missing And Repeating",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/set-mismatch/",
        "alternate_title": "Find Missing and Repeating",
        "alternate_url": "https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/1",
        "pattern": "Sum of N Math / Bitwise XOR Buckets",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Bit Manipulation"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Goldman Sachs"
        ]
    },
    {
        "category": "Arrays and Strings",
        "title": "Product of Array Except Self",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/product-of-array-except-self/",
        "alternate_title": "Product array puzzle",
        "alternate_url": "https://www.geeksforgeeks.org/problems/product-array-puzzle4525/1",
        "pattern": "Prefix & Suffix Running Product",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Meta",
            "Amazon",
            "Apple",
            "Microsoft",
            "Google"
        ]
    },
    {
        "category": "Arrays and Strings",
        "title": "Longest Consecutive Sequence",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/longest-consecutive-sequence/",
        "alternate_title": "Longest Consecutive Subsequence",
        "alternate_url": "https://www.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1",
        "pattern": "Hash Set Intelligent Sequence Start",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "HashMap / HashSet"
        ],
        "companies": [
            "Google",
            "Meta",
            "Amazon",
            "Microsoft",
            "Spotify"
        ]
    },
    {
        "category": "Sorting Algorithms",
        "title": "Count Inversions",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/global-and-local-inversions/",
        "alternate_title": "Inversion of array",
        "alternate_url": "https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1",
        "pattern": "Merge Sort Modification (Divide & Conquer)",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Sorting Algorithms"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Flipkart"
        ]
    },
    {
        "category": "Sorting Algorithms",
        "title": "Reverse Pairs",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/reverse-pairs/",
        "alternate_title": "Count Reverse Pairs",
        "alternate_url": "https://www.geeksforgeeks.org/problems/count-reverse-pairs/1",
        "pattern": "Merge Sort Inversion Counting / Fenwick Tree",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Sorting Algorithms"
        ],
        "companies": [
            "Google",
            "Amazon",
            "Microsoft"
        ]
    },
    {
        "category": "Arrays and Strings",
        "title": "Leaders In An Array",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/",
        "alternate_title": "Leaders in an array",
        "alternate_url": "https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1",
        "pattern": "Right-to-Left Running Maximum Scan",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Microsoft",
            "Adobe"
        ]
    },
    {
        "category": "Arrays and Strings",
        "title": "String to Integer (atoi)",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/string-to-integer-atoi/",
        "alternate_title": "Implement Atoi",
        "alternate_url": "https://www.geeksforgeeks.org/problems/implement-atoi/1",
        "pattern": "String State Machine & Overflow Guard",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Microsoft",
            "Meta",
            "Bloomberg",
            "Apple"
        ]
    },
    {
        "category": "Arrays and Strings",
        "title": "Longest Common Prefix",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/longest-common-prefix/",
        "alternate_title": "Longest Common Prefix of Strings",
        "alternate_url": "https://www.geeksforgeeks.org/problems/longest-common-prefix-in-an-array5129/1",
        "pattern": "Horizontal Scanning / Vertical Scanning",
        "time_complexity": "O(S)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Tries"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Adobe",
            "Apple"
        ]
    },
    {
        "category": "HashMap / HashSet",
        "title": "Contains Duplicate",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/contains-duplicate/",
        "alternate_title": "Contains Duplicate",
        "alternate_url": "https://www.geeksforgeeks.org/problems/contains-duplicate/1",
        "pattern": "Hash Set Fast Membership",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Apple",
            "Microsoft"
        ]
    },
    {
        "category": "HashMap / HashSet",
        "title": "Valid Anagram",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/valid-anagram/",
        "alternate_title": "Anagram",
        "alternate_url": "https://www.geeksforgeeks.org/problems/anagram-1587115620/1",
        "pattern": "Character Frequency Array Count",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Google",
            "Bloomberg",
            "Uber"
        ]
    },
    {
        "category": "HashMap / HashSet",
        "title": "Group Anagrams",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/group-anagrams/",
        "alternate_title": "Print Anagrams Together",
        "alternate_url": "https://www.geeksforgeeks.org/problems/print-anagrams-together/1",
        "pattern": "Character Count Tuple Key Hashing",
        "time_complexity": "O(N * K)",
        "space_complexity": "O(N * K)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Meta",
            "Google",
            "Microsoft",
            "Apple",
            "Uber"
        ]
    },
    {
        "category": "HashMap / HashSet",
        "title": "Top K Frequent Elements",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/top-k-frequent-elements/",
        "alternate_title": "Top K Frequent Elements in Array",
        "alternate_url": "https://www.geeksforgeeks.org/problems/top-k-frequent-elements-in-array/1",
        "pattern": "Frequency Hash Map + Bucket Sort",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Heap / Priority Queue"
        ],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Microsoft",
            "Uber",
            "Apple"
        ]
    },
    {
        "category": "HashMap / HashSet",
        "title": "Insert Delete GetRandom O(1)",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/insert-delete-getrandom-o1/",
        "alternate_title": "Design Insert Delete GetRandom O(1)",
        "alternate_url": "https://www.geeksforgeeks.org/problems/design-a-data-structure-that-supports-insert-delete-getrandom-in-o1-time/1",
        "pattern": "Hash Map + Dynamic Array (Swap with Last)",
        "time_complexity": "O(1) average",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "LinkedIn",
            "Twitter / X"
        ]
    },
    {
        "category": "HashMap / HashSet",
        "title": "Continuous Subarray Sum",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/continuous-subarray-sum/",
        "alternate_title": "Subarray with given sum",
        "alternate_url": "https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1",
        "pattern": "Prefix Sum Modulo Hashing",
        "time_complexity": "O(N)",
        "space_complexity": "O(min(N, K))",
        "secondary_topics": [
            "Prefix Sum & Hash Table"
        ],
        "companies": [
            "Meta",
            "Amazon",
            "Microsoft"
        ]
    },
    {
        "category": "HashMap / HashSet",
        "title": "Word Pattern",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/word-pattern/",
        "alternate_title": "Match specific pattern",
        "alternate_url": "https://www.geeksforgeeks.org/problems/match-specific-pattern/1",
        "pattern": "Bi-directional Bijection Hashing",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Uber",
            "Dropbox"
        ]
    },
    {
        "category": "HashMap / HashSet",
        "title": "Isomorphic Strings",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/isomorphic-strings/",
        "alternate_title": "Isomorphic Strings",
        "alternate_url": "https://www.geeksforgeeks.org/problems/isomorphic-strings-1587115620/1",
        "pattern": "Two-Way Character Mapping Array",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Google",
            "LinkedIn"
        ]
    },
    {
        "category": "HashMap / HashSet",
        "title": "First Unique Character in a String",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/first-unique-character-in-a-string/",
        "alternate_title": "Non Repeating Character",
        "alternate_url": "https://www.geeksforgeeks.org/problems/non-repeating-character-1587115620/1",
        "pattern": "Two-Pass Frequency Counting",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Bloomberg",
            "Microsoft",
            "Google",
            "Goldman Sachs"
        ]
    },
    {
        "category": "HashMap / HashSet",
        "title": "Longest Substring with At Most K Distinct Characters",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/",
        "alternate_title": "Longest Substring with K Distinct Characters",
        "alternate_url": "https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1",
        "pattern": "Sliding Window + Frequency Map",
        "time_complexity": "O(N)",
        "space_complexity": "O(K)",
        "secondary_topics": [
            "Sliding Window",
            "Sliding Window (Dynamic)"
        ],
        "companies": [
            "Google",
            "Amazon",
            "Meta"
        ]
    },
    {
        "category": "HashMap / HashSet",
        "title": "Subarray with 0 Sum",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/contiguous-array/",
        "alternate_title": "Subarray with 0 sum",
        "alternate_url": "https://www.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1",
        "pattern": "Prefix Sum Hash Set Existence Check",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Prefix Sum & Hash Table"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "PayPal"
        ]
    },
    {
        "category": "HashMap / HashSet",
        "title": "Count Subarrays with Given XOR",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/",
        "alternate_title": "Count Subarrays with Given XOR",
        "alternate_url": "https://www.geeksforgeeks.org/problems/count-subarray-with-given-xor/1",
        "pattern": "Prefix XOR + Frequency Map",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Bit Manipulation",
            "Prefix Sum & Hash Table"
        ],
        "companies": [
            "Amazon",
            "Flipkart"
        ]
    },
    {
        "category": "HashMap / HashSet",
        "title": "Find All Anagrams in a String",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/find-all-anagrams-in-a-string/",
        "alternate_title": "Count Occurences of Anagrams",
        "alternate_url": "https://www.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1",
        "pattern": "Sliding Window + Frequency Matching",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Sliding Window"
        ],
        "companies": [
            "Meta",
            "Amazon",
            "Microsoft",
            "Google"
        ]
    },
    {
        "category": "HashMap / HashSet",
        "title": "Minimum Window Subsequence",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/minimum-window-subsequence/",
        "alternate_title": "Minimum Window Subsequence",
        "alternate_url": "https://www.geeksforgeeks.org/problems/minimum-window-subsequence/1",
        "pattern": "Two Pointers with Backward Contraction",
        "time_complexity": "O(S * T)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Two Pointers",
            "Dynamic Programming Basics"
        ],
        "companies": [
            "Google",
            "Meta",
            "Amazon"
        ]
    },
    {
        "category": "Two Pointers",
        "title": "Valid Palindrome",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/valid-palindrome/",
        "alternate_title": "Palindrome String",
        "alternate_url": "https://www.geeksforgeeks.org/problems/string-palindrome2749/1",
        "pattern": "Two Pointers (Inward Scan with Alphanumeric Filtering)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Meta",
            "Microsoft",
            "Amazon",
            "Apple"
        ]
    },
    {
        "category": "Two Pointers",
        "title": "Two Sum II - Input Array Is Sorted",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/",
        "alternate_title": "Pair with given sum in a sorted array",
        "alternate_url": "https://www.geeksforgeeks.org/problems/pair-with-given-sum-in-a-sorted-array4940/1",
        "pattern": "Two Pointers (Opposite Ends Convergence)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Binary Search"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Apple"
        ]
    },
    {
        "category": "Two Pointers",
        "title": "3Sum",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/3sum/",
        "alternate_title": "Triplet Sum in Array",
        "alternate_url": "https://www.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/1",
        "pattern": "Sorting + Two Pointers with Duplication Skip",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Meta",
            "Amazon",
            "Microsoft",
            "Google",
            "Apple",
            "Bloomberg"
        ]
    },
    {
        "category": "Two Pointers",
        "title": "3Sum Closest",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/3sum-closest/",
        "alternate_title": "3 Sum Closest",
        "alternate_url": "https://www.geeksforgeeks.org/problems/3-sum-closest/1",
        "pattern": "Sorting + Two Pointers (Min Diff Tracking)",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Google",
            "Bloomberg"
        ]
    },
    {
        "category": "Two Pointers",
        "title": "4Sum",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/4sum/",
        "alternate_title": "Find All Four Sum Numbers",
        "alternate_url": "https://www.geeksforgeeks.org/problems/find-all-four-sum-numbers1732/1",
        "pattern": "Sorting + Nested Loops + Two Pointers",
        "time_complexity": "O(N^3)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Microsoft",
            "Apple"
        ]
    },
    {
        "category": "Two Pointers",
        "title": "Container With Most Water",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/container-with-most-water/",
        "alternate_title": "Container With Most Water",
        "alternate_url": "https://www.geeksforgeeks.org/problems/container-with-most-water/1",
        "pattern": "Greedy Two Pointers (Shift Min Height)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Google",
            "Meta",
            "Apple",
            "Microsoft"
        ]
    },
    {
        "category": "Two Pointers",
        "title": "Move Zeroes",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/move-zeroes/",
        "alternate_title": "Move all zeroes to end of array",
        "alternate_url": "https://www.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1",
        "pattern": "Slow and Fast Pointer (In-Place Partition)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Meta",
            "Amazon",
            "Apple",
            "Microsoft",
            "Bloomberg"
        ]
    },
    {
        "category": "Two Pointers",
        "title": "Remove Duplicates from Sorted Array",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/remove-duplicates-from-sorted-array/",
        "alternate_title": "Remove duplicate elements from sorted Array",
        "alternate_url": "https://www.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1",
        "pattern": "Two Pointers (Slow Write Pointer)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Microsoft",
            "Amazon",
            "Google",
            "Meta"
        ]
    },
    {
        "category": "Two Pointers",
        "title": "Remove Duplicates from Sorted Array II",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/",
        "alternate_title": "Remove Duplicates II",
        "alternate_url": "https://www.geeksforgeeks.org/problems/remove-duplicates-from-sorted-array-ii/1",
        "pattern": "Two Pointers (At Most 2 Occurrences Write Window)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Meta",
            "Amazon",
            "Microsoft"
        ]
    },
    {
        "category": "Two Pointers",
        "title": "Backspace String Compare",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/backspace-string-compare/",
        "alternate_title": "Backspace String Compare",
        "alternate_url": "https://www.geeksforgeeks.org/problems/backspace-string-compare/1",
        "pattern": "Two Pointers from Suffix (O(1) Space)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Stack / Monotonic Stack"
        ],
        "companies": [
            "Google",
            "Meta",
            "Amazon",
            "Bloomberg"
        ]
    },
    {
        "category": "Two Pointers",
        "title": "Boats to Save People",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/boats-to-save-people/",
        "alternate_title": "Boats to Save People",
        "alternate_url": "https://www.geeksforgeeks.org/problems/boats-to-save-people/1",
        "pattern": "Greedy Sorting + Two Pointers (Heaviest + Lightest)",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "Two Pointers",
        "title": "Valid Palindrome II",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/valid-palindrome-ii/",
        "alternate_title": "Delete One Character Palindrome",
        "alternate_url": "https://www.geeksforgeeks.org/problems/delete-one-character-to-make-palindrome/1",
        "pattern": "Two Pointers with Single Mismatch Branching",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Meta",
            "Amazon",
            "Microsoft",
            "Apple"
        ]
    },
    {
        "category": "Two Pointers",
        "title": "Sort Array By Parity",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/sort-array-by-parity/",
        "alternate_title": "Segregate Even and Odd numbers",
        "alternate_url": "https://www.geeksforgeeks.org/problems/segregate-even-and-odd-numbers4629/1",
        "pattern": "Two Pointers (Inward Partition)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Meta"
        ]
    },
    {
        "category": "Two Pointers",
        "title": "Trapping Rain Water",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/trapping-rain-water/",
        "alternate_title": "Trapping Rain Water",
        "alternate_url": "https://www.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1",
        "pattern": "Two Pointers (LeftMax vs RightMax Convergence)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Stack / Monotonic Stack"
        ],
        "companies": [
            "Google",
            "Meta",
            "Amazon",
            "Microsoft",
            "Goldman Sachs",
            "ByteDance",
            "Apple"
        ]
    },
    {
        "category": "Sliding Window",
        "title": "Longest Substring Without Repeating Characters",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/longest-substring-without-repeating-characters/",
        "alternate_title": "Length of the longest substring",
        "alternate_url": "https://www.geeksforgeeks.org/problems/length-of-the-longest-substring3036/1",
        "pattern": "Sliding Window (Dynamic Window + Last Seen Map)",
        "time_complexity": "O(N)",
        "space_complexity": "O(min(M, N))",
        "secondary_topics": [
            "HashMap / HashSet",
            "Sliding Window (Dynamic)"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Meta",
            "Microsoft",
            "Apple",
            "ByteDance",
            "Bloomberg"
        ]
    },
    {
        "category": "Sliding Window",
        "title": "Minimum Window Substring",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/minimum-window-substring/",
        "alternate_title": "Smallest window in a string containing all the characters of another string",
        "alternate_url": "https://www.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1",
        "pattern": "Sliding Window (Dynamic Shrinking + Required Char Counter)",
        "time_complexity": "O(M + N)",
        "space_complexity": "O(M + N)",
        "secondary_topics": [
            "Sliding Window (Dynamic)",
            "HashMap / HashSet"
        ],
        "companies": [
            "Meta",
            "Google",
            "Amazon",
            "Microsoft",
            "Uber",
            "ByteDance",
            "LinkedIn"
        ]
    },
    {
        "category": "Sliding Window",
        "title": "Longest Repeating Character Replacement",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/longest-repeating-character-replacement/",
        "alternate_title": "Longest Repeating Character Replacement",
        "alternate_url": "https://www.geeksforgeeks.org/problems/longest-repeating-character-replacement/1",
        "pattern": "Sliding Window (Window Length - Max Frequency <= K)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Sliding Window (Dynamic)"
        ],
        "companies": [
            "Google",
            "Amazon",
            "Meta",
            "Uber"
        ]
    },
    {
        "category": "Sliding Window",
        "title": "Permutation in String",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/permutation-in-string/",
        "alternate_title": "Permutation in String",
        "alternate_url": "https://www.geeksforgeeks.org/problems/permutation-in-string/1",
        "pattern": "Sliding Window (Fixed Window Frequency Match)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "HashMap / HashSet"
        ],
        "companies": [
            "Meta",
            "Microsoft",
            "Amazon",
            "Google"
        ]
    },
    {
        "category": "Sliding Window",
        "title": "Maximum Average Subarray I",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/maximum-average-subarray-i/",
        "alternate_title": "Max Sum Subarray of size K",
        "alternate_url": "https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1",
        "pattern": "Sliding Window (Fixed Window Size K)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "Sliding Window",
        "title": "Minimum Size Subarray Sum",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/minimum-size-subarray-sum/",
        "alternate_title": "Smallest subarray with sum greater than x",
        "alternate_url": "https://www.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x5651/1",
        "pattern": "Sliding Window (Dynamic Contraction)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Sliding Window (Dynamic)",
            "Binary Search"
        ],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Goldman Sachs"
        ]
    },
    {
        "category": "Sliding Window",
        "title": "Max Consecutive Ones III",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/max-consecutive-ones-iii/",
        "alternate_title": "Maximize Number of 1's",
        "alternate_url": "https://www.geeksforgeeks.org/problems/maximize-number-of-1s3142/1",
        "pattern": "Sliding Window (At Most K Zeroes in Window)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Sliding Window (Dynamic)"
        ],
        "companies": [
            "Meta",
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "Sliding Window",
        "title": "Fruit Into Baskets",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/fruit-into-baskets/",
        "alternate_title": "Fruit Into Baskets",
        "alternate_url": "https://www.geeksforgeeks.org/problems/fruit-into-baskets-1663137462/1",
        "pattern": "Sliding Window (At Most 2 Distinct Types)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Sliding Window (Dynamic)",
            "HashMap / HashSet"
        ],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "Sliding Window",
        "title": "Subarrays with K Different Integers",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/subarrays-with-k-different-integers/",
        "alternate_title": "Subarrays with K Different Integers",
        "alternate_url": "https://www.geeksforgeeks.org/problems/subarrays-with-k-different-integers/1",
        "pattern": "Exact(K) = AtMost(K) - AtMost(K - 1) Sliding Window",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Sliding Window (Dynamic)"
        ],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "Sliding Window",
        "title": "Count Number of Nice Subarrays",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/count-number-of-nice-subarrays/",
        "alternate_title": "Count Subarray with k odds",
        "alternate_url": "https://www.geeksforgeeks.org/problems/count-subarray-with-k-odds/1",
        "pattern": "Sliding Window / Prefix Sum (AtMost Pattern)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Prefix Sum & Hash Table"
        ],
        "companies": [
            "Amazon",
            "Google"
        ]
    },
    {
        "category": "Sliding Window",
        "title": "Binary Subarrays With Sum",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/binary-subarrays-with-sum/",
        "alternate_title": "Binary subarray with sum",
        "alternate_url": "https://www.geeksforgeeks.org/problems/binary-subarray-with-sum/1",
        "pattern": "AtMost(Goal) - AtMost(Goal - 1) Window",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Prefix Sum & Hash Table"
        ],
        "companies": [
            "Amazon",
            "Google"
        ]
    },
    {
        "category": "Sliding Window",
        "title": "Maximum Points You Can Obtain from Cards",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/",
        "alternate_title": "Card Rotation Problem",
        "alternate_url": "https://www.geeksforgeeks.org/problems/card-rotation/1",
        "pattern": "Sliding Window (Minimize Middle Window of Size N - K)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "Sliding Window",
        "title": "Defuse the Bomb",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/defuse-the-bomb/",
        "alternate_title": "Circular Array Window",
        "alternate_url": "https://www.geeksforgeeks.org/problems/circular-array-sum/1",
        "pattern": "Circular Array Fixed Sliding Window",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Google"
        ]
    },
    {
        "category": "Sliding Window",
        "title": "Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/",
        "alternate_title": "Count subarrays of size K with threshold",
        "alternate_url": "https://www.geeksforgeeks.org/problems/subarrays-of-size-k/1",
        "pattern": "Fixed Window Size K Running Sum",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Amazon"
        ]
    },
    {
        "category": "Stack / Monotonic Stack",
        "title": "Valid Parentheses",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/valid-parentheses/",
        "alternate_title": "Parenthesis Checker",
        "alternate_url": "https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1",
        "pattern": "Stack Bracket Matching",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Meta",
            "Amazon",
            "Microsoft",
            "Google",
            "Bloomberg",
            "Apple"
        ]
    },
    {
        "category": "Stack / Monotonic Stack",
        "title": "Min Stack",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/min-stack/",
        "alternate_title": "Special Stack",
        "alternate_url": "https://www.geeksforgeeks.org/problems/special-stack/1",
        "pattern": "Pair Stack / Encoded Value Min Tracking",
        "time_complexity": "O(1) all ops",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Bloomberg",
            "Microsoft",
            "Google",
            "Meta",
            "Apple"
        ]
    },
    {
        "category": "Stack / Monotonic Stack",
        "title": "Evaluate Reverse Polish Notation",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/evaluate-reverse-polish-notation/",
        "alternate_title": "Evaluation of Postfix Expression",
        "alternate_url": "https://www.geeksforgeeks.org/problems/evaluation-of-postfix-expression1735/1",
        "pattern": "Stack Postfix Operand Evaluation",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "LinkedIn",
            "Google",
            "Microsoft"
        ]
    },
    {
        "category": "Stack / Monotonic Stack",
        "title": "Daily Temperatures",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/daily-temperatures/",
        "alternate_title": "Next Greater Element",
        "alternate_url": "https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1",
        "pattern": "Monotonic Decreasing Stack (Next Warmer Day)",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Monotonic Stack"
        ],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Bloomberg"
        ]
    },
    {
        "category": "Stack / Monotonic Stack",
        "title": "Next Greater Element I",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/next-greater-element-i/",
        "alternate_title": "Next Greater Element I",
        "alternate_url": "https://www.geeksforgeeks.org/problems/next-greater-element/1",
        "pattern": "Monotonic Stack + Hash Map",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Monotonic Stack"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Microsoft"
        ]
    },
    {
        "category": "Stack / Monotonic Stack",
        "title": "Next Greater Element II",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/next-greater-element-ii/",
        "alternate_title": "Next Greater Element in Circular Array",
        "alternate_url": "https://www.geeksforgeeks.org/problems/next-greater-element-2/1",
        "pattern": "Monotonic Stack on Circular Array (2N Iteration)",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Monotonic Stack"
        ],
        "companies": [
            "Google",
            "Amazon",
            "Microsoft"
        ]
    },
    {
        "category": "Stack / Monotonic Stack",
        "title": "Largest Rectangle in Histogram",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/largest-rectangle-in-histogram/",
        "alternate_title": "Maximum Rectangular Area in a Histogram",
        "alternate_url": "https://www.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram-1587115620/1",
        "pattern": "Monotonic Increasing Stack (Previous & Next Smaller)",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Monotonic Stack"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Meta",
            "Microsoft",
            "Apple",
            "Uber"
        ]
    },
    {
        "category": "Stack / Monotonic Stack",
        "title": "Maximal Rectangle",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/maximal-rectangle/",
        "alternate_title": "Max rectangle",
        "alternate_url": "https://www.geeksforgeeks.org/problems/max-rectangle/1",
        "pattern": "2D Cumulative Heights + Histogram Monotonic Stack",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Monotonic Stack",
            "DP on Grids"
        ],
        "companies": [
            "Google",
            "Amazon",
            "Microsoft",
            "Meta"
        ]
    },
    {
        "category": "Stack / Monotonic Stack",
        "title": "Asteroid Collision",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/asteroid-collision/",
        "alternate_title": "Asteroid Collision",
        "alternate_url": "https://www.geeksforgeeks.org/problems/asteroid-collision/1",
        "pattern": "Stack Directional Simulation & Collision",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon",
            "Meta",
            "Uber",
            "Apple"
        ]
    },
    {
        "category": "Stack / Monotonic Stack",
        "title": "Sum of Subarray Minimums",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/sum-of-subarray-minimums/",
        "alternate_title": "Sum of Subarray Minimums",
        "alternate_url": "https://www.geeksforgeeks.org/problems/sum-of-subarray-minimum/1",
        "pattern": "Monotonic Stack (Contribution Count via PLE & NLE)",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Monotonic Stack"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Google"
        ]
    },
    {
        "category": "Stack / Monotonic Stack",
        "title": "Online Stock Span",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/online-stock-span/",
        "alternate_title": "Stock span problem",
        "alternate_url": "https://www.geeksforgeeks.org/problems/stock-span-problem-1587115621/1",
        "pattern": "Monotonic Stack (Accumulating Price & Span)",
        "time_complexity": "O(1) amortized",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Monotonic Stack"
        ],
        "companies": [
            "Amazon",
            "Meta",
            "Google",
            "Microsoft"
        ]
    },
    {
        "category": "Stack / Monotonic Stack",
        "title": "Remove K Digits",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/remove-k-digits/",
        "alternate_title": "Remove K Digits",
        "alternate_url": "https://www.geeksforgeeks.org/problems/remove-k-digits/1",
        "pattern": "Monotonic Increasing Stack (Greedy Peak Pop)",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Monotonic Stack"
        ],
        "companies": [
            "Google",
            "Amazon",
            "Microsoft"
        ]
    },
    {
        "category": "Stack / Monotonic Stack",
        "title": "Basic Calculator",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/basic-calculator/",
        "alternate_title": "Expression Evaluation",
        "alternate_url": "https://www.geeksforgeeks.org/problems/expression-evaluation/1",
        "pattern": "Stack Sign & Parentheses State Tracking",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Meta",
            "Amazon",
            "Microsoft"
        ]
    },
    {
        "category": "Stack / Monotonic Stack",
        "title": "Basic Calculator II",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/basic-calculator-ii/",
        "alternate_title": "Evaluation of Expression",
        "alternate_url": "https://www.geeksforgeeks.org/problems/evaluate-the-expression/1",
        "pattern": "Stack Operator Precedence Reduction",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Meta",
            "Amazon",
            "Microsoft",
            "Google"
        ]
    },
    {
        "category": "Stack / Monotonic Stack",
        "title": "Decode String",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/decode-string/",
        "alternate_title": "Decode the string",
        "alternate_url": "https://www.geeksforgeeks.org/problems/decode-the-string2444/1",
        "pattern": "Two Stacks (Repeat Count & Current String)",
        "time_complexity": "O(Output Length)",
        "space_complexity": "O(Output Length)",
        "secondary_topics": [
            "Recursion and Backtracking"
        ],
        "companies": [
            "Google",
            "Bloomberg",
            "Amazon",
            "Meta",
            "Oracle"
        ]
    },
    {
        "category": "Stack / Monotonic Stack",
        "title": "Implement Queue using Stacks",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/implement-queue-using-stacks/",
        "alternate_title": "Queue using two Stacks",
        "alternate_url": "https://www.geeksforgeeks.org/problems/queue-using-two-stacks/1",
        "pattern": "Two Stacks Amortized O(1) Push/Pop",
        "time_complexity": "O(1) amortized",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Queue / Deque"
        ],
        "companies": [
            "Microsoft",
            "Amazon",
            "Google",
            "Goldman Sachs"
        ]
    },
    {
        "category": "Queue / Deque",
        "title": "Design Circular Queue",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/design-circular-queue/",
        "alternate_title": "Circular Queue Implementation",
        "alternate_url": "https://www.geeksforgeeks.org/problems/circular-queue/1",
        "pattern": "Ring Buffer with Head/Tail Modulo Pointers",
        "time_complexity": "O(1) all ops",
        "space_complexity": "O(K)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Microsoft",
            "Google",
            "Meta"
        ]
    },
    {
        "category": "Queue / Deque",
        "title": "Design Circular Deque",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/design-circular-deque/",
        "alternate_title": "Design Circular Deque",
        "alternate_url": "https://www.geeksforgeeks.org/problems/design-circular-deque/1",
        "pattern": "Double-Ended Ring Buffer",
        "time_complexity": "O(1) all ops",
        "space_complexity": "O(K)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "Queue / Deque",
        "title": "Sliding Window Maximum",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/sliding-window-maximum/",
        "alternate_title": "Maximum of all subarrays of size k",
        "alternate_url": "https://www.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1",
        "pattern": "Monotonic Decreasing Deque",
        "time_complexity": "O(N)",
        "space_complexity": "O(K)",
        "secondary_topics": [
            "Monotonic Deque",
            "Sliding Window"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Meta",
            "Microsoft",
            "ByteDance",
            "Uber"
        ]
    },
    {
        "category": "Queue / Deque",
        "title": "Rotting Oranges",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/rotting-oranges/",
        "alternate_title": "Rotten Oranges",
        "alternate_url": "https://www.geeksforgeeks.org/problems/rotten-oranges2536/1",
        "pattern": "Multi-Source BFS Level-by-Level Queue",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(M * N)",
        "secondary_topics": [
            "Graph BFS/DFS"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Uber",
            "Google",
            "Meta"
        ]
    },
    {
        "category": "Queue / Deque",
        "title": "01 Matrix",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/01-matrix/",
        "alternate_title": "Distance of nearest cell having 1",
        "alternate_url": "https://www.geeksforgeeks.org/problems/distance-of-nearest-cell-having-1-1587115620/1",
        "pattern": "Multi-Source BFS Queue Flood Fill",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(M * N)",
        "secondary_topics": [
            "Graph BFS/DFS"
        ],
        "companies": [
            "Google",
            "Amazon",
            "Microsoft",
            "Apple"
        ]
    },
    {
        "category": "Queue / Deque",
        "title": "Implement Stack using Queues",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/implement-stack-using-queues/",
        "alternate_title": "Stack using two queues",
        "alternate_url": "https://www.geeksforgeeks.org/problems/stack-using-two-queues/1",
        "pattern": "Single Queue Rotation on Push",
        "time_complexity": "O(N) push, O(1) pop",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Stack / Monotonic Stack"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Bloomberg"
        ]
    },
    {
        "category": "Queue / Deque",
        "title": "First Non-Repeating Character in a Stream",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/first-unique-character-in-a-string/",
        "alternate_title": "First non-repeating character in a stream",
        "alternate_url": "https://www.geeksforgeeks.org/problems/first-non-repeating-character-in-a-stream1216/1",
        "pattern": "Queue + Frequency Array Streaming",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "HashMap / HashSet"
        ],
        "companies": [
            "Amazon",
            "Flipkart",
            "Microsoft"
        ]
    },
    {
        "category": "Queue / Deque",
        "title": "Number of Recent Calls",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/number-of-recent-calls/",
        "alternate_title": "Number of Recent Calls",
        "alternate_url": "https://www.geeksforgeeks.org/problems/number-of-recent-calls/1",
        "pattern": "Queue Sliding Time Window (t - 3000)",
        "time_complexity": "O(1) amortized",
        "space_complexity": "O(W)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "Queue / Deque",
        "title": "Shortest Subarray with Sum at Least K",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/",
        "alternate_title": "Shortest Subarray with Sum at Least K",
        "alternate_url": "https://www.geeksforgeeks.org/problems/shortest-subarray-with-sum-at-least-k/1",
        "pattern": "Prefix Sum + Monotonic Increasing Deque",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Monotonic Deque",
            "Prefix Sum & Hash Table"
        ],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "Queue / Deque",
        "title": "Constrained Subsequence Sum",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/constrained-subsequence-sum/",
        "alternate_title": "Constrained Subsequence Sum",
        "alternate_url": "https://www.geeksforgeeks.org/problems/constrained-subsequence-sum/1",
        "pattern": "DP + Monotonic Deque Sliding Window Max",
        "time_complexity": "O(N)",
        "space_complexity": "O(K)",
        "secondary_topics": [
            "Dynamic Programming Basics",
            "Monotonic Deque"
        ],
        "companies": [
            "Google",
            "Meta"
        ]
    },
    {
        "category": "Queue / Deque",
        "title": "Dota2 Senate",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/dota2-senate/",
        "alternate_title": "Dota2 Senate Voting",
        "alternate_url": "https://www.geeksforgeeks.org/problems/dota2-senate/1",
        "pattern": "Two Queues Index Round Simulation",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Valve",
            "Google"
        ]
    },
    {
        "category": "Queue / Deque",
        "title": "Reveal Cards In Increasing Order",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/reveal-cards-in-increasing-order/",
        "alternate_title": "Reveal Cards",
        "alternate_url": "https://www.geeksforgeeks.org/problems/reveal-cards/1",
        "pattern": "Deque Reverse Simulation",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Google"
        ]
    },
    {
        "category": "Binary Search",
        "title": "Binary Search",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/binary-search/",
        "alternate_title": "Binary Search",
        "alternate_url": "https://www.geeksforgeeks.org/problems/binary-search-1587115620/1",
        "pattern": "Classic Half-Interval Search",
        "time_complexity": "O(log N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Microsoft",
            "Amazon",
            "Apple",
            "Meta"
        ]
    },
    {
        "category": "Binary Search",
        "title": "Search in Rotated Sorted Array",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/search-in-rotated-sorted-array/",
        "alternate_title": "Search in a Rotated Array",
        "alternate_url": "https://www.geeksforgeeks.org/problems/search-in-a-rotated-array4618/1",
        "pattern": "Modified Binary Search (Identify Sorted Half)",
        "time_complexity": "O(log N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Microsoft",
            "Meta",
            "Google",
            "Apple",
            "LinkedIn"
        ]
    },
    {
        "category": "Binary Search",
        "title": "Search in Rotated Sorted Array II",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/search-in-rotated-sorted-array-ii/",
        "alternate_title": "Search in Rotated Array 2",
        "alternate_url": "https://www.geeksforgeeks.org/problems/search-in-rotated-array-2/1",
        "pattern": "Binary Search with Duplicate Handling (Trim Edges)",
        "time_complexity": "O(log N) average, O(N) worst",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Google"
        ]
    },
    {
        "category": "Binary Search",
        "title": "Find Minimum in Rotated Sorted Array",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/",
        "alternate_title": "Minimum element in a sorted and rotated array",
        "alternate_url": "https://www.geeksforgeeks.org/problems/minimum-element-in-a-sorted-and-rotated-array3611/1",
        "pattern": "Binary Search for Inflection Point (Pivot)",
        "time_complexity": "O(log N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Microsoft",
            "Meta",
            "Google",
            "Apple"
        ]
    },
    {
        "category": "Binary Search",
        "title": "Find First and Last Position of Element in Sorted Array",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/",
        "alternate_title": "First and last occurrences of x",
        "alternate_url": "https://www.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1",
        "pattern": "Lower Bound and Upper Bound Binary Search",
        "time_complexity": "O(log N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Microsoft",
            "LinkedIn"
        ]
    },
    {
        "category": "Binary Search",
        "title": "Search Insert Position",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/search-insert-position/",
        "alternate_title": "Search insert position of K in a sorted array",
        "alternate_url": "https://www.geeksforgeeks.org/problems/search-insert-position-of-k-in-a-sorted-array/1",
        "pattern": "Lower Bound Binary Search",
        "time_complexity": "O(log N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon",
            "Apple"
        ]
    },
    {
        "category": "Binary Search",
        "title": "Find Peak Element",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/find-peak-element/",
        "alternate_title": "Peak element",
        "alternate_url": "https://www.geeksforgeeks.org/problems/peak-element/1",
        "pattern": "Binary Search on Gradient / Slope",
        "time_complexity": "O(log N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Meta",
            "Google",
            "Amazon",
            "Microsoft"
        ]
    },
    {
        "category": "Binary Search",
        "title": "Search a 2D Matrix",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/search-a-2d-matrix/",
        "alternate_title": "Search in a row-column sorted Matrix",
        "alternate_url": "https://www.geeksforgeeks.org/problems/search-in-a-matrix-1587115621/1",
        "pattern": "Virtual 1D Array Binary Search",
        "time_complexity": "O(log(M * N))",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Microsoft",
            "Amazon",
            "Meta",
            "Google",
            "Apple"
        ]
    },
    {
        "category": "Binary Search",
        "title": "Search a 2D Matrix II",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/search-a-2d-matrix-ii/",
        "alternate_title": "Search in a Matrix II",
        "alternate_url": "https://www.geeksforgeeks.org/problems/search-in-a-matrix-ii/1",
        "pattern": "Top-Right Corner Pointer Walk / Step Search",
        "time_complexity": "O(M + N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Two Pointers"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Google",
            "Meta",
            "Apple"
        ]
    },
    {
        "category": "Binary Search",
        "title": "Koko Eating Bananas",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/koko-eating-bananas/",
        "alternate_title": "Koko Eating Bananas",
        "alternate_url": "https://www.geeksforgeeks.org/problems/koko-eating-bananas/1",
        "pattern": "Binary Search on Answer Range (Feasibility Function)",
        "time_complexity": "O(N log(max(P)))",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Binary Search on Answer Range"
        ],
        "companies": [
            "Google",
            "Amazon",
            "Meta",
            "Airbnb"
        ]
    },
    {
        "category": "Binary Search",
        "title": "Capacity To Ship Packages Within D Days",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/",
        "alternate_title": "Capacity To Ship Packages Within D Days",
        "alternate_url": "https://www.geeksforgeeks.org/problems/capacity-to-ship-packages-within-d-days/1",
        "pattern": "Binary Search on Capacity Answer Range",
        "time_complexity": "O(N log(Sum - Max))",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Binary Search on Answer Range"
        ],
        "companies": [
            "Google",
            "Amazon",
            "Meta"
        ]
    },
    {
        "category": "Binary Search",
        "title": "Allocate Minimum Pages (Book Allocation)",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/split-array-largest-sum/",
        "alternate_title": "Allocate Minimum Pages",
        "alternate_url": "https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1",
        "pattern": "Binary Search on Max Pages Limit (Painter's Partition)",
        "time_complexity": "O(N log(Sum - Max))",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Binary Search on Answer Range"
        ],
        "companies": [
            "Google",
            "Amazon",
            "Flipkart",
            "Microsoft"
        ]
    },
    {
        "category": "Binary Search",
        "title": "Aggressive Cows",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/magnetic-force-between-two-balls/",
        "alternate_title": "Aggressive Cows",
        "alternate_url": "https://www.geeksforgeeks.org/problems/aggressive-cows/1",
        "pattern": "Binary Search on Minimum Distance Feasibility",
        "time_complexity": "O(N log N + N log(MaxDist))",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Binary Search on Answer Range"
        ],
        "companies": [
            "Amazon",
            "Google",
            "DE Shaw"
        ]
    },
    {
        "category": "Binary Search",
        "title": "Median of Two Sorted Arrays",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/median-of-two-sorted-arrays/",
        "alternate_title": "Median of 2 Sorted Arrays of Different Sizes",
        "alternate_url": "https://www.geeksforgeeks.org/problems/median-of-2-sorted-arrays-of-different-sizes/1",
        "pattern": "Binary Search Partition on Shorter Array",
        "time_complexity": "O(log(min(M, N)))",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon",
            "Microsoft",
            "Meta",
            "Apple",
            "Uber",
            "Goldman Sachs"
        ]
    },
    {
        "category": "Binary Search",
        "title": "Kth Element of Two Sorted Arrays",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/",
        "alternate_title": "K-th element of two Arrays",
        "alternate_url": "https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1225/1",
        "pattern": "Binary Search Dual Partition (K elements left)",
        "time_complexity": "O(log(min(M, N)))",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon",
            "Microsoft"
        ]
    },
    {
        "category": "Binary Search",
        "title": "Find K-th Smallest Pair Distance",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/find-k-th-smallest-pair-distance/",
        "alternate_title": "Smallest Absolute Difference",
        "alternate_url": "https://www.geeksforgeeks.org/problems/smallest-absolute-difference/1",
        "pattern": "Binary Search on Distance + Two Pointers Count",
        "time_complexity": "O(N log N + N log(MaxDist))",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Binary Search on Answer Range",
            "Two Pointers"
        ],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "Binary Search",
        "title": "Single Element in a Sorted Array",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/single-element-in-a-sorted-array/",
        "alternate_title": "Find the element that appears once in sorted array",
        "alternate_url": "https://www.geeksforgeeks.org/problems/find-the-element-that-appears-once-in-sorted-array0624/1",
        "pattern": "Binary Search Even-Odd Index Parity",
        "time_complexity": "O(log N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Bit Manipulation"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Google",
            "Meta"
        ]
    },
    {
        "category": "Binary Search",
        "title": "Sqrt(x)",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/sqrtx/",
        "alternate_title": "Square root of a number",
        "alternate_url": "https://www.geeksforgeeks.org/problems/square-root/1",
        "pattern": "Binary Search on Integer Range [1, X]",
        "time_complexity": "O(log X)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Binary Search on Answer Range"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Apple",
            "Bloomberg"
        ]
    },
    {
        "category": "Linked List",
        "title": "Reverse Linked List",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/reverse-linked-list/",
        "alternate_title": "Reverse a linked list",
        "alternate_url": "https://www.geeksforgeeks.org/problems/reverse-a-linked-list/1",
        "pattern": "Iterative 3-Pointer Reversal / Recursive",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Microsoft",
            "Amazon",
            "Google",
            "Meta",
            "Apple",
            "Bloomberg"
        ]
    },
    {
        "category": "Linked List",
        "title": "Linked List Cycle",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/linked-list-cycle/",
        "alternate_title": "Detect Loop in linked list",
        "alternate_url": "https://www.geeksforgeeks.org/problems/detect-loop-in-linked-list/1",
        "pattern": "Floyd's Tortoise and Hare (Slow & Fast Pointers)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Floyd's Tortoise & Hare",
            "Two Pointers"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Meta",
            "Google",
            "Apple"
        ]
    },
    {
        "category": "Linked List",
        "title": "Linked List Cycle II",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/linked-list-cycle-ii/",
        "alternate_title": "Find the first node of loop in linked list",
        "alternate_url": "https://www.geeksforgeeks.org/problems/find-the-first-node-of-loop-in-linked-list--170645/1",
        "pattern": "Floyd's Tortoise & Hare (Cycle Start Distance Math)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Floyd's Tortoise & Hare",
            "Two Pointers"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Google",
            "Meta"
        ]
    },
    {
        "category": "Linked List",
        "title": "Merge Two Sorted Lists",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/merge-two-sorted-lists/",
        "alternate_title": "Merge two sorted linked lists",
        "alternate_url": "https://www.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1",
        "pattern": "Dummy Head Two Pointer Stitching",
        "time_complexity": "O(M + N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Two Pointers"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Meta",
            "Google",
            "Apple",
            "Bloomberg"
        ]
    },
    {
        "category": "Linked List",
        "title": "Merge k Sorted Lists",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/merge-k-sorted-lists/",
        "alternate_title": "Merge K sorted linked lists",
        "alternate_url": "https://www.geeksforgeeks.org/problems/merge-k-sorted-linked-lists/1",
        "pattern": "Min Heap Priority Queue / Divide and Conquer",
        "time_complexity": "O(N log K)",
        "space_complexity": "O(K)",
        "secondary_topics": [
            "Heap / Priority Queue"
        ],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Microsoft",
            "Uber",
            "Apple",
            "ByteDance"
        ]
    },
    {
        "category": "Linked List",
        "title": "Remove Nth Node From End of List",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/remove-nth-node-from-end-of-list/",
        "alternate_title": "Nth node from end of linked list",
        "alternate_url": "https://www.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1",
        "pattern": "Two Pointers with N-Gap Delay",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Two Pointers"
        ],
        "companies": [
            "Amazon",
            "Meta",
            "Google",
            "Microsoft",
            "Apple"
        ]
    },
    {
        "category": "Linked List",
        "title": "Reorder List",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/reorder-list/",
        "alternate_title": "Reorder List",
        "alternate_url": "https://www.geeksforgeeks.org/problems/reorder-list/1",
        "pattern": "Find Middle + Reverse Second Half + Interweave",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Two Pointers"
        ],
        "companies": [
            "Amazon",
            "Meta",
            "Google",
            "Microsoft",
            "Bloomberg"
        ]
    },
    {
        "category": "Linked List",
        "title": "Copy List with Random Pointer",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/copy-list-with-random-pointer/",
        "alternate_title": "Clone a linked list with next and random pointer",
        "alternate_url": "https://www.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1",
        "pattern": "Interleaving Cloned Nodes (O(1) Auxiliary Space)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "HashMap / HashSet"
        ],
        "companies": [
            "Amazon",
            "Meta",
            "Microsoft",
            "Google",
            "Bloomberg"
        ]
    },
    {
        "category": "Linked List",
        "title": "Add Two Numbers",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/add-two-numbers/",
        "alternate_title": "Add two numbers represented by linked lists",
        "alternate_url": "https://www.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1",
        "pattern": "Elementary Digit Addition with Carry",
        "time_complexity": "O(max(M, N))",
        "space_complexity": "O(max(M, N))",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Meta",
            "Microsoft",
            "Google",
            "Apple",
            "Bloomberg"
        ]
    },
    {
        "category": "Linked List",
        "title": "LRU Cache",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/lru-cache/",
        "alternate_title": "LRU Cache",
        "alternate_url": "https://www.geeksforgeeks.org/problems/lru-cache/1",
        "pattern": "Doubly Linked List + Hash Map Design",
        "time_complexity": "O(1) get & put",
        "space_complexity": "O(Capacity)",
        "secondary_topics": [
            "HashMap / HashSet"
        ],
        "companies": [
            "Amazon",
            "Meta",
            "Google",
            "Microsoft",
            "Bloomberg",
            "Uber",
            "Apple",
            "Netflix",
            "Atlassian",
            "ByteDance"
        ]
    },
    {
        "category": "Linked List",
        "title": "LFU Cache",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/lfu-cache/",
        "alternate_title": "LFU Cache",
        "alternate_url": "https://www.geeksforgeeks.org/problems/lfu-cache/1",
        "pattern": "Frequency Hash Map + Frequency-Bucketed DLLs",
        "time_complexity": "O(1) get & put",
        "space_complexity": "O(Capacity)",
        "secondary_topics": [
            "HashMap / HashSet"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Microsoft",
            "Meta"
        ]
    },
    {
        "category": "Linked List",
        "title": "Reverse Nodes in k-Group",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/reverse-nodes-in-k-group/",
        "alternate_title": "Reverse a Linked List in groups of given size",
        "alternate_url": "https://www.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1",
        "pattern": "Segmented Sublist Reversal with Pointers",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Microsoft",
            "Google",
            "Meta",
            "ByteDance"
        ]
    },
    {
        "category": "Linked List",
        "title": "Intersection of Two Linked Lists",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/intersection-of-two-linked-lists/",
        "alternate_title": "Intersection Point in Y Shapped Lists",
        "alternate_url": "https://www.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1",
        "pattern": "Two Pointers Pointer Swap Cycle Trick",
        "time_complexity": "O(M + N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Two Pointers"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Meta",
            "Google",
            "Apple",
            "Bloomberg"
        ]
    },
    {
        "category": "Linked List",
        "title": "Palindrome Linked List",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/palindrome-linked-list/",
        "alternate_title": "Check if Linked List is Palindrome",
        "alternate_url": "https://www.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1",
        "pattern": "Find Middle + Reverse Second Half + Compare",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Two Pointers"
        ],
        "companies": [
            "Amazon",
            "Meta",
            "Microsoft",
            "Google",
            "Apple"
        ]
    },
    {
        "category": "Linked List",
        "title": "Flatten a Multilevel Doubly Linked List",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/",
        "alternate_title": "Flattening a Linked List",
        "alternate_url": "https://www.geeksforgeeks.org/problems/flattening-a-linked-list/1",
        "pattern": "DFS Traversal / Stack Multilevel Stitching",
        "time_complexity": "O(N)",
        "space_complexity": "O(Depth)",
        "secondary_topics": [
            "Recursion and Backtracking"
        ],
        "companies": [
            "Bloomberg",
            "Amazon",
            "Microsoft"
        ]
    },
    {
        "category": "Linked List",
        "title": "Sort List",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/sort-list/",
        "alternate_title": "Sort a linked list",
        "alternate_url": "https://www.geeksforgeeks.org/problems/sort-a-linked-list/1",
        "pattern": "Merge Sort on Linked List (Fast/Slow Middle)",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(log N)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Meta",
            "Google",
            "Microsoft"
        ]
    },
    {
        "category": "Recursion and Backtracking",
        "title": "Subsets",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/subsets/",
        "alternate_title": "Subsets",
        "alternate_url": "https://www.geeksforgeeks.org/problems/subsets-1613027340/1",
        "pattern": "Backtracking Choice Tree (Include / Exclude)",
        "time_complexity": "O(N * 2^N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Backtracking & Pruning",
            "Bit Manipulation"
        ],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Microsoft",
            "Bloomberg",
            "Uber"
        ]
    },
    {
        "category": "Recursion and Backtracking",
        "title": "Subsets II",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/subsets-ii/",
        "alternate_title": "Subset II",
        "alternate_url": "https://www.geeksforgeeks.org/problems/subset-ii/1",
        "pattern": "Backtracking with Duplicate Sibling Pruning",
        "time_complexity": "O(N * 2^N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Backtracking & Pruning"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Meta"
        ]
    },
    {
        "category": "Recursion and Backtracking",
        "title": "Combination Sum",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/combination-sum/",
        "alternate_title": "Combination Sum",
        "alternate_url": "https://www.geeksforgeeks.org/problems/combination-sum-1587115620/1",
        "pattern": "Backtracking with Unbounded Candidate Reuse",
        "time_complexity": "O(2^(Target/Min))",
        "space_complexity": "O(Target/Min)",
        "secondary_topics": [
            "Backtracking & Pruning"
        ],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Microsoft",
            "Airbnb"
        ]
    },
    {
        "category": "Recursion and Backtracking",
        "title": "Combination Sum II",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/combination-sum-ii/",
        "alternate_title": "Combination Sum II",
        "alternate_url": "https://www.geeksforgeeks.org/problems/combination-sum-ii/1",
        "pattern": "Backtracking with Sorted Candidate Pruning",
        "time_complexity": "O(2^N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Backtracking & Pruning"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Meta"
        ]
    },
    {
        "category": "Recursion and Backtracking",
        "title": "Permutations",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/permutations/",
        "alternate_title": "Permutations of a String",
        "alternate_url": "https://www.geeksforgeeks.org/problems/permutations-of-a-given-string2041/1",
        "pattern": "Backtracking Swap / Used Boolean Array",
        "time_complexity": "O(N * N!)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Backtracking & Pruning"
        ],
        "companies": [
            "Meta",
            "Amazon",
            "Microsoft",
            "Google",
            "LinkedIn"
        ]
    },
    {
        "category": "Recursion and Backtracking",
        "title": "Permutations II",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/permutations-ii/",
        "alternate_title": "Unique Permutations of an Array",
        "alternate_url": "https://www.geeksforgeeks.org/problems/unique-permutations/1",
        "pattern": "Backtracking with Sorted Frequency Map",
        "time_complexity": "O(N * N!)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Backtracking & Pruning"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Microsoft"
        ]
    },
    {
        "category": "Recursion and Backtracking",
        "title": "Word Search",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/word-search/",
        "alternate_title": "Word Search",
        "alternate_url": "https://www.geeksforgeeks.org/problems/word-search/1",
        "pattern": "Grid DFS Backtracking with In-Place Visited Masking",
        "time_complexity": "O(M * N * 3^L)",
        "space_complexity": "O(L)",
        "secondary_topics": [
            "Backtracking & Pruning"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Meta",
            "Google",
            "Bloomberg",
            "Uber"
        ]
    },
    {
        "category": "Recursion and Backtracking",
        "title": "Letter Combinations of a Phone Number",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/letter-combinations-of-a-phone-number/",
        "alternate_title": "Possible Words From Phone Digits",
        "alternate_url": "https://www.geeksforgeeks.org/problems/possible-words-from-phone-digits-1587115620/1",
        "pattern": "Digit-to-Letter Recursive Cartesian Product",
        "time_complexity": "O(4^N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Backtracking & Pruning"
        ],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Microsoft",
            "Uber"
        ]
    },
    {
        "category": "Recursion and Backtracking",
        "title": "Palindrome Partitioning",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/palindrome-partitioning/",
        "alternate_title": "Find all possible palindromic partitions of a String",
        "alternate_url": "https://www.geeksforgeeks.org/problems/find-all-possible-palindromic-partitions-of-a-string/1",
        "pattern": "Backtracking with Palindrome Substring Validation",
        "time_complexity": "O(N * 2^N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Backtracking & Pruning",
            "DP on Strings"
        ],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Bloomberg"
        ]
    },
    {
        "category": "Recursion and Backtracking",
        "title": "N-Queens",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/n-queens/",
        "alternate_title": "N-Queen Problem",
        "alternate_url": "https://www.geeksforgeeks.org/problems/n-queen-problem0315/1",
        "pattern": "Backtracking with Column & Diagonal Hash Sets",
        "time_complexity": "O(N!)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Backtracking & Pruning"
        ],
        "companies": [
            "Google",
            "Amazon",
            "Microsoft",
            "Meta"
        ]
    },
    {
        "category": "Recursion and Backtracking",
        "title": "Sudoku Solver",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/sudoku-solver/",
        "alternate_title": "Solve the Sudoku",
        "alternate_url": "https://www.geeksforgeeks.org/problems/solve-the-sudoku-1587115621/1",
        "pattern": "Backtracking Constraint Satisfaction with Row/Col/Box Checks",
        "time_complexity": "O(9^(Empty Cells))",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Backtracking & Pruning"
        ],
        "companies": [
            "Google",
            "Amazon",
            "Microsoft",
            "Meta",
            "Uber"
        ]
    },
    {
        "category": "Recursion and Backtracking",
        "title": "Generate Parentheses",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/generate-parentheses/",
        "alternate_title": "Generate all binary strings without consecutive 1\u2019s",
        "alternate_url": "https://www.geeksforgeeks.org/problems/generate-all-balanced-parentheses/1",
        "pattern": "Backtracking with Open/Close Count Pruning",
        "time_complexity": "O(4^N / sqrt(N)) (Catalan)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Backtracking & Pruning"
        ],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Microsoft",
            "Apple",
            "Uber"
        ]
    },
    {
        "category": "Recursion and Backtracking",
        "title": "Rat in a Maze Problem",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/unique-paths-iii/",
        "alternate_title": "Rat in a Maze Problem - I",
        "alternate_url": "https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1",
        "pattern": "Grid 4-Directional DFS with Visited Backtracking",
        "time_complexity": "O(4^(N^2))",
        "space_complexity": "O(N^2)",
        "secondary_topics": [
            "Backtracking & Pruning"
        ],
        "companies": [
            "Amazon",
            "Microsoft"
        ]
    },
    {
        "category": "Recursion and Backtracking",
        "title": "M-Coloring Problem",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/flower-planting-with-no-adjacent/",
        "alternate_title": "M-Coloring Problem",
        "alternate_url": "https://www.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1",
        "pattern": "Graph Vertex Color Backtracking",
        "time_complexity": "O(M^V)",
        "space_complexity": "O(V)",
        "secondary_topics": [
            "Backtracking & Pruning",
            "Graph BFS/DFS"
        ],
        "companies": [
            "Amazon",
            "Microsoft"
        ]
    },
    {
        "category": "Recursion and Backtracking",
        "title": "Power (x, n)",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/powx-n/",
        "alternate_title": "Modular Exponentiation for large numbers",
        "alternate_url": "https://www.geeksforgeeks.org/problems/modular-exponentiation-for-large-numbers5537/1",
        "pattern": "Binary Exponentiation (Divide and Conquer)",
        "time_complexity": "O(log N)",
        "space_complexity": "O(log N)",
        "secondary_topics": [
            "Bit Manipulation"
        ],
        "companies": [
            "Meta",
            "Google",
            "Amazon",
            "Microsoft",
            "LinkedIn"
        ]
    },
    {
        "category": "Recursion and Backtracking",
        "title": "Tower of Hanoi",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/minimum-moves-to-reach-target-score/",
        "alternate_title": "Tower Of Hanoi",
        "alternate_url": "https://www.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1",
        "pattern": "Classic 3-Peg Recursion Decomposition",
        "time_complexity": "O(2^N)",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Microsoft"
        ]
    },
    {
        "category": "Trees / BST",
        "title": "Maximum Depth of Binary Tree",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/maximum-depth-of-binary-tree/",
        "alternate_title": "Height of Binary Tree",
        "alternate_url": "https://www.geeksforgeeks.org/problems/height-of-binary-tree/1",
        "pattern": "Post-Order Tree DFS (1 + max(left, right))",
        "time_complexity": "O(N)",
        "space_complexity": "O(H)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Google",
            "Meta",
            "Microsoft",
            "Apple",
            "LinkedIn"
        ]
    },
    {
        "category": "Trees / BST",
        "title": "Invert Binary Tree",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/invert-binary-tree/",
        "alternate_title": "Mirror Tree",
        "alternate_url": "https://www.geeksforgeeks.org/problems/mirror-tree/1",
        "pattern": "Recursive Left/Right Subtree Swap",
        "time_complexity": "O(N)",
        "space_complexity": "O(H)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon",
            "Meta",
            "Microsoft",
            "Apple"
        ]
    },
    {
        "category": "Trees / BST",
        "title": "Diameter of Binary Tree",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/diameter-of-binary-tree/",
        "alternate_title": "Diameter of a Binary Tree",
        "alternate_url": "https://www.geeksforgeeks.org/problems/diameter-of-binary-tree/1",
        "pattern": "Bottom-Up DFS with Global Max (leftHeight + rightHeight)",
        "time_complexity": "O(N)",
        "space_complexity": "O(H)",
        "secondary_topics": [],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Microsoft",
            "Bloomberg"
        ]
    },
    {
        "category": "Trees / BST",
        "title": "Balanced Binary Tree",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/balanced-binary-tree/",
        "alternate_title": "Check for Balanced Tree",
        "alternate_url": "https://www.geeksforgeeks.org/problems/check-for-balanced-tree/1",
        "pattern": "Bottom-Up Height Checking (Return -1 on Imbalance)",
        "time_complexity": "O(N)",
        "space_complexity": "O(H)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Google",
            "Meta",
            "Microsoft",
            "Apple"
        ]
    },
    {
        "category": "Trees / BST",
        "title": "Same Tree",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/same-tree/",
        "alternate_title": "Determine if Two Trees are Identical",
        "alternate_url": "https://www.geeksforgeeks.org/problems/determine-if-two-trees-are-identical/1",
        "pattern": "Simultaneous Dual Tree DFS Traversal",
        "time_complexity": "O(N)",
        "space_complexity": "O(H)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Google",
            "Microsoft",
            "Meta",
            "Apple"
        ]
    },
    {
        "category": "Trees / BST",
        "title": "Symmetric Tree",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/symmetric-tree/",
        "alternate_title": "Symmetric Tree",
        "alternate_url": "https://www.geeksforgeeks.org/problems/symmetric-tree/1",
        "pattern": "Mirror Dual DFS (t1.left vs t2.right)",
        "time_complexity": "O(N)",
        "space_complexity": "O(H)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Google",
            "Microsoft",
            "Meta",
            "Bloomberg"
        ]
    },
    {
        "category": "Trees / BST",
        "title": "Binary Tree Level Order Traversal",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/binary-tree-level-order-traversal/",
        "alternate_title": "Level order traversal",
        "alternate_url": "https://www.geeksforgeeks.org/problems/level-order-traversal/1",
        "pattern": "BFS Queue with Current Level Size Snapshot",
        "time_complexity": "O(N)",
        "space_complexity": "O(W)",
        "secondary_topics": [
            "Queue / Deque"
        ],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Microsoft",
            "Bloomberg",
            "LinkedIn"
        ]
    },
    {
        "category": "Trees / BST",
        "title": "Binary Tree Zigzag Level Order Traversal",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/",
        "alternate_title": "ZigZag Tree Traversal",
        "alternate_url": "https://www.geeksforgeeks.org/problems/zigzag-tree-traversal/1",
        "pattern": "BFS with Level Alternating Deque Direction",
        "time_complexity": "O(N)",
        "space_complexity": "O(W)",
        "secondary_topics": [
            "Queue / Deque"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Meta",
            "Google",
            "Bloomberg"
        ]
    },
    {
        "category": "Trees / BST",
        "title": "Lowest Common Ancestor of a Binary Tree",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/",
        "alternate_title": "Lowest Common Ancestor in a Binary Tree",
        "alternate_url": "https://www.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-binary-tree/1",
        "pattern": "Post-Order DFS (Propagate Left & Right Match)",
        "time_complexity": "O(N)",
        "space_complexity": "O(H)",
        "secondary_topics": [],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Microsoft",
            "Apple",
            "Uber",
            "Bloomberg"
        ]
    },
    {
        "category": "Trees / BST",
        "title": "Lowest Common Ancestor of a Binary Search Tree",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/",
        "alternate_title": "Lowest Common Ancestor in a BST",
        "alternate_url": "https://www.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-bst/1",
        "pattern": "BST Property Splitting Point Navigation",
        "time_complexity": "O(H)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Meta",
            "Microsoft",
            "Google",
            "Apple"
        ]
    },
    {
        "category": "Trees / BST",
        "title": "Validate Binary Search Tree",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/validate-binary-search-tree/",
        "alternate_title": "Check for BST",
        "alternate_url": "https://www.geeksforgeeks.org/problems/check-for-bst/1",
        "pattern": "DFS with (MinVal, MaxVal) Valid Range Propagation",
        "time_complexity": "O(N)",
        "space_complexity": "O(H)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Meta",
            "Microsoft",
            "Google",
            "Bloomberg",
            "Netflix"
        ]
    },
    {
        "category": "Trees / BST",
        "title": "Kth Smallest Element in a BST",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/kth-smallest-element-in-a-bst/",
        "alternate_title": "Find K-th smallest element in BST",
        "alternate_url": "https://www.geeksforgeeks.org/problems/find-k-th-smallest-element-in-bst/1",
        "pattern": "Inorder Traversal (Sorted Order Step Count)",
        "time_complexity": "O(H + K)",
        "space_complexity": "O(H)",
        "secondary_topics": [
            "Morris Inorder Traversal"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Meta",
            "Microsoft",
            "Uber"
        ]
    },
    {
        "category": "Trees / BST",
        "title": "Binary Tree Right Side View",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/binary-tree-right-side-view/",
        "alternate_title": "Right View of Binary Tree",
        "alternate_url": "https://www.geeksforgeeks.org/problems/right-view-of-binary-tree/1",
        "pattern": "Reverse Pre-Order DFS (Root -> Right -> Left) / BFS Level End",
        "time_complexity": "O(N)",
        "space_complexity": "O(H)",
        "secondary_topics": [],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Bloomberg",
            "Microsoft"
        ]
    },
    {
        "category": "Trees / BST",
        "title": "Construct Binary Tree from Preorder and Inorder Traversal",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/",
        "alternate_title": "Construct Tree from Inorder & Preorder",
        "alternate_url": "https://www.geeksforgeeks.org/problems/construct-tree-1/1",
        "pattern": "Preorder Root Index + Inorder Hash Map Partition",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "HashMap / HashSet"
        ],
        "companies": [
            "Amazon",
            "Meta",
            "Microsoft",
            "Google",
            "Bloomberg"
        ]
    },
    {
        "category": "Trees / BST",
        "title": "Binary Tree Maximum Path Sum",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/binary-tree-maximum-path-sum/",
        "alternate_title": "Maximum Path Sum between 2 Special Nodes",
        "alternate_url": "https://www.geeksforgeeks.org/problems/maximum-path-sum/1",
        "pattern": "Post-Order DFS (Max Gain Contribution + Local Apex Sum)",
        "time_complexity": "O(N)",
        "space_complexity": "O(H)",
        "secondary_topics": [],
        "companies": [
            "Meta",
            "Google",
            "Amazon",
            "Microsoft",
            "Apple",
            "ByteDance"
        ]
    },
    {
        "category": "Trees / BST",
        "title": "Serialize and Deserialize Binary Tree",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/serialize-and-deserialize-binary-tree/",
        "alternate_title": "Serialize and deserialize a binary tree",
        "alternate_url": "https://www.geeksforgeeks.org/problems/serialize-and-deserialize-a-binary-tree/1",
        "pattern": "Pre-Order DFS with Null Markers / BFS Queue Encoding",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Queue / Deque"
        ],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Microsoft",
            "Uber",
            "LinkedIn"
        ]
    },
    {
        "category": "Trees / BST",
        "title": "Morris Inorder Traversal",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/binary-tree-inorder-traversal/",
        "alternate_title": "Inorder Traversal (Morris Traversal)",
        "alternate_url": "https://www.geeksforgeeks.org/problems/inorder-traversal/1",
        "pattern": "Morris Traversal (Threaded Binary Tree O(1) Space)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Morris Inorder Traversal"
        ],
        "companies": [
            "Microsoft",
            "Amazon",
            "Google"
        ]
    },
    {
        "category": "Trees / BST",
        "title": "Top View of Binary Tree",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/",
        "alternate_title": "Top View of Binary Tree",
        "alternate_url": "https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1",
        "pattern": "BFS Horizontal Distance (HD) Hash Map",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "HashMap / HashSet"
        ],
        "companies": [
            "Amazon",
            "PayPal",
            "Paytm"
        ]
    },
    {
        "category": "Trees / BST",
        "title": "Bottom View of Binary Tree",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/",
        "alternate_title": "Bottom View of Binary Tree",
        "alternate_url": "https://www.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1",
        "pattern": "BFS Horizontal Distance Overwrite Map",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "HashMap / HashSet"
        ],
        "companies": [
            "Amazon",
            "Flipkart",
            "Paytm"
        ]
    },
    {
        "category": "Trees / BST",
        "title": "Boundary Traversal of Binary Tree",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/boundary-of-binary-tree/",
        "alternate_title": "Boundary Traversal of binary tree",
        "alternate_url": "https://www.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1",
        "pattern": "Left Boundary + Leaves (Inorder) + Right Boundary (Reversed)",
        "time_complexity": "O(N)",
        "space_complexity": "O(H)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Microsoft",
            "Google",
            "Paytm"
        ]
    },
    {
        "category": "Trees / BST",
        "title": "Count Complete Tree Nodes",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/count-complete-tree-nodes/",
        "alternate_title": "Count Complete Tree Nodes",
        "alternate_url": "https://www.geeksforgeeks.org/problems/count-number-of-nodes-in-a-binary-tree/1",
        "pattern": "Binary Search on Leaf Level + Bit Manipulation",
        "time_complexity": "O((log N)^2)",
        "space_complexity": "O(log N)",
        "secondary_topics": [
            "Binary Search"
        ],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "Trees / BST",
        "title": "All Nodes Distance K in Binary Tree",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/",
        "alternate_title": "Nodes at given distance in binary tree",
        "alternate_url": "https://www.geeksforgeeks.org/problems/nodes-at-given-distance-in-binary-tree/1",
        "pattern": "Parent Pointer Mapping + BFS Radial Wave",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Graph BFS/DFS",
            "HashMap / HashSet"
        ],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Microsoft"
        ]
    },
    {
        "category": "Trees / BST",
        "title": "Recover Binary Search Tree",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/recover-binary-search-tree/",
        "alternate_title": "Fixing Two nodes of a BST",
        "alternate_url": "https://www.geeksforgeeks.org/problems/fixed-two-nodes-of-a-bst/1",
        "pattern": "Inorder Traversal (Detect 2 Inversion Nodes)",
        "time_complexity": "O(N)",
        "space_complexity": "O(H) or O(1) Morris",
        "secondary_topics": [
            "Morris Inorder Traversal"
        ],
        "companies": [
            "Google",
            "Amazon",
            "Microsoft"
        ]
    },
    {
        "category": "Trees / BST",
        "title": "Maximum Width of Binary Tree",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/maximum-width-of-binary-tree/",
        "alternate_title": "Maximum Width of Tree",
        "alternate_url": "https://www.geeksforgeeks.org/problems/maximum-width-of-tree/1",
        "pattern": "BFS with Normalized 0-Indexed Node Indexing",
        "time_complexity": "O(N)",
        "space_complexity": "O(W)",
        "secondary_topics": [
            "Queue / Deque"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Bloomberg"
        ]
    },
    {
        "category": "Heap / Priority Queue",
        "title": "Kth Largest Element in an Array",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/kth-largest-element-in-an-array/",
        "alternate_title": "Kth largest element in an array",
        "alternate_url": "https://www.geeksforgeeks.org/problems/k-largest-elements3736/1",
        "pattern": "Min Heap of Size K / Quickselect",
        "time_complexity": "O(N log K) or O(N) Quickselect",
        "space_complexity": "O(K)",
        "secondary_topics": [],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Microsoft",
            "Apple",
            "Bloomberg"
        ]
    },
    {
        "category": "Heap / Priority Queue",
        "title": "Find Median from Data Stream",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/find-median-from-data-stream/",
        "alternate_title": "Find median in a stream",
        "alternate_url": "https://www.geeksforgeeks.org/problems/find-median-in-a-stream-1587115620/1",
        "pattern": "Two Heaps (MaxHeap for Lowers, MinHeap for Uppers)",
        "time_complexity": "O(log N) insert, O(1) findMedian",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon",
            "Meta",
            "Microsoft",
            "Apple",
            "Uber",
            "Goldman Sachs"
        ]
    },
    {
        "category": "Heap / Priority Queue",
        "title": "Merge k Sorted Lists",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/merge-k-sorted-lists/",
        "alternate_title": "Merge K sorted linked lists",
        "alternate_url": "https://www.geeksforgeeks.org/problems/merge-k-sorted-linked-lists/1",
        "pattern": "Min-Heap of Size K with Head Pointers",
        "time_complexity": "O(N log K)",
        "space_complexity": "O(K)",
        "secondary_topics": [
            "Linked List"
        ],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Microsoft",
            "Uber",
            "Apple",
            "ByteDance"
        ]
    },
    {
        "category": "Heap / Priority Queue",
        "title": "Task Scheduler",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/task-scheduler/",
        "alternate_title": "Task Scheduler",
        "alternate_url": "https://www.geeksforgeeks.org/problems/task-scheduler/1",
        "pattern": "Max Heap Greedy Frequency / Math Slots",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Queue / Deque"
        ],
        "companies": [
            "Meta",
            "Google",
            "Amazon",
            "Microsoft",
            "Uber"
        ]
    },
    {
        "category": "Heap / Priority Queue",
        "title": "K Closest Points to Origin",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/k-closest-points-to-origin/",
        "alternate_title": "K Closest Points to Origin",
        "alternate_url": "https://www.geeksforgeeks.org/problems/k-closest-points-to-origin/1",
        "pattern": "Max Heap of Size K on Euclidean Distance",
        "time_complexity": "O(N log K)",
        "space_complexity": "O(K)",
        "secondary_topics": [],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "LinkedIn",
            "Apple",
            "Uber"
        ]
    },
    {
        "category": "Heap / Priority Queue",
        "title": "Reorganize String",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/reorganize-string/",
        "alternate_title": "Rearrange characters in a string such that no two adjacent are same",
        "alternate_url": "https://www.geeksforgeeks.org/problems/rearrange-characters4649/1",
        "pattern": "Max Heap (Alternate Frequent Characters)",
        "time_complexity": "O(N log A)",
        "space_complexity": "O(A)",
        "secondary_topics": [
            "HashMap / HashSet"
        ],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Microsoft"
        ]
    },
    {
        "category": "Heap / Priority Queue",
        "title": "Connect Ropes to Minimise Cost",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/minimum-cost-to-connect-sticks/",
        "alternate_title": "Minimum Cost of ropes",
        "alternate_url": "https://www.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1",
        "pattern": "Min Heap Greedy (Huffman Merge)",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Goldman Sachs",
            "Google"
        ]
    },
    {
        "category": "Heap / Priority Queue",
        "title": "Kth Largest Element in a Stream",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/kth-largest-element-in-a-stream/",
        "alternate_title": "Kth largest element in a stream",
        "alternate_url": "https://www.geeksforgeeks.org/problems/kth-largest-element-in-a-stream2220/1",
        "pattern": "Fixed-Size Min Heap of Size K",
        "time_complexity": "O(log K) per add",
        "space_complexity": "O(K)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Google",
            "Meta"
        ]
    },
    {
        "category": "Heap / Priority Queue",
        "title": "Design Twitter",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/design-twitter/",
        "alternate_title": "Design Twitter",
        "alternate_url": "https://www.geeksforgeeks.org/problems/design-twitter/1",
        "pattern": "Hash Map Follower Graph + K-Way Merge Heap",
        "time_complexity": "O(K log F) getNewsFeed",
        "space_complexity": "O(U + T)",
        "secondary_topics": [
            "HashMap / HashSet"
        ],
        "companies": [
            "Twitter / X",
            "Amazon",
            "Meta",
            "Google"
        ]
    },
    {
        "category": "Heap / Priority Queue",
        "title": "Smallest Range Covering Elements from K Lists",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/",
        "alternate_title": "Smallest range in K lists",
        "alternate_url": "https://www.geeksforgeeks.org/problems/find-smallest-range-containing-elements-from-k-lists/1",
        "pattern": "Min Heap of Size K (Track Current Max & Pop Min)",
        "time_complexity": "O(N log K)",
        "space_complexity": "O(K)",
        "secondary_topics": [
            "Sliding Window"
        ],
        "companies": [
            "Google",
            "Amazon",
            "Meta"
        ]
    },
    {
        "category": "Heap / Priority Queue",
        "title": "Furthest Building You Can Reach",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/furthest-building-you-can-reach/",
        "alternate_title": "Furthest Building Reachable",
        "alternate_url": "https://www.geeksforgeeks.org/problems/furthest-building-you-can-reach/1",
        "pattern": "Min Heap for Largest Climbs (Use Ladders First)",
        "time_complexity": "O(N log L)",
        "space_complexity": "O(L)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "Heap / Priority Queue",
        "title": "Maximum Subsequence Score",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/maximum-subsequence-score/",
        "alternate_title": "Maximum Subsequence Score",
        "alternate_url": "https://www.geeksforgeeks.org/problems/maximum-subsequence-score/1",
        "pattern": "Sorting by Multiplier Descending + Min Heap of Size K",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(K)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Google"
        ]
    },
    {
        "category": "Heap / Priority Queue",
        "title": "Seat Reservation Manager",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/seat-reservation-manager/",
        "alternate_title": "Seat Reservation System",
        "alternate_url": "https://www.geeksforgeeks.org/problems/seat-reservation/1",
        "pattern": "Min Heap for Released Lower Numbered Seats",
        "time_complexity": "O(log N) reserve/unreserve",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Google"
        ]
    },
    {
        "category": "Heap / Priority Queue",
        "title": "Find K Pairs with Smallest Sums",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/find-k-pairs-with-smallest-sums/",
        "alternate_title": "Find K Pairs with Smallest Sums",
        "alternate_url": "https://www.geeksforgeeks.org/problems/k-pairs-with-smallest-sums/1",
        "pattern": "Min Heap Frontier Expansion (i, j + 1)",
        "time_complexity": "O(K log(min(N1, K)))",
        "space_complexity": "O(min(N1, K))",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon",
            "Meta"
        ]
    },
    {
        "category": "Graph BFS/DFS",
        "title": "Number of Islands",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/number-of-islands/",
        "alternate_title": "Find the number of islands",
        "alternate_url": "https://www.geeksforgeeks.org/problems/find-the-number-of-islands/1",
        "pattern": "Connected Components Grid DFS/BFS Sink (Flood Fill)",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(M * N)",
        "secondary_topics": [
            "Union Find"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Meta",
            "Microsoft",
            "Bloomberg",
            "Apple",
            "Uber",
            "LinkedIn"
        ]
    },
    {
        "category": "Graph BFS/DFS",
        "title": "Max Area of Island",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/max-area-of-island/",
        "alternate_title": "Unit Area of largest region of 1s",
        "alternate_url": "https://www.geeksforgeeks.org/problems/length-of-largest-region-of-1s-1587115620/1",
        "pattern": "Grid DFS Area Accumulator",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(M * N)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon",
            "Meta",
            "Microsoft",
            "Bloomberg"
        ]
    },
    {
        "category": "Graph BFS/DFS",
        "title": "Clone Graph",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/clone-graph/",
        "alternate_title": "Clone Graph",
        "alternate_url": "https://www.geeksforgeeks.org/problems/clone-graph/1",
        "pattern": "DFS with Old-to-New Node Hash Map Memo",
        "time_complexity": "O(V + E)",
        "space_complexity": "O(V)",
        "secondary_topics": [
            "HashMap / HashSet"
        ],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Microsoft",
            "Uber"
        ]
    },
    {
        "category": "Graph BFS/DFS",
        "title": "Pacific Atlantic Water Flow",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/pacific-atlantic-water-flow/",
        "alternate_title": "Pacific Atlantic Water Flow",
        "alternate_url": "https://www.geeksforgeeks.org/problems/pacific-atlantic-water-flow/1",
        "pattern": "Reverse DFS from Ocean Coastlines + Set Intersection",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(M * N)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon",
            "Meta",
            "Microsoft"
        ]
    },
    {
        "category": "Graph BFS/DFS",
        "title": "Surrounded Regions",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/surrounded-regions/",
        "alternate_title": "Replace O's with X's",
        "alternate_url": "https://www.geeksforgeeks.org/problems/replace-os-with-xs0037/1",
        "pattern": "Boundary Connected Component DFS (Preserve Edge O's)",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(M * N)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Google",
            "Microsoft"
        ]
    },
    {
        "category": "Graph BFS/DFS",
        "title": "Word Ladder",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/word-ladder/",
        "alternate_title": "Word Ladder I",
        "alternate_url": "https://www.geeksforgeeks.org/problems/word-ladder/1",
        "pattern": "Bi-directional BFS / Shortest Path in Unweighted Graph",
        "time_complexity": "O(N * L * 26)",
        "space_complexity": "O(N * L)",
        "secondary_topics": [
            "Queue / Deque"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Meta",
            "Microsoft",
            "Uber",
            "Apple"
        ]
    },
    {
        "category": "Graph BFS/DFS",
        "title": "Word Ladder II",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/word-ladder-ii/",
        "alternate_title": "Word Ladder II",
        "alternate_url": "https://www.geeksforgeeks.org/problems/word-ladder-ii/1",
        "pattern": "BFS Step Distance DAG + DFS Path Reconstruction",
        "time_complexity": "O(N * L * 26 + Paths)",
        "space_complexity": "O(N * L)",
        "secondary_topics": [
            "Recursion and Backtracking"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Meta",
            "Microsoft"
        ]
    },
    {
        "category": "Graph BFS/DFS",
        "title": "Is Graph Bipartite?",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/is-graph-bipartite/",
        "alternate_title": "Bipartite Graph",
        "alternate_url": "https://www.geeksforgeeks.org/problems/bipartite-graph/1",
        "pattern": "2-Coloring BFS / DFS (Check Odd-Length Cycle)",
        "time_complexity": "O(V + E)",
        "space_complexity": "O(V)",
        "secondary_topics": [],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Microsoft"
        ]
    },
    {
        "category": "Graph BFS/DFS",
        "title": "Network Delay Time",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/network-delay-time/",
        "alternate_title": "Implementing Dijkstra Algorithm",
        "alternate_url": "https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1",
        "pattern": "Dijkstra's Shortest Path Algorithm (Min Heap)",
        "time_complexity": "O((V + E) log V)",
        "space_complexity": "O(V + E)",
        "secondary_topics": [
            "Dijkstra's Algorithm",
            "Heap / Priority Queue"
        ],
        "companies": [
            "Google",
            "Amazon",
            "Meta"
        ]
    },
    {
        "category": "Graph BFS/DFS",
        "title": "Cheapest Flights Within K Stops",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/cheapest-flights-within-k-stops/",
        "alternate_title": "Cheapest Flights Within K Stops",
        "alternate_url": "https://www.geeksforgeeks.org/problems/cheapest-flights-within-k-stops/1",
        "pattern": "Bellman-Ford Algorithm / Modified BFS with Stop Budget",
        "time_complexity": "O(K * E)",
        "space_complexity": "O(V)",
        "secondary_topics": [
            "Bellman-Ford Algorithm",
            "Queue / Deque"
        ],
        "companies": [
            "Airbnb",
            "Amazon",
            "Google",
            "Meta"
        ]
    },
    {
        "category": "Graph BFS/DFS",
        "title": "Shortest Path in Binary Matrix",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/shortest-path-in-binary-matrix/",
        "alternate_title": "Shortest Source to Destination Path",
        "alternate_url": "https://www.geeksforgeeks.org/problems/shortest-source-to-destination-path3544/1",
        "pattern": "8-Directional Level Order BFS",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N^2)",
        "secondary_topics": [
            "Queue / Deque"
        ],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Microsoft"
        ]
    },
    {
        "category": "Graph BFS/DFS",
        "title": "Floyd Warshall All-Pairs Shortest Path",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/",
        "alternate_title": "Floyd Warshall",
        "alternate_url": "https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1",
        "pattern": "Floyd-Warshall Dynamic Programming (All-Pairs)",
        "time_complexity": "O(V^3)",
        "space_complexity": "O(V^2)",
        "secondary_topics": [
            "Floyd-Warshall Algorithm"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Samsung"
        ]
    },
    {
        "category": "Graph BFS/DFS",
        "title": "Critical Connections in a Network (Tarjan's Bridges)",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/critical-connections-in-a-network/",
        "alternate_title": "Bridges in a Graph",
        "alternate_url": "https://www.geeksforgeeks.org/problems/bridge-edge-in-graph/1",
        "pattern": "Tarjan's Algorithm (Time of Insertion & Low-Link)",
        "time_complexity": "O(V + E)",
        "space_complexity": "O(V + E)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Meta",
            "Google"
        ]
    },
    {
        "category": "Graph BFS/DFS",
        "title": "Strongly Connected Components (Kosaraju's Algorithm)",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/all-paths-from-source-to-target/",
        "alternate_title": "Strongly Connected Components (Kosaraju's Algo)",
        "alternate_url": "https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1",
        "pattern": "Kosaraju's Algorithm (DFS Finishing Stack + Transpose DFS)",
        "time_complexity": "O(V + E)",
        "space_complexity": "O(V + E)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Microsoft",
            "Google"
        ]
    },
    {
        "category": "Graph BFS/DFS",
        "title": "Reconstruct Itinerary",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/reconstruct-itinerary/",
        "alternate_title": "Eulerian Path in Directed Graph",
        "alternate_url": "https://www.geeksforgeeks.org/problems/euler-circuit-and-path/1",
        "pattern": "Hierholzer's Algorithm (Eulerian Path Postorder DFS)",
        "time_complexity": "O(E log E)",
        "space_complexity": "O(V + E)",
        "secondary_topics": [
            "Heap / Priority Queue"
        ],
        "companies": [
            "Google",
            "Amazon",
            "Meta",
            "Uber"
        ]
    },
    {
        "category": "Graph BFS/DFS",
        "title": "Detect cycle in an undirected graph",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/redundant-connection/",
        "alternate_title": "Detect cycle in an undirected graph",
        "alternate_url": "https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1",
        "pattern": "Parent-Tracked BFS/DFS Cycle Check",
        "time_complexity": "O(V + E)",
        "space_complexity": "O(V)",
        "secondary_topics": [
            "Union Find"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Google",
            "Adobe"
        ]
    },
    {
        "category": "Graph BFS/DFS",
        "title": "Detect cycle in a directed graph",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/course-schedule/",
        "alternate_title": "Detect cycle in a directed graph",
        "alternate_url": "https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1",
        "pattern": "DFS Recursion Call Stack (Path Visited Array)",
        "time_complexity": "O(V + E)",
        "space_complexity": "O(V)",
        "secondary_topics": [
            "Topological Sort"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Google",
            "Flipkart"
        ]
    },
    {
        "category": "Graph BFS/DFS",
        "title": "Flood Fill",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/flood-fill/",
        "alternate_title": "Flood fill Algorithm",
        "alternate_url": "https://www.geeksforgeeks.org/problems/flood-fill-algorithm1856/1",
        "pattern": "Classic 4-Direction Grid DFS/BFS",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(M * N)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Google",
            "Microsoft",
            "Meta",
            "Apple"
        ]
    },
    {
        "category": "Topological Sort",
        "title": "Course Schedule",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/course-schedule/",
        "alternate_title": "Course Schedule I",
        "alternate_url": "https://www.geeksforgeeks.org/problems/course-schedule/1",
        "pattern": "Kahn's Algorithm (BFS In-Degree Queue) / Cycle Detection",
        "time_complexity": "O(V + E)",
        "space_complexity": "O(V + E)",
        "secondary_topics": [
            "Kahn's Algorithm (BFS Topo)",
            "Graph BFS/DFS"
        ],
        "companies": [
            "Amazon",
            "Meta",
            "Google",
            "Microsoft",
            "Uber",
            "ByteDance",
            "Twitter / X"
        ]
    },
    {
        "category": "Topological Sort",
        "title": "Course Schedule II",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/course-schedule-ii/",
        "alternate_title": "Course Schedule II",
        "alternate_url": "https://www.geeksforgeeks.org/problems/course-schedule-ii/1",
        "pattern": "Kahn's Algorithm (Ordered Dependency Linearization)",
        "time_complexity": "O(V + E)",
        "space_complexity": "O(V + E)",
        "secondary_topics": [
            "Kahn's Algorithm (BFS Topo)"
        ],
        "companies": [
            "Amazon",
            "Meta",
            "Google",
            "Microsoft",
            "Uber",
            "ByteDance"
        ]
    },
    {
        "category": "Topological Sort",
        "title": "Alien Dictionary",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/alien-dictionary/",
        "alternate_title": "Alien Dictionary",
        "alternate_url": "https://www.geeksforgeeks.org/problems/alien-dictionary/1",
        "pattern": "Character Precedence Graph + Kahn's Topological Sort",
        "time_complexity": "O(C)",
        "space_complexity": "O(1) (26 characters)",
        "secondary_topics": [
            "Kahn's Algorithm (BFS Topo)"
        ],
        "companies": [
            "Meta",
            "Google",
            "Amazon",
            "Microsoft",
            "Airbnb",
            "Uber"
        ]
    },
    {
        "category": "Topological Sort",
        "title": "Topological Sort (Kahn's vs DFS)",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/course-schedule/",
        "alternate_title": "Topological sort",
        "alternate_url": "https://www.geeksforgeeks.org/problems/topological-sort/1",
        "pattern": "Kahn's In-Degree BFS vs DFS Reversal Stack",
        "time_complexity": "O(V + E)",
        "space_complexity": "O(V)",
        "secondary_topics": [
            "Kahn's Algorithm (BFS Topo)"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Google",
            "Flipkart"
        ]
    },
    {
        "category": "Topological Sort",
        "title": "Minimum Height Trees",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/minimum-height-trees/",
        "alternate_title": "Minimum Height Trees",
        "alternate_url": "https://www.geeksforgeeks.org/problems/minimum-height-trees/1",
        "pattern": "Leaf Trimming BFS (In-Degree 1 Layer Peel)",
        "time_complexity": "O(V)",
        "space_complexity": "O(V)",
        "secondary_topics": [
            "Graph BFS/DFS"
        ],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "Topological Sort",
        "title": "Sequence Reconstruction",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/sequence-reconstruction/",
        "alternate_title": "Sequence Reconstruction",
        "alternate_url": "https://www.geeksforgeeks.org/problems/sequence-reconstruction/1",
        "pattern": "Topological Sort Uniqueness (Queue Size == 1 Always)",
        "time_complexity": "O(V + E)",
        "space_complexity": "O(V + E)",
        "secondary_topics": [
            "Kahn's Algorithm (BFS Topo)"
        ],
        "companies": [
            "Google",
            "Meta"
        ]
    },
    {
        "category": "Topological Sort",
        "title": "Find Eventual Safe States",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/find-eventual-safe-states/",
        "alternate_title": "Eventual Safe States",
        "alternate_url": "https://www.geeksforgeeks.org/problems/eventual-safe-states/1",
        "pattern": "Reverse Graph Edge BFS Topo (Out-Degree 0 Terminal Queue)",
        "time_complexity": "O(V + E)",
        "space_complexity": "O(V + E)",
        "secondary_topics": [
            "Kahn's Algorithm (BFS Topo)"
        ],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "Topological Sort",
        "title": "Longest Increasing Path in a Matrix",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/longest-increasing-path-in-a-matrix/",
        "alternate_title": "Longest Increasing Path in a Matrix",
        "alternate_url": "https://www.geeksforgeeks.org/problems/longest-increasing-path-in-a-matrix/1",
        "pattern": "DAG Topological Sort / Grid DFS with Memoization",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(M * N)",
        "secondary_topics": [
            "DP on Grids"
        ],
        "companies": [
            "Google",
            "Amazon",
            "Meta",
            "ByteDance"
        ]
    },
    {
        "category": "Topological Sort",
        "title": "All Ancestors of a Node in a Directed Acyclic Graph",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/",
        "alternate_title": "Ancestors in DAG",
        "alternate_url": "https://www.geeksforgeeks.org/problems/ancestors-in-dag/1",
        "pattern": "Kahn's Algorithm Topo Order Set Propagation",
        "time_complexity": "O(V * (V + E))",
        "space_complexity": "O(V^2)",
        "secondary_topics": [
            "Kahn's Algorithm (BFS Topo)"
        ],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "Topological Sort",
        "title": "Sort Items by Groups Respecting Dependencies",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/",
        "alternate_title": "Sort Items by Groups",
        "alternate_url": "https://www.geeksforgeeks.org/problems/sort-items-by-groups/1",
        "pattern": "2-Level Hierarchical Topological Sort (Group & Item)",
        "time_complexity": "O(V + E)",
        "space_complexity": "O(V + E)",
        "secondary_topics": [
            "Kahn's Algorithm (BFS Topo)"
        ],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "Union Find",
        "title": "Number of Provinces",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/number-of-provinces/",
        "alternate_title": "Number of Provinces",
        "alternate_url": "https://www.geeksforgeeks.org/problems/number-of-provinces/1",
        "pattern": "Disjoint Set Union (DSU with Path Compression & Rank)",
        "time_complexity": "O(N^2 * alpha(N))",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Kruskal's Algorithm (DSU)",
            "Graph BFS/DFS"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Microsoft"
        ]
    },
    {
        "category": "Union Find",
        "title": "Redundant Connection",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/redundant-connection/",
        "alternate_title": "Redundant Connection",
        "alternate_url": "https://www.geeksforgeeks.org/problems/redundant-connection/1",
        "pattern": "DSU Cycle Detection on Edge Addition",
        "time_complexity": "O(N * alpha(N))",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Kruskal's Algorithm (DSU)"
        ],
        "companies": [
            "Google",
            "Amazon",
            "Meta"
        ]
    },
    {
        "category": "Union Find",
        "title": "Accounts Merge",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/accounts-merge/",
        "alternate_title": "Accounts Merge",
        "alternate_url": "https://www.geeksforgeeks.org/problems/merging-details/1",
        "pattern": "DSU on Email Addresses + Name Mapping",
        "time_complexity": "O(N * K log(N * K))",
        "space_complexity": "O(N * K)",
        "secondary_topics": [
            "HashMap / HashSet"
        ],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Microsoft",
            "Uber"
        ]
    },
    {
        "category": "Union Find",
        "title": "Min Cost to Connect All Points (Kruskal's / Prim's)",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/min-cost-to-connect-all-points/",
        "alternate_title": "Minimum Spanning Tree (Kruskal/Prim)",
        "alternate_url": "https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1",
        "pattern": "Kruskal's MST with DSU / Prim's Algorithm with Min Heap",
        "time_complexity": "O(E log E) Kruskal / O(V^2) Prim",
        "space_complexity": "O(V + E)",
        "secondary_topics": [
            "Kruskal's Algorithm (DSU)",
            "Prim's Algorithm"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Meta",
            "Microsoft"
        ]
    },
    {
        "category": "Union Find",
        "title": "Graph Valid Tree",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/graph-valid-tree/",
        "alternate_title": "Is it a Tree?",
        "alternate_url": "https://www.geeksforgeeks.org/problems/is-it-a-tree/1",
        "pattern": "Edges == V - 1 and DSU Single Component",
        "time_complexity": "O(V * alpha(V))",
        "space_complexity": "O(V)",
        "secondary_topics": [
            "Kruskal's Algorithm (DSU)"
        ],
        "companies": [
            "Google",
            "Meta",
            "Amazon",
            "LinkedIn"
        ]
    },
    {
        "category": "Union Find",
        "title": "Number of Operations to Make Network Connected",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/number-of-operations-to-make-network-connected/",
        "alternate_title": "Connecting the graph",
        "alternate_url": "https://www.geeksforgeeks.org/problems/connecting-the-graph/1",
        "pattern": "DSU Redundant Edges >= Disconnected Components - 1",
        "time_complexity": "O(V + E * alpha(V))",
        "space_complexity": "O(V)",
        "secondary_topics": [
            "Kruskal's Algorithm (DSU)"
        ],
        "companies": [
            "Amazon",
            "Google"
        ]
    },
    {
        "category": "Union Find",
        "title": "Most Stones Removed with Same Row or Column",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/",
        "alternate_title": "Maximum Stone Removal",
        "alternate_url": "https://www.geeksforgeeks.org/problems/maximum-stone-removal-1662179442/1",
        "pattern": "DSU Union on Row & Inverted Col Indices (N - Components)",
        "time_complexity": "O(N * alpha(N))",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Kruskal's Algorithm (DSU)"
        ],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "Union Find",
        "title": "Making A Large Island",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/making-a-large-island/",
        "alternate_title": "Making A Large Island",
        "alternate_url": "https://www.geeksforgeeks.org/problems/making-a-large-island/1",
        "pattern": "DSU Component Size Tagging + 0-Cell Flip Boundary Sum",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N^2)",
        "secondary_topics": [
            "Graph BFS/DFS"
        ],
        "companies": [
            "Meta",
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "Union Find",
        "title": "Swim in Rising Water",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/swim-in-rising-water/",
        "alternate_title": "Minimum time to reach bottom",
        "alternate_url": "https://www.geeksforgeeks.org/problems/minimum-time-to-reach-bottom/1",
        "pattern": "Sorted Elevation DSU Connectivity / Modified Dijkstra",
        "time_complexity": "O(N^2 log N)",
        "space_complexity": "O(N^2)",
        "secondary_topics": [
            "Dijkstra's Algorithm",
            "Binary Search on Answer Range"
        ],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "Union Find",
        "title": "Disjoint Set Union (Union by Rank & Size)",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/friend-circles/",
        "alternate_title": "Disjoint set (Union-Find)",
        "alternate_url": "https://www.geeksforgeeks.org/problems/disjoint-set-union-find/1",
        "pattern": "Canonical DSU Implementation with Path Compression",
        "time_complexity": "O(alpha(N)) per op",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Kruskal's Algorithm (DSU)"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Microsoft"
        ]
    },
    {
        "category": "Tries",
        "title": "Implement Trie (Prefix Tree)",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/implement-trie-prefix-tree/",
        "alternate_title": "Trie | (Insert and Search)",
        "alternate_url": "https://www.geeksforgeeks.org/problems/trie-insert-and-search0651/1",
        "pattern": "Trie Node Array [26] + EndOfWord Flag",
        "time_complexity": "O(L) per word op",
        "space_complexity": "O(Total Chars * 26)",
        "secondary_topics": [
            "Trie Prefix Tree"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Microsoft",
            "Meta",
            "Apple",
            "Twitter / X"
        ]
    },
    {
        "category": "Tries",
        "title": "Design Add and Search Words Data Structure",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/design-add-and-search-words-data-structure/",
        "alternate_title": "Word Boggle (Trie search)",
        "alternate_url": "https://www.geeksforgeeks.org/problems/word-boggle4143/1",
        "pattern": "Trie with Wildcard '.' Backtracking Branching",
        "time_complexity": "O(M) exact, O(26^L) worst wildcard",
        "space_complexity": "O(Total Chars * 26)",
        "secondary_topics": [
            "Trie Prefix Tree",
            "Recursion and Backtracking"
        ],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Microsoft"
        ]
    },
    {
        "category": "Tries",
        "title": "Word Search II",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/word-search-ii/",
        "alternate_title": "Word Boggle II",
        "alternate_url": "https://www.geeksforgeeks.org/problems/word-boggle-ii/1",
        "pattern": "Grid DFS Backtracking Pruned with Prefix Trie",
        "time_complexity": "O(M * N * 4^L)",
        "space_complexity": "O(Sum(Len(Words)))",
        "secondary_topics": [
            "Trie Prefix Tree",
            "Recursion and Backtracking"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Meta",
            "Microsoft",
            "Uber",
            "Apple"
        ]
    },
    {
        "category": "Tries",
        "title": "Maximum XOR of Two Numbers in an Array",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/",
        "alternate_title": "Maximum XOR of two numbers in an array",
        "alternate_url": "https://www.geeksforgeeks.org/problems/maximum-xor-of-two-numbers-in-an-array/1",
        "pattern": "32-Bit Binary Trie (Greedy Opposite Bit Walk)",
        "time_complexity": "O(N * 32)",
        "space_complexity": "O(N * 32)",
        "secondary_topics": [
            "Bit Manipulation",
            "Trie Prefix Tree"
        ],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "Tries",
        "title": "Maximum XOR With an Element From Array",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/maximum-xor-with-an-element-from-array/",
        "alternate_title": "Maximum XOR With an Element From Array",
        "alternate_url": "https://www.geeksforgeeks.org/problems/maximum-xor-with-an-element-from-array/1",
        "pattern": "Offline Query Sorting + Incremental Bit Trie Insertion",
        "time_complexity": "O(Q log Q + N log N + (N + Q) * 32)",
        "space_complexity": "O(N * 32)",
        "secondary_topics": [
            "Bit Manipulation",
            "Trie Prefix Tree"
        ],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "Tries",
        "title": "Search Suggestions System",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/search-suggestions-system/",
        "alternate_title": "Auto-complete system",
        "alternate_url": "https://www.geeksforgeeks.org/problems/auto-complete-system/1",
        "pattern": "Trie with Top-3 Lexicographical Cache per Node",
        "time_complexity": "O(N log N + L)",
        "space_complexity": "O(Total Chars * 26)",
        "secondary_topics": [
            "Trie Prefix Tree",
            "Binary Search"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Microsoft"
        ]
    },
    {
        "category": "Tries",
        "title": "Replace Words",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/replace-words/",
        "alternate_title": "Replace words with root",
        "alternate_url": "https://www.geeksforgeeks.org/problems/replace-words/1",
        "pattern": "Trie Shortest Root Prefix Match",
        "time_complexity": "O(Sentence Length)",
        "space_complexity": "O(Dictionary Chars)",
        "secondary_topics": [
            "Trie Prefix Tree"
        ],
        "companies": [
            "Google",
            "Amazon",
            "Uber"
        ]
    },
    {
        "category": "Tries",
        "title": "Longest Common Prefix using Trie",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/longest-common-prefix/",
        "alternate_title": "Longest Common Prefix in an Array",
        "alternate_url": "https://www.geeksforgeeks.org/problems/longest-common-prefix-in-an-array5129/1",
        "pattern": "Trie Single-Child Chain Traversal",
        "time_complexity": "O(S)",
        "space_complexity": "O(S * 26)",
        "secondary_topics": [
            "Trie Prefix Tree"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Adobe"
        ]
    },
    {
        "category": "Dynamic Programming Basics",
        "title": "Climbing Stairs",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/climbing-stairs/",
        "alternate_title": "Count ways to reach the n'th stair",
        "alternate_url": "https://www.geeksforgeeks.org/problems/count-ways-to-reach-the-nth-stair-1587115620/1",
        "pattern": "1D State Transition (Fibonacci dp[i] = dp[i-1] + dp[i-2])",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Google",
            "Meta",
            "Microsoft",
            "Apple",
            "Adobe"
        ]
    },
    {
        "category": "Dynamic Programming Basics",
        "title": "Min Cost Climbing Stairs",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/min-cost-climbing-stairs/",
        "alternate_title": "Min Cost Climbing Stairs",
        "alternate_url": "https://www.geeksforgeeks.org/problems/min-cost-climbing-stairs/1",
        "pattern": "1D DP (dp[i] = cost[i] + min(dp[i-1], dp[i-2]))",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Google",
            "Microsoft",
            "Apple"
        ]
    },
    {
        "category": "Dynamic Programming Basics",
        "title": "House Robber",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/house-robber/",
        "alternate_title": "Stickler Thief",
        "alternate_url": "https://www.geeksforgeeks.org/problems/stickler-theif-1587115621/1",
        "pattern": "Include / Exclude Choice (rob = max(rob, skip + num))",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Google",
            "Meta",
            "Microsoft",
            "Apple",
            "LinkedIn"
        ]
    },
    {
        "category": "Dynamic Programming Basics",
        "title": "House Robber II",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/house-robber-ii/",
        "alternate_title": "House Robber II",
        "alternate_url": "https://www.geeksforgeeks.org/problems/house-robber-ii/1",
        "pattern": "Circular Array DP (max(Rob(0..N-2), Rob(1..N-1)))",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Google",
            "Microsoft",
            "Meta"
        ]
    },
    {
        "category": "Dynamic Programming Basics",
        "title": "Coin Change",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/coin-change/",
        "alternate_title": "Coin Change (Minimum Coins)",
        "alternate_url": "https://www.geeksforgeeks.org/problems/number-of-coins1824/1",
        "pattern": "Unbounded Knapsack Min Value (dp[a] = min(dp[a], 1 + dp[a - c]))",
        "time_complexity": "O(Amount * N)",
        "space_complexity": "O(Amount)",
        "secondary_topics": [
            "Unbounded Knapsack Pattern"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Meta",
            "Microsoft",
            "Apple",
            "Bloomberg",
            "ByteDance"
        ]
    },
    {
        "category": "Dynamic Programming Basics",
        "title": "Coin Change II",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/coin-change-ii/",
        "alternate_title": "Coin Change (Count Ways)",
        "alternate_url": "https://www.geeksforgeeks.org/problems/coin-change2448/1",
        "pattern": "Unbounded Knapsack Total Combinations Count",
        "time_complexity": "O(Amount * N)",
        "space_complexity": "O(Amount)",
        "secondary_topics": [
            "Unbounded Knapsack Pattern"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Meta",
            "Microsoft"
        ]
    },
    {
        "category": "Dynamic Programming Basics",
        "title": "0/1 Knapsack Problem",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/ones-and-zeroes/",
        "alternate_title": "0 - 1 Knapsack Problem",
        "alternate_url": "https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1",
        "pattern": "0/1 Knapsack Pattern (Backward Weight Iteration)",
        "time_complexity": "O(N * W)",
        "space_complexity": "O(W)",
        "secondary_topics": [
            "0/1 Knapsack Pattern"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Microsoft",
            "Flipkart",
            "Paytm"
        ]
    },
    {
        "category": "Dynamic Programming Basics",
        "title": "Partition Equal Subset Sum",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/partition-equal-subset-sum/",
        "alternate_title": "Subset Sum Problem",
        "alternate_url": "https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1",
        "pattern": "0/1 Knapsack Target Sum == Total / 2",
        "time_complexity": "O(N * Target)",
        "space_complexity": "O(Target)",
        "secondary_topics": [
            "0/1 Knapsack Pattern"
        ],
        "companies": [
            "Amazon",
            "Meta",
            "Google",
            "Microsoft"
        ]
    },
    {
        "category": "Dynamic Programming Basics",
        "title": "Target Sum",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/target-sum/",
        "alternate_title": "Target Sum",
        "alternate_url": "https://www.geeksforgeeks.org/problems/target-sum-1626326450/1",
        "pattern": "Subset Sum Reduction ((Total + Target) / 2)",
        "time_complexity": "O(N * S)",
        "space_complexity": "O(S)",
        "secondary_topics": [
            "0/1 Knapsack Pattern"
        ],
        "companies": [
            "Meta",
            "Amazon",
            "Google"
        ]
    },
    {
        "category": "Dynamic Programming Basics",
        "title": "Longest Increasing Subsequence",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/longest-increasing-subsequence/",
        "alternate_title": "Longest Increasing Subsequence",
        "alternate_url": "https://www.geeksforgeeks.org/problems/longest-increasing-subsequence-1587115620/1",
        "pattern": "LIS Pattern (Binary Search Patience Sorting O(N log N))",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Longest Increasing Subsequence (LIS)",
            "Binary Search"
        ],
        "companies": [
            "Google",
            "Amazon",
            "Microsoft",
            "Meta",
            "Apple",
            "Bloomberg"
        ]
    },
    {
        "category": "Dynamic Programming Basics",
        "title": "Russian Doll Envelopes",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/russian-doll-envelopes/",
        "alternate_title": "Russian Doll Envelopes",
        "alternate_url": "https://www.geeksforgeeks.org/problems/russian-doll-envelopes/1",
        "pattern": "2D Sort (Width Asc, Height Desc) + 1D LIS Binary Search",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Longest Increasing Subsequence (LIS)",
            "Binary Search"
        ],
        "companies": [
            "Google",
            "Amazon",
            "Meta",
            "Uber"
        ]
    },
    {
        "category": "Dynamic Programming Basics",
        "title": "Word Break",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/word-break/",
        "alternate_title": "Word Break",
        "alternate_url": "https://www.geeksforgeeks.org/problems/word-break1352/1",
        "pattern": "1D Prefix Partition DP + Hash Set Lookup",
        "time_complexity": "O(N^2 * L)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "HashMap / HashSet",
            "Tries"
        ],
        "companies": [
            "Amazon",
            "Meta",
            "Google",
            "Microsoft",
            "Bloomberg",
            "Apple",
            "Uber"
        ]
    },
    {
        "category": "Dynamic Programming Basics",
        "title": "Decode Ways",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/decode-ways/",
        "alternate_title": "Total Decoding Messages",
        "alternate_url": "https://www.geeksforgeeks.org/problems/total-decoding-messages1235/1",
        "pattern": "1D DP Single and Double Digit Transition",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Microsoft",
            "Uber"
        ]
    },
    {
        "category": "Dynamic Programming Basics",
        "title": "Combination Sum IV",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/combination-sum-iv/",
        "alternate_title": "Ways to sum to N",
        "alternate_url": "https://www.geeksforgeeks.org/problems/ways-to-sum-to-n5752/1",
        "pattern": "Unbounded Knapsack Order Matters (Permutation DP)",
        "time_complexity": "O(Target * N)",
        "space_complexity": "O(Target)",
        "secondary_topics": [
            "Unbounded Knapsack Pattern"
        ],
        "companies": [
            "Google",
            "Amazon",
            "Meta"
        ]
    },
    {
        "category": "Dynamic Programming Basics",
        "title": "Best Time to Buy and Sell Stock with Cooldown",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/",
        "alternate_title": "Stock with Cooldown",
        "alternate_url": "https://www.geeksforgeeks.org/problems/buy-stock-with-cooldown/1",
        "pattern": "State Machine DP (Held, Sold, Rest)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon",
            "Meta"
        ]
    },
    {
        "category": "Dynamic Programming Basics",
        "title": "Best Time to Buy and Sell Stock with Transaction Fee",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/",
        "alternate_title": "Buy Stock with Fee",
        "alternate_url": "https://www.geeksforgeeks.org/problems/buy-stock-with-transaction-fee/1",
        "pattern": "Two-State DP (Hold vs Free)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Meta",
            "Amazon",
            "Google"
        ]
    },
    {
        "category": "Dynamic Programming Basics",
        "title": "Matrix Chain Multiplication",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/minimum-cost-to-merge-stones/",
        "alternate_title": "Matrix Chain Multiplication",
        "alternate_url": "https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1",
        "pattern": "Interval / Partition DP (MCM Pattern dp[i][j])",
        "time_complexity": "O(N^3)",
        "space_complexity": "O(N^2)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Microsoft",
            "Flipkart"
        ]
    },
    {
        "category": "Dynamic Programming Basics",
        "title": "Fibonacci Number",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/fibonacci-number/",
        "alternate_title": "Nth Fibonacci Number",
        "alternate_url": "https://www.geeksforgeeks.org/problems/nth-fibonacci-number1359/1",
        "pattern": "Base 1D DP / Matrix Exponentiation",
        "time_complexity": "O(N) or O(log N) Matrix",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Google",
            "Microsoft",
            "Apple"
        ]
    },
    {
        "category": "DP on Strings",
        "title": "Longest Common Subsequence",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/longest-common-subsequence/",
        "alternate_title": "Longest Common Subsequence",
        "alternate_url": "https://www.geeksforgeeks.org/problems/longest-common-subsequence-1587115620/1",
        "pattern": "2D Grid LCS Transition (Match 1 + dp[i-1][j-1])",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(min(M, N))",
        "secondary_topics": [
            "Longest Common Subsequence (LCS)"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Microsoft",
            "Meta",
            "Adobe",
            "PayPal"
        ]
    },
    {
        "category": "DP on Strings",
        "title": "Longest Palindromic Subsequence",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/longest-palindromic-subsequence/",
        "alternate_title": "Longest Palindromic Subsequence",
        "alternate_url": "https://www.geeksforgeeks.org/problems/longest-palindromic-subsequence-1612327878/1",
        "pattern": "LCS(S, Reverse(S)) / Interval DP",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Longest Common Subsequence (LCS)"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Microsoft"
        ]
    },
    {
        "category": "DP on Strings",
        "title": "Edit Distance",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/edit-distance/",
        "alternate_title": "Edit Distance",
        "alternate_url": "https://www.geeksforgeeks.org/problems/edit-distance3702/1",
        "pattern": "Levenshtein Distance 2D DP (Insert, Delete, Replace)",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(min(M, N))",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon",
            "Microsoft",
            "Meta",
            "Apple",
            "ByteDance"
        ]
    },
    {
        "category": "DP on Strings",
        "title": "Distinct Subsequences",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/distinct-subsequences/",
        "alternate_title": "Distinct occurrences",
        "alternate_url": "https://www.geeksforgeeks.org/problems/distinct-occurrences/1",
        "pattern": "2D DP Matching (dp[i][j] = dp[i-1][j-1] + dp[i-1][j])",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "DP on Strings",
        "title": "Wildcard Matching",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/wildcard-matching/",
        "alternate_title": "Wildcard Pattern Matching",
        "alternate_url": "https://www.geeksforgeeks.org/problems/wildcard-pattern-matching/1",
        "pattern": "2D DP Character Matching with '*' Multi-Match Transition",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Meta",
            "Amazon",
            "Microsoft"
        ]
    },
    {
        "category": "DP on Strings",
        "title": "Regular Expression Matching",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/regular-expression-matching/",
        "alternate_title": "Regular Expression Matching",
        "alternate_url": "https://www.geeksforgeeks.org/problems/regular-expression-matching/1",
        "pattern": "2D DP Zero or More Character Kleene Star Transition",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Meta",
            "Google",
            "Amazon",
            "Microsoft",
            "Apple",
            "Uber"
        ]
    },
    {
        "category": "DP on Strings",
        "title": "Longest Palindromic Substring",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/longest-palindromic-substring/",
        "alternate_title": "Longest Palindromic Substring",
        "alternate_url": "https://www.geeksforgeeks.org/problems/longest-palindrome-in-a-string3411/1",
        "pattern": "Expand Around Center O(1) Space / 2D DP Interval",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Two Pointers"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Meta",
            "Google",
            "Apple",
            "Bloomberg"
        ]
    },
    {
        "category": "DP on Strings",
        "title": "Palindromic Substrings",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/palindromic-substrings/",
        "alternate_title": "Count Palindrome Sub-Strings of a String",
        "alternate_url": "https://www.geeksforgeeks.org/problems/count-palindrome-sub-strings-of-a-string0652/1",
        "pattern": "Expand Around Center (Odd and Even Axes)",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Two Pointers"
        ],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "LinkedIn",
            "Twitter / X"
        ]
    },
    {
        "category": "DP on Strings",
        "title": "Shortest Common Supersequence",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/shortest-common-supersequence/",
        "alternate_title": "Shortest Common Supersequence",
        "alternate_url": "https://www.geeksforgeeks.org/problems/shortest-common-supersequence0322/1",
        "pattern": "LCS Table Backtracking for Merged Supersequence",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(M * N)",
        "secondary_topics": [
            "Longest Common Subsequence (LCS)"
        ],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "DP on Strings",
        "title": "Interleaving String",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/interleaving-string/",
        "alternate_title": "Interleaved Strings",
        "alternate_url": "https://www.geeksforgeeks.org/problems/interleaved-strings/1",
        "pattern": "2D Grid DP (dp[i][j] = match(s1) or match(s2))",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon",
            "Microsoft"
        ]
    },
    {
        "category": "DP on Strings",
        "title": "Minimum Insertion Steps to Make a String Palindrome",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/",
        "alternate_title": "Form a palindrome",
        "alternate_url": "https://www.geeksforgeeks.org/problems/form-a-palindrome1455/1",
        "pattern": "Len(S) - LPS(S)",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Longest Common Subsequence (LCS)"
        ],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "DP on Strings",
        "title": "Delete Operation for Two Strings",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/delete-operation-for-two-strings/",
        "alternate_title": "Minimum number of deletions and insertions",
        "alternate_url": "https://www.geeksforgeeks.org/problems/minimum-number-of-deletions-and-insertions0209/1",
        "pattern": "Len(s1) + Len(s2) - 2 * LCS(s1, s2)",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Longest Common Subsequence (LCS)"
        ],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "DP on Grids",
        "title": "Unique Paths",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/unique-paths/",
        "alternate_title": "Number of Unique Paths",
        "alternate_url": "https://www.geeksforgeeks.org/problems/number-of-unique-paths5339/1",
        "pattern": "2D Grid DP (dp[i][j] = dp[i-1][j] + dp[i][j-1]) / Combinatorics",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Google",
            "Meta",
            "Microsoft",
            "Bloomberg"
        ]
    },
    {
        "category": "DP on Grids",
        "title": "Unique Paths II",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/unique-paths-ii/",
        "alternate_title": "Unique Paths in a Grid with Obstacles",
        "alternate_url": "https://www.geeksforgeeks.org/problems/unique-paths-in-a-grid--170647/1",
        "pattern": "2D Grid DP with Obstacle Zeroing",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Google",
            "Meta"
        ]
    },
    {
        "category": "DP on Grids",
        "title": "Minimum Path Sum",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/minimum-path-sum/",
        "alternate_title": "Minimum Cost Path",
        "alternate_url": "https://www.geeksforgeeks.org/problems/minimum-cost-path3833/1",
        "pattern": "2D Grid DP (grid[i][j] + min(up, left))",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Google",
            "Microsoft",
            "Bloomberg",
            "Goldman Sachs"
        ]
    },
    {
        "category": "DP on Grids",
        "title": "Triangle",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/triangle/",
        "alternate_title": "Triangle Path Sum",
        "alternate_url": "https://www.geeksforgeeks.org/problems/triangle-path-sum/1",
        "pattern": "Bottom-Up Triangular Reduction (dp[j] = val + min(dp[j], dp[j+1]))",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Google",
            "Apple"
        ]
    },
    {
        "category": "DP on Grids",
        "title": "Maximal Square",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/maximal-square/",
        "alternate_title": "Largest square sub-matrix with all 1s",
        "alternate_url": "https://www.geeksforgeeks.org/problems/largest-square-sub-matrix-with-all-1s3904/1",
        "pattern": "2D Grid DP (1 + min(left, up, diag))",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon",
            "Meta",
            "Apple",
            "ByteDance"
        ]
    },
    {
        "category": "DP on Grids",
        "title": "Dungeon Game",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/dungeon-game/",
        "alternate_title": "Dungeon Game",
        "alternate_url": "https://www.geeksforgeeks.org/problems/dungeon-game/1",
        "pattern": "Bottom-Right to Top-Left Required Health Backpropagation",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon",
            "Microsoft"
        ]
    },
    {
        "category": "DP on Grids",
        "title": "Cherry Pickup",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/cherry-pickup/",
        "alternate_title": "Cherry Pickup",
        "alternate_url": "https://www.geeksforgeeks.org/problems/cherry-pickup/1",
        "pattern": "Simultaneous Dual Path 3D DP (r1, c1, r2)",
        "time_complexity": "O(N^3)",
        "space_complexity": "O(N^2)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "DP on Grids",
        "title": "Cherry Pickup II",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/cherry-pickup-ii/",
        "alternate_title": "Chocolates Pickup",
        "alternate_url": "https://www.geeksforgeeks.org/problems/chocolates-pickup/1",
        "pattern": "Row Step Dual Robot 3D DP (row, col1, col2)",
        "time_complexity": "O(R * C^2 * 9)",
        "space_complexity": "O(C^2)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "DP on Grids",
        "title": "Minimum Falling Path Sum",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/minimum-falling-path-sum/",
        "alternate_title": "Minimum Falling Path Sum",
        "alternate_url": "https://www.geeksforgeeks.org/problems/minimum-falling-path-sum/1",
        "pattern": "2D Grid DP Top-Down 3-Branch Descent",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "DP on Grids",
        "title": "Knight Probability in Chessboard",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/knight-probability-in-chessboard/",
        "alternate_title": "Knight Probability in Chessboard",
        "alternate_url": "https://www.geeksforgeeks.org/problems/knight-walk4524/1",
        "pattern": "3D Dynamic Programming (K Steps 8-Move Distribution)",
        "time_complexity": "O(K * N^2)",
        "space_complexity": "O(N^2)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "DP on Grids",
        "title": "Out of Boundary Paths",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/out-of-boundary-paths/",
        "alternate_title": "Out of Boundary Paths",
        "alternate_url": "https://www.geeksforgeeks.org/problems/out-of-boundary-paths/1",
        "pattern": "3D Grid DP (Move Count 4-Directional Propagation)",
        "time_complexity": "O(N * M * MaxMove)",
        "space_complexity": "O(M * N)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "DP on Grids",
        "title": "Count Square Submatrices with All Ones",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/count-square-submatrices-with-all-ones/",
        "alternate_title": "Count Square Submatrices",
        "alternate_url": "https://www.geeksforgeeks.org/problems/count-square-submatrices-with-all-ones/1",
        "pattern": "2D DP Max Square Side Length Accumulator",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "Intervals",
        "title": "Merge Intervals",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/merge-intervals/",
        "alternate_title": "Overlapping Intervals",
        "alternate_url": "https://www.geeksforgeeks.org/problems/overlapping-intervals--170633/1",
        "pattern": "Sort by Start Time + Greedy Overlap Extend",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Arrays and Strings"
        ],
        "companies": [
            "Meta",
            "Google",
            "Amazon",
            "Microsoft",
            "Bloomberg",
            "Uber"
        ]
    },
    {
        "category": "Intervals",
        "title": "Insert Interval",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/insert-interval/",
        "alternate_title": "Insert Interval",
        "alternate_url": "https://www.geeksforgeeks.org/problems/insert-interval-1666736229/1",
        "pattern": "Three-Phase Linear Scan (Before, Overlap Merge, After)",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Meta",
            "Amazon",
            "Microsoft",
            "LinkedIn"
        ]
    },
    {
        "category": "Intervals",
        "title": "Non-overlapping Intervals",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/non-overlapping-intervals/",
        "alternate_title": "Non-overlapping Intervals",
        "alternate_url": "https://www.geeksforgeeks.org/problems/non-overlapping-intervals/1",
        "pattern": "Greedy Activity Selection (Sort by End Time)",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Google",
            "Meta"
        ]
    },
    {
        "category": "Intervals",
        "title": "Meeting Rooms",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/meeting-rooms/",
        "alternate_title": "Attend all meetings",
        "alternate_url": "https://www.geeksforgeeks.org/problems/attend-all-meetings/1",
        "pattern": "Sort by Start Time + Adjacent Overlap Check",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Microsoft",
            "Bloomberg"
        ]
    },
    {
        "category": "Intervals",
        "title": "Meeting Rooms II",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/meeting-rooms-ii/",
        "alternate_title": "Minimum Platforms",
        "alternate_url": "https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1",
        "pattern": "Two Pointers Chronological Sweepline / Min Heap",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Heap / Priority Queue",
            "Two Pointers"
        ],
        "companies": [
            "Amazon",
            "Meta",
            "Google",
            "Microsoft",
            "Bloomberg",
            "Uber",
            "ByteDance",
            "PayPal"
        ]
    },
    {
        "category": "Intervals",
        "title": "Minimum Number of Arrows to Burst Balloons",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/",
        "alternate_title": "Minimum Number of Arrows to Burst Balloons",
        "alternate_url": "https://www.geeksforgeeks.org/problems/minimum-number-of-arrows-to-burst-balloons/1",
        "pattern": "Greedy Interval Intersection (Sort by End Coordinate)",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon",
            "Meta"
        ]
    },
    {
        "category": "Intervals",
        "title": "Interval List Intersections",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/interval-list-intersections/",
        "alternate_title": "Interval List Intersections",
        "alternate_url": "https://www.geeksforgeeks.org/problems/interval-list-intersections/1",
        "pattern": "Two Pointers max(start1, start2) <= min(end1, end2)",
        "time_complexity": "O(M + N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Two Pointers"
        ],
        "companies": [
            "Meta",
            "Google",
            "Amazon",
            "Uber"
        ]
    },
    {
        "category": "Intervals",
        "title": "Summary Ranges",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/summary-ranges/",
        "alternate_title": "Summary Ranges",
        "alternate_url": "https://www.geeksforgeeks.org/problems/summary-ranges/1",
        "pattern": "Linear Scan Consecutive Subarray Identification",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "Intervals",
        "title": "Employee Free Time",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/employee-free-time/",
        "alternate_title": "Find free interval",
        "alternate_url": "https://www.geeksforgeeks.org/problems/find-free-interval/1",
        "pattern": "K-Way Merge Min Heap / Merged Interval Gaps",
        "time_complexity": "O(N log K)",
        "space_complexity": "O(K)",
        "secondary_topics": [
            "Heap / Priority Queue"
        ],
        "companies": [
            "Google",
            "Meta",
            "Amazon",
            "Airbnb",
            "Pinterest"
        ]
    },
    {
        "category": "Intervals",
        "title": "Data Stream as Disjoint Intervals",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/data-stream-as-disjoint-intervals/",
        "alternate_title": "Disjoint Intervals Stream",
        "alternate_url": "https://www.geeksforgeeks.org/problems/disjoint-intervals-stream/1",
        "pattern": "Balanced BST / TreeSet Binary Search Interval Merging",
        "time_complexity": "O(log N) per add",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Trees / BST"
        ],
        "companies": [
            "Google",
            "Amazon"
        ]
    },
    {
        "category": "Bit Manipulation",
        "title": "Single Number",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/single-number/",
        "alternate_title": "Single Number",
        "alternate_url": "https://www.geeksforgeeks.org/problems/single-number1014/1",
        "pattern": "XOR Accumulation (A ^ A = 0, A ^ 0 = A)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Google",
            "Microsoft",
            "Meta",
            "Apple"
        ]
    },
    {
        "category": "Bit Manipulation",
        "title": "Single Number II",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/single-number-ii/",
        "alternate_title": "Find element occuring once when all other are present thrice",
        "alternate_url": "https://www.geeksforgeeks.org/problems/find-element-occuring-once-when-all-other-are-present-thrice/1",
        "pattern": "32-Bit Positional Sum Modulo 3 / Digital Logic (Ones, Twos)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Google"
        ]
    },
    {
        "category": "Bit Manipulation",
        "title": "Single Number III",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/single-number-iii/",
        "alternate_title": "Two numbers with odd occurrences",
        "alternate_url": "https://www.geeksforgeeks.org/problems/two-numbers-with-odd-occurrences5846/1",
        "pattern": "XOR Total + Rightmost Set Bit Separation (diff & -diff)",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Bitmasking & Kernighan"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Microsoft"
        ]
    },
    {
        "category": "Bit Manipulation",
        "title": "Number of 1 Bits",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/number-of-1-bits/",
        "alternate_title": "Set Bits",
        "alternate_url": "https://www.geeksforgeeks.org/problems/set-bits0143/1",
        "pattern": "Brian Kernighan\u2019s Algorithm (n = n & (n - 1))",
        "time_complexity": "O(Set Bits Count)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Bitmasking & Kernighan"
        ],
        "companies": [
            "Microsoft",
            "Apple",
            "Amazon"
        ]
    },
    {
        "category": "Bit Manipulation",
        "title": "Counting Bits",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/counting-bits/",
        "alternate_title": "Count total set bits in all numbers from 1 to n",
        "alternate_url": "https://www.geeksforgeeks.org/problems/count-total-set-bits-1587115620/1",
        "pattern": "Bit DP (dp[i] = dp[i >> 1] + (i & 1))",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Dynamic Programming Basics"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Meta"
        ]
    },
    {
        "category": "Bit Manipulation",
        "title": "Reverse Bits",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/reverse-bits/",
        "alternate_title": "Reverse Bits",
        "alternate_url": "https://www.geeksforgeeks.org/problems/reverse-bits3556/1",
        "pattern": "32-Bit Shift & Mask Bitwise Reversal",
        "time_complexity": "O(1)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Apple",
            "Amazon",
            "Microsoft"
        ]
    },
    {
        "category": "Bit Manipulation",
        "title": "Missing Number",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/missing-number/",
        "alternate_title": "Missing number in array",
        "alternate_url": "https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1",
        "pattern": "XOR with [0..N] / Arithmetic Series Sum",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Microsoft",
            "Meta",
            "Google",
            "Apple"
        ]
    },
    {
        "category": "Bit Manipulation",
        "title": "Sum of Two Integers",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/sum-of-two-integers/",
        "alternate_title": "Add two numbers without using arithmetic operators",
        "alternate_url": "https://www.geeksforgeeks.org/problems/add-two-numbers-without-using-arithmetic-operators/1",
        "pattern": "Bitwise Half Adder (Sum = a ^ b, Carry = (a & b) << 1)",
        "time_complexity": "O(1)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Meta",
            "Amazon",
            "Microsoft"
        ]
    },
    {
        "category": "Bit Manipulation",
        "title": "Subsets using Bitmasking",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/subsets/",
        "alternate_title": "Power Set",
        "alternate_url": "https://www.geeksforgeeks.org/problems/power-set4302/1",
        "pattern": "Binary Counter Bitmask [0..(1<<N)-1]",
        "time_complexity": "O(N * 2^N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Bitmasking & Kernighan",
            "Recursion and Backtracking"
        ],
        "companies": [
            "Meta",
            "Amazon",
            "Google"
        ]
    },
    {
        "category": "Bit Manipulation",
        "title": "Find the Duplicate Number",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/find-the-duplicate-number/",
        "alternate_title": "Find duplicates in an array",
        "alternate_url": "https://www.geeksforgeeks.org/problems/find-duplicates-in-an-array/1",
        "pattern": "Bit Manipulation Positional Count vs Range Count",
        "time_complexity": "O(32 * N)",
        "space_complexity": "O(1)",
        "secondary_topics": [],
        "companies": [
            "Amazon",
            "Microsoft",
            "Google"
        ]
    },
    {
        "category": "Sorting Algorithms",
        "title": "Selection Sort",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/sort-an-array/",
        "alternate_title": "Selection Sort Algorithm",
        "alternate_url": "https://www.geeksforgeeks.org/problems/selection-sort/1",
        "pattern": "Selection Sort (Find Minimum in Unsorted Subarray & Swap)",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Sorting Algorithms",
            "Arrays and Strings"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Google"
        ]
    },
    {
        "category": "Sorting Algorithms",
        "title": "Bubble Sort",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/sort-an-array/",
        "alternate_title": "Bubble Sort Algorithm",
        "alternate_url": "https://www.geeksforgeeks.org/problems/bubble-sort/1",
        "pattern": "Bubble Sort (Adjacent Elements Comparison with Early Exit Flag)",
        "time_complexity": "O(N^2) / Best O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Sorting Algorithms",
            "Arrays and Strings"
        ],
        "companies": [
            "Amazon",
            "Microsoft"
        ]
    },
    {
        "category": "Sorting Algorithms",
        "title": "Insertion Sort",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/insertion-sort-list/",
        "alternate_title": "Insertion Sort Algorithm",
        "alternate_url": "https://www.geeksforgeeks.org/problems/insertion-sort/1",
        "pattern": "Insertion Sort (Incremental Sorted Prefix Expansion)",
        "time_complexity": "O(N^2) / Best O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Sorting Algorithms",
            "Arrays and Strings"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Adobe"
        ]
    },
    {
        "category": "Sorting Algorithms",
        "title": "Merge Sort",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/sort-an-array/",
        "alternate_title": "Merge Sort Algorithm",
        "alternate_url": "https://www.geeksforgeeks.org/problems/merge-sort/1",
        "pattern": "Divide and Conquer (Recursive Halving + Linear Two-Pointer Merge)",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Sorting Algorithms",
            "Recursion and Backtracking"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Microsoft",
            "Meta",
            "Apple"
        ]
    },
    {
        "category": "Sorting Algorithms",
        "title": "Quick Sort",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/sort-an-array/",
        "alternate_title": "Quick Sort Algorithm",
        "alternate_url": "https://www.geeksforgeeks.org/problems/quick-sort/1",
        "pattern": "Divide and Conquer (Lomuto / Hoare Pivot Partitioning)",
        "time_complexity": "O(N log N) / Worst O(N^2)",
        "space_complexity": "O(log N)",
        "secondary_topics": [
            "Sorting Algorithms",
            "Recursion and Backtracking"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Microsoft",
            "Meta",
            "Uber"
        ]
    },
    {
        "category": "Sorting Algorithms",
        "title": "Sort an Array",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/sort-an-array/",
        "alternate_title": "Sort an Array",
        "alternate_url": "https://www.geeksforgeeks.org/problems/sort-an-array7033/1",
        "pattern": "Merge Sort / Heap Sort Implementation (Avoid O(N^2) Worst Case)",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Sorting Algorithms",
            "Divide and Conquer"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Apple",
            "Google"
        ]
    },
    {
        "category": "Sorting Algorithms",
        "title": "Counting Sort",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/relative-sort-array/",
        "alternate_title": "Counting Sort Algorithm",
        "alternate_url": "https://www.geeksforgeeks.org/problems/counting-sort/1",
        "pattern": "Non-Comparison Sort (Direct Indexing via Frequency Accumulator)",
        "time_complexity": "O(N + K)",
        "space_complexity": "O(K)",
        "secondary_topics": [
            "Sorting Algorithms",
            "HashMap / HashSet"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Google"
        ]
    },
    {
        "category": "Sorting Algorithms",
        "title": "Largest Number",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/largest-number/",
        "alternate_title": "Largest Number formed from an Array",
        "alternate_url": "https://www.geeksforgeeks.org/problems/largest-number-formed-from-an-array1117/1",
        "pattern": "Custom String Sorting Comparator (a + b vs b + a)",
        "time_complexity": "O(N log N * K)",
        "space_complexity": "O(N * K)",
        "secondary_topics": [
            "Sorting Algorithms",
            "Arrays and Strings"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Google",
            "Meta",
            "Goldman Sachs"
        ]
    },
    {
        "category": "Sorting Algorithms",
        "title": "Custom Sort String",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/custom-sort-string/",
        "alternate_title": "Custom Sort String",
        "alternate_url": "https://www.geeksforgeeks.org/problems/custom-sort-a-string/1",
        "pattern": "Frequency Counting Map + Target Order Linear Traversal",
        "time_complexity": "O(N + M)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Sorting Algorithms",
            "HashMap / HashSet"
        ],
        "companies": [
            "Meta",
            "Amazon",
            "Google",
            "Bloomberg"
        ]
    },
    {
        "category": "Binary Search",
        "title": "Floor and Ceil in Sorted Array",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/search-insert-position/",
        "alternate_title": "Floor in a Sorted Array",
        "alternate_url": "https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1",
        "pattern": "Lower Bound and Upper Bound Binary Search (Floor <= X, Ceil >= X)",
        "time_complexity": "O(log N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Binary Search",
            "Searching & Sorting"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Paypal"
        ]
    },
    {
        "category": "Binary Search",
        "title": "Find Rotation Count in Rotated Sorted Array",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/",
        "alternate_title": "Rotation Count in Rotated Sorted Array",
        "alternate_url": "https://www.geeksforgeeks.org/problems/rotation4723/1",
        "pattern": "Binary Search on Pivot / Inflection Point (Index of Minimum Element equals Rotation Count)",
        "time_complexity": "O(log N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Binary Search",
            "Searching & Sorting"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Google"
        ]
    },
    {
        "category": "Binary Search",
        "title": "Minimum Number of Days to Make m Bouquets",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/",
        "alternate_title": "Minimum Days to Make M Bouquets",
        "alternate_url": "https://www.geeksforgeeks.org/problems/minimum-days-to-make-m-bouquets/1",
        "pattern": "Binary Search on Day Range [min, max] (Adjacent Flower Feasibility Count)",
        "time_complexity": "O(N log(max - min))",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Binary Search",
            "Binary Search on Answer Range"
        ],
        "companies": [
            "Google",
            "Amazon",
            "Meta",
            "Bloomberg"
        ]
    },
    {
        "category": "Binary Search",
        "title": "Find the Smallest Divisor Given a Threshold",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/",
        "alternate_title": "Smallest Divisor Given a Threshold",
        "alternate_url": "https://www.geeksforgeeks.org/problems/smallest-divisor/1",
        "pattern": "Binary Search on Divisor Range [1, max(nums)] with Monotonic Division Sum Check",
        "time_complexity": "O(N log(max))",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Binary Search",
            "Binary Search on Answer Range"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Microsoft"
        ]
    },
    {
        "category": "Binary Search",
        "title": "Split Array Largest Sum",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/split-array-largest-sum/",
        "alternate_title": "The Painter's Partition Problem",
        "alternate_url": "https://www.geeksforgeeks.org/problems/the-painters-partition-problem1535/1",
        "pattern": "Binary Search on Answer Range [max_elem, sum_all] (Subarray Allocation Feasibility)",
        "time_complexity": "O(N log(sum - max))",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Binary Search",
            "Binary Search on Answer Range"
        ],
        "companies": [
            "Google",
            "Amazon",
            "Meta",
            "Microsoft",
            "Uber"
        ]
    },
    {
        "category": "Binary Search",
        "title": "Kth Missing Positive Number",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/kth-missing-positive-number/",
        "alternate_title": "Kth Missing Positive Number",
        "alternate_url": "https://www.geeksforgeeks.org/problems/kth-missing-element/1",
        "pattern": "Binary Search on Missing Count (arr[mid] - (mid + 1) < K)",
        "time_complexity": "O(log N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Binary Search"
        ],
        "companies": [
            "Meta",
            "Amazon",
            "Google"
        ]
    },
    {
        "category": "Binary Search",
        "title": "Matrix Median",
        "difficulty": "Hard",
        "problem_url": "https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/",
        "alternate_title": "Median in a row-wise sorted Matrix",
        "alternate_url": "https://www.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1",
        "pattern": "Binary Search on Value Range [1, 10^9] + Row-wise Upper Bound Count <= (R*C)/2",
        "time_complexity": "O(32 * R * log C)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Binary Search",
            "2D Matrix Binary Search"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Flipkart",
            "Samsung"
        ]
    },
    {
        "category": "Binary Search",
        "title": "Row with Maximum 1s",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/row-with-maximum-ones/",
        "alternate_title": "Row with Max 1s",
        "alternate_url": "https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1",
        "pattern": "Top-Right Pointer Step Search O(R+C) or Row Binary Search O(R log C)",
        "time_complexity": "O(R + C)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Binary Search",
            "Arrays and Strings"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Google"
        ]
    },
    {
        "category": "Binary Search",
        "title": "Find Peak Element II (2D Peak)",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/find-a-peak-element-ii/",
        "alternate_title": "Find Peak Element in 2D Matrix",
        "alternate_url": "https://www.geeksforgeeks.org/problems/peak-element-in-2d-matrix/1",
        "pattern": "Binary Search on Columns (Find Row Max in Mid Column & Compare Left/Right Neighbors)",
        "time_complexity": "O(R log C)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Binary Search",
            "2D Matrix Binary Search"
        ],
        "companies": [
            "Google",
            "Amazon",
            "Meta",
            "Microsoft"
        ]
    },
    {
        "category": "Sorting Algorithms",
        "title": "Sort Characters By Frequency",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/sort-characters-by-frequency/",
        "alternate_title": "Sort Characters By Frequency",
        "alternate_url": "https://www.geeksforgeeks.org/problems/frequency-sorting/1",
        "pattern": "Frequency Hash Map + Bucket Sort Array [N+1] or Max Heap",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Sorting Algorithms",
            "HashMap / HashSet"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Bloomberg",
            "Meta"
        ]
    },
    {
        "category": "Sorting Algorithms",
        "title": "Maximum Gap",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/maximum-gap/",
        "alternate_title": "Maximum Gap in Sorted Array",
        "alternate_url": "https://www.geeksforgeeks.org/problems/maximum-gap-in-array/1",
        "pattern": "Bucket Sort / Pigeonhole Principle (Bucket Min & Max Tracking in Linear Time)",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Sorting Algorithms"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Microsoft"
        ]
    },
    {
        "category": "Sorting Algorithms",
        "title": "Minimum Swaps to Sort",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/",
        "alternate_title": "Minimum Swaps to Sort",
        "alternate_url": "https://www.geeksforgeeks.org/problems/minimum-swaps-to-sort/1",
        "pattern": "Array Element-Index Pairing + Graph Cycle Decomposition (Swaps = sum(cycle_size - 1))",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "secondary_topics": [
            "Sorting Algorithms",
            "Graph BFS/DFS"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Goldman Sachs"
        ]
    },
    {
        "category": "Sorting Algorithms",
        "title": "Wiggle Sort II",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/wiggle-sort-ii/",
        "alternate_title": "Wiggle Sort II",
        "alternate_url": "https://www.geeksforgeeks.org/problems/wiggle-sort-ii/1",
        "pattern": "Quickselect Median Partition O(N) + Virtual 3-Way Index Rewiring",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Sorting Algorithms",
            "Two Pointers"
        ],
        "companies": [
            "Google",
            "Meta",
            "Amazon"
        ]
    },
    {
        "category": "Sorting Algorithms",
        "title": "Find All Duplicates in an Array",
        "difficulty": "Medium",
        "problem_url": "https://leetcode.com/problems/find-all-duplicates-in-an-array/",
        "alternate_title": "Find All Duplicates in an Array",
        "alternate_url": "https://www.geeksforgeeks.org/problems/find-duplicates-in-an-array/1",
        "pattern": "Cyclic Sort / In-Place Value Negation as Visited Flag",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Sorting Algorithms",
            "Cyclic Sort",
            "Arrays and Strings"
        ],
        "companies": [
            "Amazon",
            "Microsoft",
            "Meta",
            "Google"
        ]
    },
    {
        "category": "Sorting Algorithms",
        "title": "Set Mismatch",
        "difficulty": "Easy",
        "problem_url": "https://leetcode.com/problems/set-mismatch/",
        "alternate_title": "Set Mismatch (Find Duplicate and Missing)",
        "alternate_url": "https://www.geeksforgeeks.org/problems/set-mismatch/1",
        "pattern": "Cyclic Sort In-Place Swapping (nums[i] placed at nums[nums[i]-1])",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "secondary_topics": [
            "Sorting Algorithms",
            "Cyclic Sort"
        ],
        "companies": [
            "Amazon",
            "Google",
            "Microsoft"
        ]
    }
]
