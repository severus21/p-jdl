#!/usr/bin/env python3
# coding: utf-8
import os
from multiprocessing import Pool
from jdl_web.jdl_core.jdl import courbe2, data_final

def wrapper(args):
    if args[0].startswith("MARSEILLE-") or args[0].startswith("LYON-") or args[0] == "PARIS":
        return None

    location = f'static/jdl_web/graph_taille/{args[1]}-{args[0]}.png'
    if not os.path.exists(location):
        courbe2(*args, location)

cpls = [(row['NOM_COM'], row['CODE_DEPT'])  for _,row in data_final.iterrows()]
with Pool(7) as p:
    p.map(wrapper, cpls)
#courbe2("LYON", "69")
