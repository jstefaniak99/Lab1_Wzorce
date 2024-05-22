import time

def bad_character(pattern):
    # Tworzymy tablicę o rozmiarze 256 (dla wszystkich możliwych znaków ASCII)
    bad_char = [-1] * 256
    
    # Wypełniamy tablicę indeksami ostatnich wystąpień znaków we wzorcu
    for i in range(len(pattern)):
        bad_char[ord(pattern[i])] = i
    print("Podgląd jak wygląda wywołanie funkcji bad_character")
    print(bad_char)
    return bad_char

def boyer_moore_search(text, pattern):
    n = len(text)   
    m = len(pattern) 
    bad_char = bad_character(pattern)
    result = []

    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]: # porównanie wzorca z tekstem od prawej do lewej strony
            j -= 1
        # Jeśli wzorzec pasuje (indeks j staje się -1)
        if j < 0:
            result.append(s)
            s += (m - bad_char[ord(text[s + m])] if s + m < n else 1)
        else:
            # Przesuwamy wzorzec zgodnie z heurystyką złego znaku
            s += max(1, j - bad_char[ord(text[s + j])])
    return result

text = "Loremipabcsumdolorsitametconsecteturabc"
pattern = "abc" # Nasza reprezentacja (a - 0, b - 1, c - 2)

start_time = time.time()
bm_result = boyer_moore_search(text, pattern)
end_time = time.time()

# Wynik i czas wykonania
execution_time = end_time - start_time
print("Boyer-Moore wyszukiwanie:", bm_result)
print(f"Czas wykonania: {execution_time:.10f} sekund")
