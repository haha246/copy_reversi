# Reversi Game Project
### Prerequsite
```
$ pip install pygame
$ pip install tqdm
$ pip install numpy
```
### Repo structure
```
.
├── README.md
├── agent
│   └── base_agent.py
│   └── moose1108.py(這個是自動下棋的主程式)
├── arena.py
├── board.py
├── env.py
├── font
│   ├── LICENSE.txt
│   └── OpenSans-Regular.ttf
├── pygamewrapper.py
├── reversi.py
├── reversi_board.py
└── utils.py
```


### Usage
```
$ git clone https://github.com/haha246/copy_reversi
$ cd copy_reversi
$ python3 arena.py --time_limit=600000
```
Now you can play with an AI

OR use this to test 我們寫的自動下棋程式
```
$ python3 arena.py --agent1 moose1108.MyAgent --agent2 base_agent.RandomAgent
```

### Team members
- Team leader:
    - name: 蔡孟錡
    - student_id: B09902023
    - github: [moose1108](https://github.com/moose1108)
- member:
    - name: 陳剛頡
    - student_id: B09902125
    - github: [B09902125](https://github.com/B09902125)
- member:
    - name: 呂建廷
    - student_id: B09902109
    - github: [haha246](https://github.com/haha246)
