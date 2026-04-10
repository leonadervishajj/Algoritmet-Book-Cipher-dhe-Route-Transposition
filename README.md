# Book-Cipher-dhe-Route-Transposition.
Ky projekt paraqet dizajnin dhe implementimin e dy teknikave klasike të enkriptimit në fushën e Kriptografisë:
**- Book Cipher (zëvendësim i bazuar në indeks)**
**- Route Transposition Cipher (rregullim i bazuar në permutim)**

Qëllimi kryesor është demonstrimi i njohurive teorike dhe aftësive praktike në implementimin e algoritmeve kriptografike duke përdorur Python, si dhe aplikimi i praktikave të mira të zhvillimit të softuerit.

**📖 Book Cipher**

Book Cipher është një metodë e bazuar në zëvendësim, ku fjalët e mesazhit zëvendësohen me pozicionit (indekse) nga një tekst referencë(libër). 

**⚙️ Përshkrimi i Algoritmit**
***Enkriptimi***
Fillimisht merret mesazhi dhe teksti referencë, që dëshirojmë të enkriptojmë, dekriptojmë apo në të cilin duam të aplikojmë algoritmin. Pastaj, i njëjti tekst ndahet në fjalë të vetme. Pastaj krijohet struktura apo dictionary që lidh çdo fjalë me pozicionet e saj, dhe kçdo fjalë me pozicionet e kshtu çdo fjalë e mesazhit zëvendësohet me indeksin përkatës. 
