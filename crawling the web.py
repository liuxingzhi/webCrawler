#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 23:24:00 2017

"""

import requests
import seaborn as sns
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import networkx as nx

start = "http://whbc2000.lofter.com/"
start = "https://docs.python.org/3/tutorial/index.html"
def scrawl_all_links (url):
    links_dic = {} # Dict to hold adjacent sites
    scrape = [start] # Stack of links to visit
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0 Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0'}
    while scrape and len(links_dic) < 1000:
        page = scrape.pop()
        try:
            r = requests.get(page,headers = headers)
        except:
            continue
        soup = BeautifulSoup(r.text,"html5lib")
        for link in soup.find_all('a'):
    #        print(link)
            try:
                href = link.get('href')
    #            print(href)
            except requests.exceptions.ConnectionError:
                continue
            if not href or not href.startswith('http'):
                continue
            if not href in links_dic:
                links_dic[href] = [page]
                if href not in scrape:
                    scrape.append(href)
            else:
                links_dic[href].append(page)
        print("up to {} links.".format(len(links_dic)))
    return links_dic

link_dic = scrawl_all_links(start)

def graph_network (links_dic):
    network_graph = nx.Graph()
    network_graph.add_nodes_from(links_dic.keys())
    for node, adjacent in links_dic.items():
        for a in adjacent:
            network_graph.add_edge(node,a)
    with sns.axes_style('dark'):
        fig = plt.subplots(1,figsize=(13,10))
        nx.draw_networkx(network_graph,edge_color='#a4a4a4',with_labels = False, 
                         node_size=list(map(lambda x: len(x) * 8, links_dic.values())))
        plt.axis('off')
                
graph_network(link_dic)
