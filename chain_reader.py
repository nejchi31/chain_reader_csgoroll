import matplotlib.pyplot as plt
import numpy as np
import hashlib
import random
import string
import hmac
import csv

game_hash = '03423dcf7ad3b67ad5dd516cec8c2c512e4db941031242530bcaf714a42f66ef' # Update to latest game's hash for more results
first_game = "cadaaef371bc977aae209dc9be1a30665550adf89fa40fc17771051914d1f9fc"

def get_result(game_hash):
    INSTANT_CRASH_PERCENTAGE= 6.66
    hm = hmac.new(str.encode(game_hash), b'', hashlib.sha256)
    h = hm.hexdigest()
    h = int(h[:13], 16)
    e = 2**52
    result = (((100 * e - h) / (e-h)) // 1) 
    houseEdgeModifier = 1 - INSTANT_CRASH_PERCENTAGE / 100
    return max(100, result * houseEdgeModifier)

def get_prev_game(hash_code):
    m = hashlib.sha256()
    m.update(hash_code.encode("utf-8"))
    return m.hexdigest()

def export_data_to_file(game_hash, first_game):
    results = []
    count = 0
    with open('DATASET_ALL_17_2.csv', 'a', newline='') as fd:
        while game_hash != first_game:
            count += 1
            crash_result = round(get_result(game_hash)/100,2)
            results.append(crash_result)
            writerdata = csv.writer(fd)
            writerdata.writerow([crash_result])
            #print("written: " + result)
            game_hash = get_prev_game(game_hash)
    fd.close()
    return np.array(results)

results = export_data_to_file(game_hash, first_game)