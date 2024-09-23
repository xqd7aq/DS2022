#!/bin/bash


clear
echo "Let's build a mad-lib!"
read -p "1. Name an unusual sport: " NOUN1
read -p "2. Favorite time of the day " ADJ1
read -p "3. Name an unusual color: " ADJ2
read -p "4. What is your name?: " NOUN3
read -p "5. What is you favority drink?: " NOUN4
read -p "6. What is your favorite cereal? " NOUN5
read -p "7. What is your favorite fruit?: " NOUN6
read -p "8. What is yout favorite palce to visit? " NOUN7

echo "Once upon a time $NOUN3 went to the store to get a box of $NOUN4."
echo "But they ran into a $ADJ2 named Frank. Frank said he was here to get $ADJ1 $NOUN5."
echo "Then Frank had to leave to $NOUN7 to play with $NOUN6"
