#!/usr/bin/python

import urllib.request

condition_map = [
    ["Acquired immune deficiency syndrome", 52316],
    ["Active tuberculosis", 11480],
    ["Acute hepatitis C", 671],
    ["Acute nonparalytic poliomyelitis", 6047],
    ["Acute paralytic poliomyelitis", 19462],
    ["Acute poliomyelitis", 137581],
    ["Acute type A viral hepatitis", 41058],
    ["Acute type B viral hepatitis", 41277],
    ["Amebic dysentery", 11708],
    ["Anthrax", 7100],
    ["Aseptic meningitis", 41828],
    ["Babesiosis", 3300],
    ["Bacillary dysentery", 11094],
    ["Brucellosis", 20002],
    ["Campylobacteriosis", 4486],
    ["Chlamydia trachomatis infection", 7049],
    ["Chlamydial infection", 74097],
    ["Cholera", 101],
    ["Coccidioidomycosis", 10678],
    ["Congenital rubella syndrome", 187],
    ["Congenital syphilis", 3927],
    ["Cryptosporidiosis", 54082],
    ["Dengue", 83892],
    ["Dengue hemorrhagic fever", 10798],
    ["Dengue without warning signs", 16331],
    ["Diphtheria", 370739],
    ["Disease caused by West Nile virus", 611],
    ["Disorder of nervous system caused by West Nile virus", 11758],
    ["Dysentery", 10444],
    ["Encephalitis", 6736],
    ["Encephalitis lethargica", 29711],
    ["Giardiasis", 49482],
    ["Gonorrhea", 163739],
    ["Haemophilus influenzae infection", 59450],
    ["Haemophilus influenzae type b infection", 919],
    ["Hepatitis non-A non-B", 34073],
    ["Human anaplasmosis caused by Anaplasma phagocytophilum", 8464],
    ["Human ehrlichiosis caused by Ehrlichia chaffeensis", 9784],
    ["Infantile paralysis", 29654],
    ["Infection caused by Escherichia coli", 3581],
    ["Infection caused by Shiga toxin producing Escherichia coli", 35127],
    ["Infection caused by larvae of Trichinella", 653],
    ["Infection caused by non-cholerae vibrio", 765],
    ["Infective encephalitis", 46000],
    ["Inflammatory disease of liver", 26],
    ["Influenza", 221574],
    ["Intestinal infection caused by Escherichia coli O157:H7", 30579],
    ["Invasive Group A beta-hemolytic streptococcal disease", 19270],
    ["Invasive Streptococcus pneumoniae disease", 42208],
    ["Invasive drug resistant Streptococcus pneumoniae disease", 11686],
    ["Invasive meningococcal disease", 2063],
    ["Legionella infection", 67630],
    ["Leprosy", 14217],
    ["Listeriosis", 8599],
    ["Lobar pneumonia", 4209],
    ["Lyme disease", 51254],
    ["Malaria", 106082],
    ["Measles", 436932],
    ["Meningitis", 25812],
    ["Meningococcal infectious disease", 136449],
    ["Meningococcal meningitis", 126493],
    ["Mumps", 165242],
    ["Murine typhus", 2786],
    ["Ornithosis", 824],
    ["Pellagra", 29738],
    ["Pertussis", 297794],
    ["Pneumonia", 198788],
    ["Post-infectious encephalitis", 12918],
    ["Primary encephalitis", 26152],
    ["Rocky Mountain spotted fever", 71024],
    ["Rubella", 72676],
    ["Salmonella infection", 71824],
    ["Scarlet fever", 351882],
    ["Shigellosis", 63790],
    ["Smallpox", 260066],
    ["Smallpox without rash", 19],
    ["Spotted fever group rickettsial disease", 4742],
    ["Streptococcal sore throat", 4642],
    ["Syphilis", 47],
    ["Tetanus", 20251],
    ["Toxic shock syndrome", 10981],
    ["Tuberculosis", 392715],
    ["Tularemia", 43851],
    ["Typhoid and paratyphoid fevers", 58242],
    ["Typhoid fever", 345041],
    ["Typhus group rickettsial disease", 11447],
    ["Varicella", 97986],
    ["Viral hepatitis", 27341],
    ["Viral hepatitis type B", 95518],
    ["Viral hepatitis, type A", 80854],
    ["West Nile fever without encephalitis", 9850],
    ["Yellow fever", 68]
]

max_count = 20000

outfile = open("tyco_USA_all_data.csv","w")
skip_header = False

for condition in condition_map:
    
    count = condition[1]
    offset = 0
    while count > 0:
        condition_url = condition[0].replace(" ", "%20")
        url = "https://www.tycho.pitt.edu/api/query?apikey=ca9c5d59101a526ddcc7&ConditionName=" + condition_url + "&CountryISO=US&offset=" + str(offset) + "&limit=20000"

        print("Getting from url: " + url)
        req = urllib.request.urlopen(url)
        if skip_header:
            line = req.readline().decode("utf8")
#            print(line)
            col_num = len(line.split(','))
            if col_num is not 20:
                print("Column number is not 20")
                break
#            print(col_num)
        else:
            skip_header = True
        content = req.read()
        outfile.write(content.decode("utf8"))
        count -= max_count
        offset += max_count
        
        print(count)
    
outfile.close()

