# uxtotrack
python tools to track back uxtos, address and bitcoin stuff

run without arguments:

```
python3 utxotrack.py
```


```
Missing arguments expected:
python3 utxotrack.py <network> <txid> <level>
```

```
python3 utxotrack.py bitcoin a95e587f7ed6813b567c291f91db80785c5e5a3d73f97222f0d3dfcf04e988f3 1
```

Output:

```
Level 0 TX a95e587f7ed6813b567c291f91db80785c5e5a3d73f97222f0d3dfcf04e988f3 have 1 inputs and 1 outputs.
inputs:
adbed3a8ea57bb321ed93a39b5a7ef4424de876a7c2ebb254c82517d6555697e 1875 from bc1qyp8nuqvwfydg9svlm9cgyz3h4krfcrglue786g
Total involved addresses: 1
bc1qyp8nuqvwfydg9svlm9cgyz3h4krfcrglue786g : 1
Total involved txids: 1
adbed3a8ea57bb321ed93a39b5a7ef4424de876a7c2ebb254c82517d6555697e : 1
```

Minimum level is level 1, example with level 3, **repeated** TXID and Address are going to appear with different color:

![image](https://github.com/albertobsd/uxtotrack/assets/17832765/bccb8d04-1e1a-4ebb-8bfc-460b286ba043)

```
python3 utxotrack.py bitcoin a95e587f7ed6813b567c291f91db80785c5e5a3d73f97222f0d3dfcf04e988f3 3
```
```
Level 0 TX a95e587f7ed6813b567c291f91db80785c5e5a3d73f97222f0d3dfcf04e988f3 have 1 inputs and 1 outputs.
inputs:
adbed3a8ea57bb321ed93a39b5a7ef4424de876a7c2ebb254c82517d6555697e 1875 from bc1qyp8nuqvwfydg9svlm9cgyz3h4krfcrglue786g
Level 1 TX adbed3a8ea57bb321ed93a39b5a7ef4424de876a7c2ebb254c82517d6555697e have 2 inputs and 2 outputs.
inputs:
Detected repeated TX id: 5c6dded31f8db448690e7eeb57eb340029335b84f2d5c9bb0475527a1f505f24
Detected repeated address: bc1qzc6rjlyrqt6vfp5hjlhwx6nqeahyt4tqe6lcnr
5c6dded31f8db448690e7eeb57eb340029335b84f2d5c9bb0475527a1f505f24 3651 from bc1qzc6rjlyrqt6vfp5hjlhwx6nqeahyt4tqe6lcnr
5c6dded31f8db448690e7eeb57eb340029335b84f2d5c9bb0475527a1f505f24 3685 from bc1qzc6rjlyrqt6vfp5hjlhwx6nqeahyt4tqe6lcnr
Level 2 TX 5c6dded31f8db448690e7eeb57eb340029335b84f2d5c9bb0475527a1f505f24 have 2 inputs and 10 outputs.
inputs:
Detected repeated address: 3P8KDNJD19M2pZVkozVKdxqxPh5VhyXod5
bc918ad6752795087494f07b3f8d69bc1e2d0a49865e01606e54d1afe2e5a619 1073 from 3P8KDNJD19M2pZVkozVKdxqxPh5VhyXod5
e57f2edf96c3a1aaa2032c87d9a6f6df9a2709107cbf0d3379067e428d9f7afc 38773 from 3P8KDNJD19M2pZVkozVKdxqxPh5VhyXod5
Total involved addresses: 3
bc1qyp8nuqvwfydg9svlm9cgyz3h4krfcrglue786g : 1
bc1qzc6rjlyrqt6vfp5hjlhwx6nqeahyt4tqe6lcnr : 2
3P8KDNJD19M2pZVkozVKdxqxPh5VhyXod5 : 2
Total involved txids: 4
adbed3a8ea57bb321ed93a39b5a7ef4424de876a7c2ebb254c82517d6555697e : 1
5c6dded31f8db448690e7eeb57eb340029335b84f2d5c9bb0475527a1f505f24 : 2
bc918ad6752795087494f07b3f8d69bc1e2d0a49865e01606e54d1afe2e5a619 : 1
e57f2edf96c3a1aaa2032c87d9a6f6df9a2709107cbf0d3379067e428d9f7afc : 1
```

Please don't try something like level 10 or more, the program will take a lot of time in complete and you may get banned from mempool.space
