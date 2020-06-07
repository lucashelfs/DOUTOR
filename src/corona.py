"""
Given a JSON configuration file that specifies the dates and sections 
of the DOU that should be downloaded, filtered and posted to Slack, 
do all that. The configuration file keywords are:

USAGE:   corona.py 

Written by Henrique S. Xavier, hsxavier@gmail.com, on 23/jun/2019.
Adapted by Lucas Helfstein, on 25/mar/2020.
"""

import sys
import capture_driver as cd

config_file = '../configs/monitore_corona.json'

relevant_articles = cd.capture_DOU_driver(config_file)

values = []

# ARRUMAR VERIFICACAO DE TAMANHO DE NOME DE ARQUIVO!!
# Verificar o tamanho do conteudo que ira para as celulas. Nao pode passar de 50000 chars.
for i in range(len(relevant_articles)):
    for article in relevant_articles[i]:      
        value = [article['orgao'], article['identifica'], article['assina'], article['ementa'], article['pub_date'], article['url'], article['fulltext']]
        short_value = []
        for v in value:
            if v:
                if len(v) > 50000:
                    short_value.append('Texto muito grande para caber em uma célula.')
                else:
                    short_value.append(v)
            else:
                short_value.append(v)
        values.append(short_value)


# Split fulltext pelo assunto etc.
clean_values = []
for value in values:
    x = value
    if x[-1]:
        split_text = x[-1].split(x[1])
        if len(split_text) > 1:
            clean_text = split_text[1]
            print(clean_text)
            print()
            x[-1] = clean_text
    clean_values.append(x)


print(clean_values)
