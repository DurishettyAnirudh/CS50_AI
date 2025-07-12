#### 🎬 Degrees of Separation
This Python project finds the shortest path of connections between two actors or celebrities based on the movies they’ve starred in together.
It uses Breadth-First Search (BFS) to find the smallest number of degrees of separation, similar to the Kevin Bacon game.

#### 📌 Description
Given a dataset of people, movies, and which actors starred in which movies, this program can answer questions like:

“How is Emma Watson connected to Tom Hanks?”
or
“What is the shortest chain of movies connecting Actor A to Actor B?”

The program:

Loads data from CSV files (people.csv, movies.csv, stars.csv)

Builds an in-memory graph of people and movies

Uses BFS to find the shortest path between two people through shared movies

Resolves ambiguous names if there are multiple people with the same name

Clearly displays the connection step by step

#### 🗂️ How It Works
Graph Representation:

Nodes: People (actors)

Edges: Movies they starred in together

Search Algorithm:

Uses a QueueFrontier for BFS to find the shortest path.

Keeps track of explored nodes to avoid cycles.

Constructs the path backward from target to source.

Files:

people.csv — actor IDs, names, birth years

movies.csv — movie IDs, titles, years

stars.csv — links people to the movies they starred in

#### ▶️ How to Run

```bash
# Example usage:
python degrees.py [directory]
# If no directory is specified, it defaults to 'small'
# Directory should contain people.csv, movies.csv, stars.csv
```

You’ll be prompted to enter the names of two people. If a name is ambiguous, you can pick the intended person by ID.

#### ✅ Features
Handles name ambiguities.

Finds shortest connections efficiently.

Works for large datasets too (depending on CSV size).

#### 🧩 Learning Focus
Graph traversal with BFS

Real-world data structures: nodes, edges, frontiers

Handling real-world data ambiguity

Clear modular Python code

#### 📂 Example
```bash
Name: Emma Watson
Which 'Emma Watson'?
ID: 102, Name: Emma Watson, Birth: 1990
Intended Person ID: 102
Name: Tom Hanks
2 degrees of separation.
1: Emma Watson and John Doe starred in Some Movie
2: John Doe and Tom Hanks starred in Another Movie
✏️ Credits
This project structure is inspired by classic CS50 AI course exercises.
```