ARTIFICIAL INTELLIGENCE LAB PROJECT PORTFOLIO

Introduction

This portfolio presents a collection of Artificial Intelligence applications developed to understand various problem-solving and reasoning techniques used in modern AI systems. The work covers game-playing strategies, intelligent recommendation systems, knowledge representation, and probabilistic decision-making models.

---

 Project 1: Game Playing Using AI Search Techniques



Search algorithms play a crucial role in game-playing AI. To study their behavior, a Tic-Tac-Toe environment was created where different search methods compete in selecting the most effective move.

 Techniques Studied

* Minimax Strategy
* Alpha-Beta Pruning
* Heuristic Search
* Monte Carlo Tree Search

Working Principle

Each algorithm analyzes the current board position and predicts future game states before making a move. The objective is to maximize the chances of winning while preventing the opponent from gaining an advantage.

Observations

* Minimax guarantees optimal decisions.
* Alpha-Beta reduces unnecessary exploration.
* Heuristic Search improves execution speed.
* MCTS relies on simulation-based decision making.

 Source Files

* search_algorithms.py
* test_search_algorithms.py

---

 Project 2: Verification Framework for Search Algorithms

Purpose

After implementing the search techniques, a separate testing framework was developed to ensure that each algorithm behaves correctly under different game situations.

Evaluation Scenarios

The algorithms were examined under several board conditions including:

* Winning opportunities
* Defensive situations
* Initial empty boards
* Draw configurations

 Outcome

The testing framework confirmed whether the generated moves matched the expected strategic behavior for each scenario.

---

 Project 3: Smart Travel Recommendation Assistant

 Overview

This project focuses on developing a recommendation system capable of generating travel plans according to user preferences. Instead of manually searching for destinations and accommodations, users receive automated suggestions.

 Functionalities

* Attraction recommendation
* Food suggestions
* Budget analysis
* Accommodation guidance
* Itinerary generation

Available Destinations

The knowledge repository currently contains information related to:

* Hyderabad
* Visakhapatnam
* Bengaluru

Inputs Considered

The planner takes into account:

* Travel destination
* Budget constraints
* Trip duration
* Personal interests
* Food preferences

Results Generated

The system produces a complete travel schedule together with estimated expenses and suitable recommendations.

---

 Project 4: Representation of Knowledge Using Graph Structures

 Overview

Knowledge graphs provide a powerful method for organizing and connecting information. This project demonstrates how entities and relationships can be represented in a graph-based structure.

 Example

A city can be connected to multiple related entities:

* Tourist attractions
* Transportation facilities
* Popular food items

Such relationships allow efficient retrieval and exploration of information.

 Technologies Explored

* Neo4j
* RDFLib
* GraphDB
* Protégé
* NetworkX

Learning Outcome

The project provided practical exposure to knowledge representation and graph-oriented data modelling.

---

 Project 5: Probabilistic Reasoning with Bayesian Networks

 Overview

Many real-world problems involve uncertainty. Bayesian Networks provide a mathematical framework for representing uncertain knowledge and performing probabilistic reasoning.

 Case Study

A disease prediction model was constructed using symptoms such as:

* Fever
* Cough
* Fatigue

The network analyzes symptom evidence and estimates the probability of a disease being present.

 Software Tools

* pgmpy
* GeNIe
* Netica
* BayesiaLab
* bnlearn

 Learning Outcome

The project demonstrated how probability theory can be integrated with AI systems to support inference and decision-making under uncertainty.

---

 Overall Learning

Through these projects, practical understanding was gained in several important AI domains including search strategies, automated planning, knowledge representation, graph modelling, testing methodologies, and probabilistic reasoning. The implementations illustrate how intelligent systems can analyze information, make decisions, and assist users in solving complex problems efficiently.
