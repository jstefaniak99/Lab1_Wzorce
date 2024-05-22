import time

def naive_method(text, pattern):
    n = len(text) 
    m = len(pattern)
    result = []
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            result.append(i)
    
    return result

text = "Loremipabcsumdolorsitametconsecteturabc"
pattern = "abc"

start = time.time()
naive_result = naive_method(text, pattern)
end = time.time()

execution_time = end - start
print("Naiwne wyszukiwanie:", naive_result)
print(f"Czas wykonania: {execution_time:.8f} sekund")