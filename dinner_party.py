#!/usr/local/bin/python3

import random
import time

def main():
    dinner = DinnerParty()
    people = dinner.parse_file("hw1-inst1.txt")
    table = Table(len(people), people)
    table.seat()
    print(table.calculate_score())
    for index, person in enumerate(table.guests):
        print(person.ID, index)

class DinnerParty(object):
    """docstring for DinnerParty"""
    def __init__(self):
        super(DinnerParty, self).__init__()     
    # one interresting fact for me is that even though
    # a method only take one param python passes 2 params 
    # to the function: self AND filename
    def parse_file(self, filename):
        file = open(filename)
        index = 0
        people = []
        numberOfGuests = int(file.readline())
        for line in file:
            index += 1
            if index <= numberOfGuests/2:
                gender = True   #Female
            else:
                gender = False  # Male
            likeness = line.split()
            likeness = [int(i) for i in likeness]
            person = Person(index, likeness, gender)
            people.append(person)
        file.close()
        return people
    # This is a method used to output the result
    def write_output(self, table):
        file = open("hw1-sol1.txt", "wt")
        for t in table:
            # write can only takes string not a list
            file.write(",".join(map(str, t.preference)))
        file.close()

class Person(object):
    """docstring for Person"""
    def __init__(self, ID, preference, gender):
        super(Person, self).__init__()
        self.ID = ID
        self.preference = preference
        self.gender = gender

    def preference_func(self, person_id):
        return self.preference[person_id - 1]
        
class Table(object):
    """docstring for Table"""
    def __init__(self, numberOfChairs, guests):
        super(Table, self).__init__()
        self.numberOfChairs = numberOfChairs
        self.guests = guests

    def seat(self):
        self.initial_state()
        end_time = time.clock() + 20
        while True:
            if time.clock() > end_time:
                break
            else:
                self.generate_state()

    def initial_state(self):
        random.shuffle(self.guests)

    def generate_state(self):
        # this method uses local search or hill climbing in AI
        best_score = self.calculate_score()
        best_table = Table(self.numberOfChairs, self.guests)
        glist = best_table.guests
        index = random.randint(0, self.numberOfChairs - 1)
        for person in glist:
            a, b = index, glist.index(person)
            if a != b:
                glist[b], glist[a] = glist[a], glist[b]
                cur_score = best_table.calculate_score()
                if cur_score > best_score:
                    best_score = cur_score
                    self.guests = list(glist)
                # swap back to prepare for the next loop
                glist[b], glist[a] = glist[a], glist[b]


    def calculate_score(self):
        # What we gonna do in this method is to traverse half of 
        # the length of the list since the list represents for 
        # a table of 2 sides
        score = 0
        for i in range(0, int(len(self.guests)/2) - 1):
            # calculate the top row first
            # adjacent different in gender add 1 point
            p1 = self.guests[i]
            p2 = self.guests[i + 1]
            if p1.gender != p2.gender:
                score += 1
            # h(p1,p2) + h(p2,p1) for adjacent pair of 2 people
            score += p1.preference_func(p2.ID) + p2.preference_func(p2.ID)
            # 2 points for opposite pair in different gender
            p2 = self.guests[int(len(self.guests)/2) + i]
            if p1.gender != p2.gender:
                score += 2
            # h(p1,p2) + h(p2,p1) for opposite pair of 2 people 
            score += p1.preference_func(p2.ID) + p2.preference_func(p2.ID)
            # now for the bottom row
            p1 = self.guests[int(len(self.guests)/2) + i]
            p2 = self.guests[int(len(self.guests)/2) + i + 1]
            if p1.gender != p2.gender:
                score += 1
            score += p1.preference_func(p2.ID) + p2.preference_func(p2.ID)  
        #last pair in the table
        p1 = self.guests[int(len(self.guests)/2) - 1]
        p2 = self.guests[len(self.guests) - 1]
        if p1.gender != p2.gender:
            score += 1
        score += p1.preference_func(p2.ID) + p2.preference_func(p2.ID)
        return score

if __name__ == '__main__':
    main()