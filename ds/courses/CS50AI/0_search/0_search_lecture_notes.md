# CS50AI Lecture 0 - Search

## Terminology

- agent: entity that perceives its environment and acts upon that environment
- state: a configuration of the agent and its environment
- initial state: the state in which the agent begins
- actions: choices that can be made in a state
  - `actions(s)` returns the set of actions that can be executed in state `s`
- transition model: a description of what state results from performing any applicable action in any state
  - `result(s, a)` returns the state resulting from performing action `a` in state `s`
- state space: the set of all states reachable from the initial state by any sequence of actions
  - Can be represented as a graph, each node a state, each arrow an action
- goal test: way to determine whether a given state is a goal state
- path cost: numerical cost associated with a given path
- solution: a sequence of actions that leads from the initial state to a goal state
- optimal solution: a solution that has the lowest path cost among all solutions

### Search problems

- initial state
- actions
- transition model
- goal test
- path cost function

### Node

A data structure that keeps track of:

- a state
- a parent (node that generated it)
- an action (action applied to parent to get node)
- a path cost (from initial state to node)

## Approach

- Start with a frontier that contains the initial state
- Repeat:
  - If frontier is empty, then no solution
  - Otherwise, remove a node from the frontier
  - If node contains goal state, return the solution
  - Expand node, add resulting nodes to frontier

### Revised approach

- Start with a frontier that contains the initial state
- Start with an empty "explored" set
- Repeat:
  - If frontier is empty, then no solution
  - Otherwise, remove a node from the frontier
  - If node contains goal state, return the solution
  - Add the node to the "explored" set
  - Expand node, add resulting nodes to frontier if they aren't already in the frontier or the "explored" set
