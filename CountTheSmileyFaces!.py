def count_smileys(arr):
    sf=0
    for i in arr:
        if set(i).issubset({'D', ':', '-', ';', '~', ')'}):
            sf+=1
    return sf

':)',':(',':D',':O',':;'