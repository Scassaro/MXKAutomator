def determineZPERF(banknum):
    zperfdict = dict.fromkeys(["18","19","205","206","224"], "1")
    zperfdict.update(dict.fromkeys(["7","8","225","226","227"], "2"))
    zperfdict.update(dict.fromkeys(["9","10","17","201","202"], "3"))
    zperfdict.update(dict.fromkeys(["11","12","13","106","107"], "4"))
    zperfdict.update(dict.fromkeys(["1","2","105","220","221"], "5"))
    zperfdict.update(dict.fromkeys(["3","4","104","207","208"], "6"))
    zperfdict.update(dict.fromkeys(["101","102","103","228","239"], "7"))
    zperfdict.update(dict.fromkeys(["14","15","203","204","213"], "8"))
    zperfdict.update(dict.fromkeys(["0","25","126","192","248"], "9"))
    zperfdict.update(dict.fromkeys(["5","6","209","211"], "10"))
    zperfdict.update(dict.fromkeys(["20","21","222","223"], "11"))
    zperfdict.update(dict.fromkeys(["121","123","124","229","230"], "12"))
    zperfdict.update(dict.fromkeys(["16","22","122","175","176"], "13"))
    zperfdict.update(dict.fromkeys(["23","119","125","173","231"], "14"))
    zperfdict.update(dict.fromkeys(["112","120","127","128","212"], "15"))
    zperfdict.update(dict.fromkeys(["108","109","110","111"], "16"))
    zperfdict.update(dict.fromkeys(["30","31","32","33","118"], "17"))
    zperfdict.update(dict.fromkeys(["34","35","36","37","117"], "18"))
    zperfdict.update(dict.fromkeys(["38","39","60","61","113"], "19"))
    zperfdict.update(dict.fromkeys(["40","41","64","65","114"], "20"))
    zperfdict.update(dict.fromkeys(["42","43","44","45","46"], "21"))
    zperfdict.update(dict.fromkeys(["47","66","67","68","69"], "22"))
    zperfdict.update(dict.fromkeys(["70","71","72","73","74"], "23"))
    zperfdict.update(dict.fromkeys(["48","49","75","76","77"], "24"))
    zperfdict.update(dict.fromkeys(["26","116","130","193"], "25"))
    zperfdict.update(dict.fromkeys(["161","162","163","164","165"], "26"))
    zperfdict.update(dict.fromkeys(["166","167","168","169","170"], "27"))
    zperfdict.update(dict.fromkeys(["150","171","172","177","178"], "28"))
    zperfdict.update(dict.fromkeys(["151","152","153","154","155"], "29"))
    zperfdict.update(dict.fromkeys(["148","149","156","157","158"], "30"))
    zperfdict.update(dict.fromkeys(["129","131","132"], "31"))
    zperfdict.update(dict.fromkeys(["136","137","138","139","140"], "32"))
    zperfdict.update(dict.fromkeys(["28","29","141","142","143"], "33"))
    zperfdict.update(dict.fromkeys(["82","83","84","85","86"], "34"))
    zperfdict.update(dict.fromkeys(["87","88","89","90","91"], "35"))
    zperfdict.update(dict.fromkeys(["92","93","94","95","96"], "36"))
    zperfdict.update(dict.fromkeys(["97","98","99","100","179"], "37"))
    zperfdict.update(dict.fromkeys(["180","181","182","183","184"], "38"))
    zperfdict.update(dict.fromkeys(["185","186","187","188","189"], "39"))
    zperfdict.update(dict.fromkeys(["62","78","79","80","81"], "40"))
    zperfdict.update(dict.fromkeys(["190","191","194","195","196"], "41"))
    zperfdict.update(dict.fromkeys(["63","197","198","199","200"], "42"))
    zperfdict.update(dict.fromkeys(["246","247"], "43"))

    returnstring = "10.57.100.1"
    if(int(zperfdict[banknum]) < 10):
        returnstring += "0" 
    return(returnstring + zperfdict[banknum])

def determineSuper(banknum):
    # Dupers in order
    superdict = dict.fromkeys(["150", "152", "153", "154", "155", "149", "156", "157", "158"], "62")
    superdict.update(dict.fromkeys(["151", "136", "137", "138", "139", "140", "28", "141", "142", "143"], "63"))
    superdict.update(dict.fromkeys(["87", "88", "89", "90", "91", "92", "93", "94", "95", "96"], "73"))
    superdict.update(dict.fromkeys(["97", "98", "99", "100", "179", "180", "181", "182", "183", "184"], "74"))
    superdict.update(dict.fromkeys(["185", "186", "187", "188", "189", "190", "191", "194", "195", "196"], "75"))
    superdict.update(dict.fromkeys(["78", "79", "80", "81", "63", "197", "198", "199", "200"], "76"))

    # Novas in order
    superdict = dict.fromkeys(["0", "21", "229", "230", "23", "40", "29"], "51")
    superdict.update(dict.fromkeys(["239", "25", "119", "112", "120", "127", "108", "109", "111", "34", "35", "36", "37", "61", "62"], "52"))
    superdict.update(dict.fromkeys(["225", "9", "10", "14", "126", "123", "124", "125", "128", "30", "31", "32", "33", "41"], "53"))
    superdict.update(dict.fromkeys(["7", "8", "11", "12", "13", "1", "2", "3", "4", "5", "6", "211", "118", "117", "64", "114"], "54"))
    superdict.update(dict.fromkeys(["18", "19", "205", "206", "17", "201", "202", "15", "209", "20", "16", "212", "60", "113"], "55"))
    superdict.update(dict.fromkeys(["220", "207", "208", "203", "204", "213", "192", "173", "231"], "56"))
    superdict.update(dict.fromkeys(["42", "43", "44", "45", "46", "47", "66", "67", "68", "69", "70", "71", "72", "73", "74", "48", "49"], "57"))
    superdict.update(dict.fromkeys(["106", "107", "105", "104", "101", "102", "103", "248", "65", "193", "177", "178"], "58"))
    superdict.update(dict.fromkeys(["161", "162", "163", "164", "165", "166", "167", "168", "169", "170", "171", "172"], "59"))
    superdict.update(dict.fromkeys(["224", "226", "227", "221", "228", "222", "223", "121", "22", "38", "39", "116"], "60"))
    superdict.update(dict.fromkeys(["175", "176", "130", "148", "131", "132", "82", "83", "84", "85", "86"], "61"))
                                            
    # Supernet01
    if(int(banknum) == 122 or int(banknum) == 129):
        returnstring = "172.24.84.92"
    else:
        returnstring = "10.57.100.1" + superdict[banknum]

    return(returnstring)
