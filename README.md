<p align="center">
  <img src="https://openclipart.org/image/800px/63805" width="400" title="hover text">
</p>

# Rock, Paper, Scissors

Simple rock, paper, scissors game with a slight twist! 

Unless you've been living under an actual rock, the rules of the game are simple: rock blunts scissors, scissors cuts paper and paper covers rock. You play against an opponent by simultaneously forming the shapes with your hands. The game is more than 4,000 years old! 

The twist in this implementation is that a human plays against an AI. As the game is repeated the AI gets 'smarter' and takes advantage of an interesting strategy which exploits the irrationalities present in human behaviours and actions. 
The AI 'strategy algorithm' is based on a series of observations that took place in a study conducted in China (Xu et al., 2013).

Yes... THERE ARE studies of people actually playing rock, paper, scissors. 

TL;DR: the study observed that players followed a 'win-stay, lose-shift strategy' in which: 

1. If a player wins, they are likely to play the hand their opponent played. E.g. If I win by playing rock, my next move should be scissors as I think my opponent will play paper.
2. If a player loses, they are likely to shift their hand to what would beat what their opponent played. E.g. If I lost playing scissors, my next play should be paper as I think my opponent will keep playing rock.

For the full paper, see [here.](https://www.sciencedirect.com/science/article/pii/S0378437113005578)



## How to play

When prompted, choose total number of games (`int`)

`rock` for rock, `paper` for paper, `scissors` for scissors. Couldn't have been easier!

When prompted, choose `y` to play the game or `n` to quit.

Have fun!

## Notes

I'm having trouble printing the ✌ emoji (which is part of the code) on my computer. Would love to know if this is also the case for others?

## License

[MIT](https://choosealicense.com/licenses/mit/)
