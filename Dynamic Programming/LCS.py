def lcs(s1, s2, m, n):
    L = [[0 for x in range(n+1)] for x in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    
    index = L[m][n]
    LCS_algo = [""] * (index+1)
    LCS_algo[index] = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            LCS_algo[index-1] = s1[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
    print("S1 : " + s1 + "\nS2 : " + s2)
    print("LCS :" + "".join(LCS_algo))
    
if __name__ == "__main__":
    
    S1 = "ACADB"
    S2 = "CBDA"
    m = len(S1)
    n = len(S2)
    lcs(S1, S2, m, n)
                
                
                             
    