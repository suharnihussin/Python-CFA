#!/usr/bin/env python

import random

def main():
    #Title.
    print("JOM TEKA PERMAINAN!")
    print("*********************************************")
    
    #pilihan permainan
    games = ["BOLA TAMPAR", "SEPAK TAKRAW", "BOLA JARING", "BOLA BALING", "BOLA SEPAK", "RUGBY", "FUTSAL"]
    
    #jawapan pilihan akan ditukar ke huruf besar
    chosen_game = random.choice(games).upper()
    max_trials = 3 #bilangan percubaan

    #proses percubaan menjawab tidak melebihi 3x
    for _ in range(max_trials):
        guess = input("PERMAINAN INI MEMERLUKAN LEBIH DARI SEORANG PEMAIN DAN MENGGUNAKAN SEBIJI BOLA. CUBA TEKA PERMAINAN APAKAH YANG SAYA SEDANG FIKIRKAN?").strip().upper()
        
        #jika pilihan user = tekaan
        if guess == chosen_game:
            print(f"TAHNIAH!! JAWAPAN '{guess}' ADALAH BETUL!")
            break
        else:
            print(f"MAAF, '{guess}' ADALAH TEKAAN YANG SALAH.")
            if max_trials > 1:
                print(f"ANDA MEMPUNYAI {max_trials - 1} CUBAAN LAGI.")
            else:
                print(f"CUBAAN TAMAT! PERMAINAN YANG SAYA SEDANG FIKIRKAN IALAH PERMAINAN '{chosen_game}'.")
        max_trials -= 1 #bil percubaan akan berkurang

main()