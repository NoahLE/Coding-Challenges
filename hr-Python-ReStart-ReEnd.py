# https://www.hackerrank.com/challenges/re-start-re-end/problem

if __name__ == '__main__':
    # Get user input
    S = input()
    k = input()
    
    # Find start and end of all occurrences of string k in S
    # This is done by breaking S into pieces the same size as k, then, each piece is compared
    
    results_found = False

    for item in range(S.__len__()):        
        cutoff = k.__len__() + item
        current_snippet = S[item:cutoff]

        # If the snippet matches k, print the result
        if current_snippet == k:
            print("({start}, {end})".format(start=item, end=cutoff - 1))
            results_found = True

    # If no match is found
    if results_found is False:
        print("(-1, -1)")
