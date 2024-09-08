#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 20:51:29 2023

@author: parthmehta
"""
#Finds top 10 people in the leaderboard
class Leaderboard():
    #Method for finding top ten
    def findTop10():
        #Array for unsorted names and scores
        nameList = []
        scoreList = []
        #Reads name file and places in array, still unsorted
        with open('names.txt', 'r') as file1:
            for line in file1:
                try:
                    nameList.append(line[:line.index('\n')])
                except:
                    nameList.append(line)
        #Reads score file and places in array, still unsorted
        with open('scores.txt', 'r') as file2:
            for line in file2:
                try:
                    scoreList.append(int(line[:line.index('\n')]))
                except ValueError:
                    scoreList.append(int(line))
                
        #Finds index of top 10 scores in score array
        res = sorted(range(len(scoreList)), key = lambda sub: scoreList[sub])[-10:]
        
        #Output array
        topNames = []
        topScores = []

        #Uses res as a key for finding and placing real scores and names into output
        for i in res:
            topNames.append(nameList[i])
            topScores.append(scoreList[i])

        #Returns matrix of matrix of names and scores, almost like a table
        return [topScores, topNames]
        

        

