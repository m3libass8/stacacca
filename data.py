def anno_bisestile(anno):
    #funzione_verifica_anno_bisestile
    if(anno % 4==0 and anno % 100!=0) or (anno % 400==0):
        return True
    return False
def giorno_settimana(giorno, mese, anno):
    #funzione_verifica_giorno_mese_anno
    #usando_algoritmo_zeller
    if mese < 3 
        mese += 12
        anno -= 1
    k = anno % 100
    j = anno // 100
    f = giorno + (13*(mese + 1))// 5 + k + (k // 4) + (j // 4) - 2* j
    return (f % 7 + 7) % 7 