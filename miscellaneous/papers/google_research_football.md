- [paper](https://arxiv.org/abs/1907.11180)
- [blog](https://ai.googleblog.com/2019/06/introducing-google-research-football.html) 
- 足球对RL的挑战很大，因为需要平衡短期传控和高级策略之间的关系
- 谷歌的Research Football Environment给训练足球RL提供了一个环境，里面有物理3D引擎，让agents可以控制一个或者全部的足球运动员，学习如何传球，如何破解对手的防守。环境还提供了高度优化的游戏引擎，一系列足球任务的benchmarks，用于从易到难的RL场景，比如单刀，防反，传射，角球等。
- 谷歌提供的football engine可以通过球员的状态，或者直接通过图像进行学习。而且还可以选择是否加入随机干扰。这个足球引擎是跟OpenAI Gym具有同样的竞争力。研究人员甚至可以使用键盘，自己参与到游戏之中。
- football benchmarks是agents跟rule-based对手进行对战，分为简单的，中等的，和令人发狂的三个难度等级。- 谷歌提供了两个SOTA的RL算法的结果：DQN和IMPALA。谷歌尝试了两种不同的方案：1. reward只有进球 2. reward还包括把球运转到更接近球门的位置。
- [第一名的策略](https://www.kaggle.com/c/google-football/discussion/202232)

