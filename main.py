import caesar
import vigenere

print('1.1. ', caesar.encrypt('PREMIER EXEMPLE', 'Y'))
print('1.2. ', caesar.decrypt('MZMV CV DFULCV UV TIPGKF', 'R'))
print('1.3. ', caesar.decrypt('KNS IZ UWJRNJW JCT'))

print('2.1. ', vigenere.encrypt('CAMARCHE', 'ROI'))
print('2.2. ', vigenere.decrypt(
    'XATBGYQBJTQVMUUEEZDDWEYEQELIPVGRWTWVROFMVVXEKRILJSGGTVFILYEFZDWEMTUEMQEUUSHTVLPAFLPRZUAMFIGNW', 'MASTER'))
