CFR: Counterfactual Regret Minimization
=======================================

[![License](https://img.shields.io/badge/license-Boost-blue.svg)](https://opensource.org/licenses/BSL-1.0)
[![](https://tokei.rs/b1/github/rhalbersma/cfr)](https://github.com/rhalbersma/cfr)

A [Python](http://isocpp.org) library implementing various counterfactual regret minimization algorithms for imperfect information games.

> #### Disclaimer
> This library is currently in a [pre-alpha](https://en.wikipedia.org/wiki/Software_release_life_cycle#Pre-alpha) stage. All code is subject to change without prior notice. 

##### Roadmap

The aim is to make a fully generic self-play algorithm that can be configured with the following parameters
- [ ] Update methods:
  - [x] CFR
  - [x] CFR+
  - [ ] Fictitious play
  - [ ] Hedge
- [ ] Graph methods:
  - [x] Full width ("vanilla")
  - [x] Chance sampling ("Monte Carlo")
- [ ] Optimizations:
  - [ ] Fixed strategy iteration
  - [ ] Pruning
- [ ] Games:
  - [x] Rock-Paper-Scissors
  - [ ] Liar Die
  - [ ] (optional, no promises!) any game in [Gambit EFG format](http://www.gambit-project.org/gambit13/formats.html) through its [PyAPI](http://www.gambit-project.org/gambit13/pyapi.html)
   - [ ] (long-term goal) Stratego

##### Acknowledgments

This library was inspired by [Todd W. Neller's](http://cs.gettysburg.edu/~tneller/) and [Marc Lanctot's](http://mlanctot.info/) lecture notes ["An Introduction to Counterfactual Regret Minimization"](http://cs.gettysburg.edu/~tneller/modelai/2013/cfr/). Their lecture notes, slides and original Java implementations for the games of [Rock-Paper-Scissors](https://en.wikipedia.org/wiki/Rock%E2%80%93paper%E2%80%93scissors), [Kuhn poker](https://en.wikipedia.org/wiki/Kuhn_poker), [Dudo](https://en.wikipedia.org/wiki/Dudo) and [Liar Die](https://en.wikipedia.org/wiki/Mia_(game)) have been added to this repository for archival purposes. 

License
-------

Copyright Rein Halbersma 2018.  
Distributed under the [Boost Software License, Version 1.0](http://www.boost.org/users/license.html).  
(See accompanying file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
