from collections import Counter

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def decrypt_affine(ciphertext, a, b, m=26):
    if gcd(a, m) != 1:
        return None
    
    a_inv = mod_inverse(a, m)
    if a_inv is None:
        return None
    
    result = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                x = ord(char) - ord('A')
                decrypted = (a_inv * (x - b)) % m
                result += chr(decrypted + ord('A'))
            else:
                x = ord(char) - ord('a')
                decrypted = (a_inv * (x - b)) % m
                result += chr(decrypted + ord('a'))
        else:
            result += char
    
    return result

def score_text(text):
    english_freqs = {
        'e': 12.02, 't': 9.10, 'a': 8.12, 'o': 7.68, 'i': 7.31, 'n': 6.95,
        's': 6.28, 'r': 6.02, 'h': 5.92, 'd': 4.32, 'l': 3.98, 'u': 2.88,
        'c': 2.71, 'm': 2.61, 'f': 2.30, 'y': 2.11, 'w': 2.09, 'g': 2.03,
        'p': 1.82, 'b': 1.49, 'v': 1.11, 'k': 0.69, 'x': 0.17, 'q': 0.11,
        'j': 0.10, 'z': 0.07
    }
    
    text = text.lower()
    text = ''.join(filter(str.isalpha, text))
    if not text:
        return 0
    
    counter = Counter(text)
    total = len(text)
    
    score = 0
    for char, count in counter.items():
        if char in english_freqs:
            observed_freq = count / total * 100
            expected_freq = english_freqs[char]
            score -= abs(observed_freq - expected_freq)
    
    common_words = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "it"]
    text_lower = text.lower()
    for word in common_words:
        if word in text_lower:
            score += 10
    
    return score

def frequency_analysis(ciphertext):
    english_common = 'etaoinsrhdlucmfywgpbvkxqjz'
    
    cleaned_text = ''.join(c.lower() for c in ciphertext if c.isalpha())
    if not cleaned_text:
        return []
    
    counter = Counter(cleaned_text)
    
    cipher_freq_order = sorted(counter.keys(), key=lambda c: counter[c], reverse=True)
    
    possible_keys = []
    
    for i in range(min(5, len(cipher_freq_order))):
        cipher_char = cipher_freq_order[i]
        
        for j in range(min(5, len(english_common))):
            plain_char = english_common[j]
            
            y = ord(cipher_char) - ord('a')
            x = ord(plain_char) - ord('a')
            
            for k in range(min(5, len(cipher_freq_order))):
                if k == i:
                    continue
                    
                cipher_char2 = cipher_freq_order[k]
                
                for l in range(min(5, len(english_common))):
                    if l == j:
                        continue
                        
                    plain_char2 = english_common[l]
                    
                    y2 = ord(cipher_char2) - ord('a')
                    x2 = ord(plain_char2) - ord('a')
                    
                    m = 26
                    diff_y = (y - y2) % m
                    diff_x = (x - x2) % m
                    
                    if gcd(diff_x, m) != 1:
                        continue
                    
                    diff_x_inv = mod_inverse(diff_x, m)
                    if diff_x_inv is None:
                        continue
                        
                    a = (diff_y * diff_x_inv) % m
                    
                    b = (y - a * x) % m
                    
                    if gcd(a, m) == 1:
                        possible_keys.append((a, b))
    
    return list(set(possible_keys))

def crack_affine(ciphertext):
    m = 26
    best_score = float('-inf')
    best_decryption = ""
    best_key = (0, 0)
    
    possible_keys = frequency_analysis(ciphertext)
    print(f"通过频率分析找到 {len(possible_keys)} 个可能的密钥")
    
    for a, b in possible_keys:
        decryption = decrypt_affine(ciphertext, a, b, m)
        if decryption:
            score = score_text(decryption)
            if score > best_score:
                best_score = score
                best_decryption = decryption
                best_key = (a, b)
    
    if best_score == float('-inf'):
        print("频率分析未能解决，尝试暴力破解")
        valid_a = [a for a in range(1, m) if gcd(a, m) == 1]
        
        for a in valid_a:
            for b in range(m):
                if (a, b) in possible_keys:
                    continue
                    
                decryption = decrypt_affine(ciphertext, a, b, m)
                if decryption:
                    score = score_text(decryption)
                    if score > best_score:
                        best_score = score
                        best_decryption = decryption
                        best_key = (a, b)
    
    return best_key, best_decryption

if __name__ == "__main__":
    cleaned_text = """
    Nu bslknxb swx glldxg wxkl nb jbjhmmz bhaxg hs swx mhbs dnujsx yz bldx bsklvx lo olksjux, yjs hmdlbs hmrhzb wnb bxubx lo ahmjxb nb pwhufxg. Wx yxpldxb dlkx hcckxpnhsnax lo swx dxhunuf lo mnox hug nsb cxkdhuxus bcnknsjhm ahmjxb. Ns whb losxu yxxu ulsxg swhs swlbx rwl mnax, lk whax mnaxg, nu swx bwhglr lo gxhsw yknuf h dxmmlr brxxsuxbb sl xaxkzswnuf swxz gl.
    Dlbs lo jb, wlrxaxk, shvx mnox olk fkhusxg. Rx vulr swhs lux ghz rx djbs gnx, yjs jbjhmmz rx cnpsjkx swhs ghz hb ohk nu swx ojsjkx. Rwxu rx hkx nu yjlzhus wxhmsw, gxhsw nb hmm yjs jundhfnuhymx. Rx bxmgld swnuv lo ns. Swx ghzb bskxspw ljs nu hu xugmxbb anbsh. Bl rx fl hyljs ljk cxssz shbvb, whkgmz hrhkx lo ljk mnbsmxbb hssnsjgx slrhkg mnox.
    Swx bhdx mxswhkfz, N hd hokhng, pwhkhpsxknqxb swx jbx lo hmm ljk ohpjmsnxb hug bxubxb. Lumz swx gxho hcckxpnhsx wxhknuf, lumz swx ymnug kxhmnqx swx dhunolmg ymxbbnufb swhs mnx nu bnfws. Chksnpjmhkmz glxb swnb lybxkahsnlu hccmz sl swlbx rwl whax mlbs bnfws hug wxhknuf nu hgjms mnox. Yjs swlbx rwl whax uxaxk bjooxkxg ndchnkdxus lo bnfws lk wxhknuf bxmgld dhvx swx ojmmxbs jbx lo swxbx ymxbbxg ohpjmsnxb. Swxnk xzxb hug xhkb shvx nu hmm bnfwsb hug bljugb whqnmz, rnswljs plupxuskhsnlu hug rnsw mnssmx hcckxpnhsnlu. Ns nb swx bhdx lmg bslkz lo uls yxnuf fkhsxojm olk rwhs rx whax jusnm rx mlbx ns, lo uls yxnuf plubpnljb lo wxhmsw jusnm rx hkx nmm.
    """

    print("开始破解仿射密码...")
    key, decrypted = crack_affine(cleaned_text)
    
    print(f"最可能的密钥: a={key[0]}, b={key[1]}")
    print("\n解密结果:")
    print(decrypted)