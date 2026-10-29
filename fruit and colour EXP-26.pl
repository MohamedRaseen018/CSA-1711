% Facts: Fruit and its colour
fruit_colour(apple, red).
fruit_colour(banana, yellow).
fruit_colour(grapes, green).
fruit_colour(orange, orange).
fruit_colour(mango, yellow).
fruit_colour(grapes, purple).
fruit_colour(strawberry, red).
fruit_colour(guava, green).

% Rule to find the colour of a fruit
colour(Fruit, Colour) :-
    fruit_colour(Fruit, Colour).
